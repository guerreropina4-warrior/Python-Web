"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
    count: int = 0

    @rx.event
    def incrementa(self):
        self.count += 1

    @rx.event
    def decrementa(self):
        self.count -= 1


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.button(
                "Decrement",
                color_scheme="ruby",
                on_click=State.decrementa,
            ),
            rx.heading(State.count, font_size="2em"),
            rx.button(
                "Increment",
                color_scheme="grass",
                on_click=State.incrementa,
            ),
            spacing="4",

        ),
    )


app = rx.App()
app.add_page(index)
