from textual import on
from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Button, Label


class CountClickApp(App):
    CSS_PATH = "style.tcss"

    def __init__(self, *a, **kw) -> None:
        super().__init__(*a, **kw)
        self.clicks = 0

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Label(id="label_clicks")
            yield Button("Нажать", id="button_click")
            yield Button("Очистить", id="button_clear")

    def on_ready(self) -> None:
        self.update()
        self.set_interval(0.1, self.update)

    @on(Button.Pressed, "#button_click")
    def clicker(self, event: Button.Pressed) -> None:
        self.clicks += 1

    @on(Button.Pressed, "#button_clear")
    def clear_clicks(self, event: Button.Pressed) -> None:
        self.clicks = 0

    def update(self) -> None:
        lb: Label = self.query_one("#label_clicks")
        lb.update(str(self.clicks))


if __name__ == "__main__":
    CountClickApp().run()
