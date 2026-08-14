import reflex as rx

from ..components.layout import layout
from ..state.formulario import FormState


def formulario() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading(
                "Formulario de contacto",
                size="6",
            ),

            rx.input(
                placeholder="Nombre",
                value=FormState.nombre,
                on_change=FormState.set_nombre,
                width="100%",
            ),

            rx.input(
                placeholder="Email",
                type="email",
                value=FormState.email,
                on_change=FormState.set_email,
                width="100%",
            ),

            rx.text_area(
                placeholder="Mensaje",
                value=FormState.mensaje,
                on_change=FormState.set_mensaje,
                width="100%",
            ),

            rx.button(
                "Enviar",
                on_click=FormState.enviar_formulario,
                width="100%",
            ),

            spacing="4",
            width="100%",
            max_width="400px",
        )
    )