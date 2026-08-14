import reflex as rx

from .navbar import navbar
from .footer import footer


def layout(content: rx.Component) -> rx.Component:
    return rx.vstack(
        navbar(),

        rx.box(
            content,
            flex="1",
            width="100%",
        ),

        footer(),

        width="100%",
        min_height="100vh",
    )