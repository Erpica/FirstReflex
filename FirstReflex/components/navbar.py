import reflex as rx


def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            "Inicio",
            href="/",
        ),
        rx.link(
            "Formulario",
            href="/formulario",
        ),
        rx.spacer(),
        rx.color_mode.button(),
        width="100%",
        padding="1em",
    )