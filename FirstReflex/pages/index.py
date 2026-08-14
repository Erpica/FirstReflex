import reflex as rx

from ..components.layout import layout


def index() -> rx.Component:
    return layout(
        rx.center(
            rx.vstack(
                # Etiqueta superior
                rx.badge(
                    "PYTHON + REFLEX",
                    color_scheme="blue",
                    variant="soft",
                    size="2",
                ),

                # Título principal
                rx.heading(
                    "Construye aplicaciones web",
                    rx.text.span(
                        " con Python",
                        color="blue.500",
                    ),
                    size="9",
                    weight="bold",
                    text_align="center",
                ),

                # Subtítulo
                rx.text(
                    "Una aplicación moderna, construida desde cero "
                    "mientras aprendo Reflex.",
                    size="5",
                    color="gray.600",
                    text_align="center",
                    max_width="650px",
                ),

                # Botones
                rx.hstack(
                    rx.link(
                        rx.button(
                            "Ir al formulario",
                            size="3",
                        ),
                        href="/formulario",
                    ),

                    rx.link(
                        rx.button(
                            "Ver documentación",
                            size="3",
                            variant="outline",
                        ),
                        href="#",
                        is_external=False,
                    ),

                    spacing="4",
                ),

                # Tarjetas
                rx.grid(
                    rx.card(
                        rx.vstack(
                            rx.heading(
                                "🐍 Python",
                                size="4",
                            ),
                            rx.text(
                                "Toda la lógica de la aplicación "
                                "se desarrolla con Python.",
                                size="3",
                                color="gray.600",
                            ),
                        ),
                        padding="1.5em",
                    ),

                    rx.card(
                        rx.vstack(
                            rx.heading(
                                "⚡ Reflex",
                                size="4",
                            ),
                            rx.text(
                                "Construcción de interfaces web "
                                "sin necesidad de escribir React.",
                                size="3",
                                color="gray.600",
                            ),
                        ),
                        padding="1.5em",
                    ),

                    rx.card(
                        rx.vstack(
                            rx.heading(
                                "🗄️ Base de datos",
                                size="4",
                            ),
                            rx.text(
                                "El proyecto evolucionará hasta "
                                "incorporar persistencia de datos.",
                                size="3",
                                color="gray.600",
                            ),
                        ),
                        padding="1.5em",
                    ),

                    columns="3",
                    spacing="4",
                    width="100%",
                    max_width="1000px",
                ),

                spacing="7",
                align="center",
                width="100%",
            ),

            width="100%",
            padding="4em 2em",
        )
    )