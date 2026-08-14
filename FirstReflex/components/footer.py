import reflex as rx


def footer() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text(
                "© 2026 FirstReflex",
                size="2",
            ),

            rx.spacer(),

            rx.hstack(
                rx.link(
                    "Inicio",
                    href="/",
                ),
                rx.link(
                    "Formulario",
                    href="/formulario",
                ),
                spacing="4",
            ),

            width="100%",
            max_width="1200px",
            margin="0 auto",
            padding="1em",
        ),
        width="100%",
        border_top="1px solid var(--gray-5)",
    )