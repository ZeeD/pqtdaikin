from os import environ
from pathlib import Path
from typing import TYPE_CHECKING
from typing import Final
from typing import Literal
from typing import override

from httpx import AsyncClient
from httpx import Auth
from httpx import Request as httpx_Request
from httpx import Response as httpx_Response
from ludic.catalog.buttons import ButtonSuccess
from ludic.catalog.layouts import Cluster
from ludic.catalog.pages import Body
from ludic.catalog.pages import Head
from ludic.catalog.pages import HtmlPage
from ludic.web import LudicApp
from ludic.web import Request
from starlette.responses import RedirectResponse
from starlette.responses import Response
from uvicorn import run

if TYPE_CHECKING:
    from collections.abc import Generator

    from ludic.components import BaseComponent

app = LudicApp()

ACCESS_TOKEN: str | None = None
REFRESH_TOKEN: str | None = None

SOGGIORNO: Final = 'DaikinAP13459 - sogg'
EMBEDDED_ID: Final = 'climateControl'


class BearerToken(Auth):
    def __init__(self, token: str) -> None:
        self.token = token

    @override
    def auth_flow(
        self, request: httpx_Request
    ) -> 'Generator[httpx_Request, httpx_Response, None]':
        request.headers['Authorization'] = f'Bearer {self.token}'
        yield request


@app.get('/')
async def index(request: Request) -> 'BaseComponent|Response':
    global ACCESS_TOKEN
    global REFRESH_TOKEN

    if ACCESS_TOKEN is None or REFRESH_TOKEN is None:
        client_id = environ['client_id']
        client_secret = environ['client_secret']

        state: str | None = request.query_params.get('state')
        code: str | None = request.query_params.get('code')

        if state is None and code is None:
            return RedirectResponse(
                url=(
                    'https://idp.onecta.daikineurope.com/v1/oidc/authorize?'
                    f'response_type=code&client_id={client_id}&'
                    'redirect_uri=https://pqtdaikin.local&'
                    'scope=openid%20onecta:basic.integration'
                )
            )

        async with AsyncClient() as client:
            r = await client.post(
                'https://idp.onecta.daikineurope.com/v1/oidc/token?'
                f'grant_type=authorization_code&client_id={client_id}&'
                f'client_secret={client_secret}&code={code}&'
                'redirect_uri=https://pqtdaikin.local'
            )
        response = r.json()
        ACCESS_TOKEN = response['access_token']
        REFRESH_TOKEN = response['refresh_token']
        return RedirectResponse(url='/')

    async with AsyncClient() as client:
        # info = (await client.get('https://api.onecta.daikineurope.com/v1/info',auth=BearerToken(ACCESS_TOKEN))).json()
        r = await client.get(
            'https://api.onecta.daikineurope.com/v1/gateway-devices',
            auth=BearerToken(ACCESS_TOKEN),
        )
    gateway_devices = r.json()

    # get gateway_device_id, on_off_mode
    gateway_device_id: str | None = None
    on_off_mode: Literal['on', 'off'] | None = None

    for gateway_device in gateway_devices:
        gateway_device_id = gateway_device['id']
        for management_point in gateway_device['managementPoints']:
            if management_point['embeddedId'] != EMBEDDED_ID:
                continue
            on_off_mode = management_point['onOffMode']['value']
            if management_point['name']['value'] == SOGGIORNO:
                break

    if gateway_device_id is None or on_off_mode is None:
        raise ValueError

    return HtmlPage(
        Head(favicon='data:image/x-icon;base64,', load_styles=False),
        Body(
            render_on_off_mode(gateway_device_id, on_off_mode),
            htmx_enabled=True,
        ),
    )


def render_on_off_mode(
    gateway_device_id: str, on_off_mode: str
) -> 'BaseComponent':
    return Cluster(
        'DaikinAP13459 - sogg',
        on_off_mode,
        'gateway_device_id',
        gateway_device_id,
        ButtonSuccess(
            'toggle',
            hx_post=app.url_path_for(
                'toggle_on_off_mode',
                gateway_device_id=gateway_device_id,
                on_off_mode='on' if on_off_mode == 'off' else 'off',
            ),
            hx_target='#on_off_mode',
        ),
        id='on_off_mode',
    )


@app.post('/on-off-mode/{gateway_device_id:str}/{on_off_mode:str}')
async def toggle_on_off_mode(
    gateway_device_id: str, on_off_mode: str
) -> 'BaseComponent':
    if ACCESS_TOKEN is None:
        raise ValueError
    async with AsyncClient() as client:
        r = await client.patch(
            f'https://api.onecta.daikineurope.com/v1/gateway-devices/{gateway_device_id}/management-points/{EMBEDDED_ID}/characteristics/onOffMode',
            auth=BearerToken(ACCESS_TOKEN),
            json={'value': on_off_mode},
        )
    print(f'{r.status_code=}')
    if r.status_code != 204:
        raise ValueError(r.json())
    return render_on_off_mode(gateway_device_id, on_off_mode)



def main() -> None:
    root = Path(__file__).parents[2]
    run(
        f'{__name__}:app',
        host='pqtdaikin.local',
        port=8443,
        reload=True,
        ssl_keyfile=root / '_wildcard.local+3-key.pem',
        ssl_certfile=root / '_wildcard.local+3.pem',
        env_file=root / '.env',
    )


if __name__ == '__main__':
    main()
