"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config


class State(rx.State):
    """The app state."""


class FormState(rx.State):
    nombre: str = ""
    email: str = ""
    mensaje: str = ""

    def set_nombre(self, value: str):
        self.nombre = value

    def set_email(self, value: str):
        self.email = value

    def set_mensaje(self, value: str):
        self.mensaje = value

    def enviar_formulario(self):
        print(f"Formulario enviado: {self.nombre}, {self.email}, {self.mensaje}")
        self.nombre = ""
        self.email = ""
        self.mensaje = ""


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Mi primera aplicación con Reflex!", size="9"),
            rx.text(
                rx.code(f"Archivo principal: {config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )


def formulario() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Formulario de contacto", size="6"),
            rx.input(
                placeholder="Nombre",
                value=FormState.nombre,
                on_change=FormState.set_nombre,
                width="100%",
            ),
            rx.input(
                placeholder="Email",
                type="email",  # Corregido: type="email"
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
            rx.button("Enviar", on_click=FormState.enviar_formulario, width="100%"),
            width="100%",
            max_width="400px",
            spacing="4",
        ),
        min_height="85vh",
    )


app = rx.App()
app.add_page(index)
app.add_page(formulario, route="/formulario")