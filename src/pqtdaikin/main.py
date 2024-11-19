from sys import argv
from typing import TYPE_CHECKING
from typing import Protocol

from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication

if TYPE_CHECKING:
    from collections.abc import Callable

    from PySide6.QtWebEngineCore import QWebEnginePage


class PQtDaikin(Protocol):
    def show(self) -> None: ...


def pf(prefix: str) -> 'Callable[..., None]':
    return lambda *args, **kwargs: print(prefix, *args, **kwargs)  # noqa: T201


def on_render_process_terminated(
    termination_status: 'QWebEnginePage.RenderProcessTerminationStatus',
    exit_code: int,
) -> None:
    pass


def pqtdaikin(app: QApplication) -> PQtDaikin:
    args = app.arguments()
    url = args[1] if len(args) > 1 else 'https://www.google.com'

    view = QWebEngineView()

    view.loadStarted.connect(pf('loadStarted'))
    view.loadProgress.connect(pf('loadProgress'))
    view.renderProcessTerminated.connect(on_render_process_terminated)
    view.loadFinished.connect(pf('loadFinished'))

    view.load(QUrl(url))
    return view


def main() -> None:
    app = QApplication(argv)

    widget = pqtdaikin(app)
    widget.show()

    raise SystemExit(app.exec())
