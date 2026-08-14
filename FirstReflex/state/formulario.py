import reflex as rx


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
        print(
            f"Formulario enviado: "
            f"{self.nombre}, "
            f"{self.email}, "
            f"{self.mensaje}"
        )

        self.nombre = ""
        self.email = ""
        self.mensaje = ""