import flet as ft


class Postre:
    """Representa un postre con su nombre y precio."""

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class CalculadoraPedido:
    """Arma la pantalla y procesa el evento del botón."""

    def __init__(self, page: ft.Page, postres):
        self.page = page
        self.postres = postres
        self.campos = {}  # nombre del postre -> campo de cantidad
        self.resultado = ft.Text("Total: $0", size=24, weight=ft.FontWeight.BOLD)
        self.mensaje = ft.Text("", color=ft.Colors.RED)

    def construir_pantalla(self):
        """Crea los elementos visuales y los agrega a la página."""
        self.page.title = "Calculadora de pedidos de postres"
        self.page.padding = 30
        self.page.window.width = 700   # ancho de la ventana
        self.page.window.height = 520  # alto de la ventana

        self.page.add(ft.Text("Dulce Anochecer", size=30, weight=ft.FontWeight.BOLD))
        self.page.add(ft.Text("Escribe la cantidad de cada postre:"))

        for postre in self.postres:
            campo = ft.TextField(label="Cantidad", value="0", width=120)
            self.campos[postre.nombre] = campo
            self.page.add(
                ft.Row(
                    [
                        ft.Text(f"{postre.nombre} (${postre.precio:,})".replace(",", "."), width=280),
                        campo,
                    ]
                )
            )

        # El botón conecta el clic del usuario con el método calcular_total
        self.page.add(ft.Button(content="Calcular total", on_click=self.calcular_total))
        self.page.add(self.resultado)
        self.page.add(self.mensaje)

    def calcular_total(self, e):
        """Evento: se ejecuta cuando el usuario presiona el botón."""
        total = 0
        try:
            for postre in self.postres:
                cantidad = int(self.campos[postre.nombre].value)
                if cantidad < 0:
                    raise ValueError
                total += cantidad * postre.precio
            self.mensaje.value = ""
            self.resultado.value = f"Total: ${total:,}".replace(",", ".")
        except ValueError:
            self.mensaje.value = "Escribe solo números enteros (0 o más)."
        self.page.update()  # actualiza la pantalla con el resultado


def main(page: ft.Page):
    postres = [
        Postre("Cocada", 3500),
        Postre("Brownie", 5000),
        Postre("Torta de chocolate (porción)", 8000),
    ]
    app = CalculadoraPedido(page, postres)
    app.construir_pantalla()


ft.run(main)