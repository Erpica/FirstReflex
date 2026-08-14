import reflex as rx

from .pages.index import index
from .pages.formulario import formulario


app = rx.App()

app.add_page(index)
app.add_page(formulario, route="/formulario")
