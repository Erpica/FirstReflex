import reflex as rx

config = rx.Config(
    app_name="FirstReflex",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)