from typing import override

from ludic.attrs import NoAttrs
from ludic.catalog.buttons import ButtonDanger
from ludic.catalog.buttons import ButtonSuccess
from ludic.catalog.layouts import Cluster
from ludic.catalog.pages import Body
from ludic.catalog.pages import Head
from ludic.catalog.pages import HtmlPage
from ludic.components import Component
from ludic.html import b
from ludic.types import AnyChildren
from ludic.web import LudicApp
from uvicorn import run

app = LudicApp()


class Page(Component[AnyChildren, NoAttrs]):
    @override
    def render(self) -> HtmlPage:
        return HtmlPage(
            Head(favicon='data:image/x-icon;base64,', load_styles=False),
            Body(*self.children, htmx_enabled=True),
        )


@app.get('/')
def index() -> Page:
    return Page(counter(0))


@app.get('/counter/{number:int}')
def counter(number: int) -> Cluster:
    return Cluster(
        ButtonDanger(
            '-',
            disabled=number <= 0,
            hx_get=app.url_path_for('counter', number=max(0, number - 1)),
            hx_target='#counter',
        ),
        b(number),
        ButtonSuccess(
            '+',
            hx_get=app.url_path_for('counter', number=number + 1),
            hx_target='#counter',
        ),
        id='counter',
    )


def main() -> None:
    run(f'{__name__}:app', reload=True)
