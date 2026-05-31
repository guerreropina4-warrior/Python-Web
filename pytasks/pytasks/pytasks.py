"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    count: int = 0

    def incrementar(self):
        self.count += 1

    def decrementar(self):
        self.count -= 1


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Contador Interactivo", size="7"),
            rx.text("Aprendiendo State y Event Handlers"),
            rx.heading(State.count, size="9", color="blue"),
            rx.hstack(
                rx.button("➖", on_click=State.decrementar, color_scheme="red"),
                rx.button("➕", on_click=State.incrementar,
                          color_scheme="green"),
                spacing="4",
            ),
            spacing="5",
            justify="center",
            min_height="80vh",
        ),
    )


app = rx.App()
app.add_page(index)


app = rx.App()
app.add_page(index)
