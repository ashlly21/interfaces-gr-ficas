import flet as ft
# Menú de la pastelería: (nombre, precio). Para agregar un postre, añade una línea.
MENU = [
    ("Cocada", 3500),
    ("Brownie", 5000),
    ("Torta de chocolate (porción)", 8000),
]

def formatear_pesos(valor):
    """Devuelve un número con formato de pesos, por ejemplo $12.000."""
    return f"${valor:,}".replace(",", ".")


class Postre:
    """Modelo de datos: guarda un postre y sabe calcular su subtotal.
    No conoce nada de la interfaz gráfica."""

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calcular_subtotal(self, cantidad):
        return self.precio * cantidad

@ft.control
class FilaPostre(ft.Row):
    """Control personalizado: una fila con el nombre del postre y su campo de cantidad.
    Se encarga de mostrar un postre y de leer la cantidad que escribe el usuario."""

    nombre: str = ""
    precio: int = 0

    def init(self):
        self.postre = Postre(self.nombre, self.precio)
        self.campo_cantidad = ft.TextField(label="Cantidad", value="0", width=120)
        self.controls = [
            ft.Text(f"{self.postre.nombre} ({formatear_pesos(self.postre.precio)})", width=280),
            self.campo_cantidad,
        ]

    def obtener_subtotal(self):
        """Lee la cantidad del campo y devuelve el subtotal.
        Lanza ValueError si el dato no es un entero mayor o igual a cero."""
        cantidad = int(self.campo_cantidad.value)
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        return self.postre.calcular_subtotal(cantidad)


@ft.control
class CalculadoraPedido(ft.Column):
    """Control personalizado principal: arma toda la pantalla,
    recibe el evento del botón y actualiza el total en la interfaz."""

    def init(self):
        self.filas = [FilaPostre(nombre=n, precio=p) for n, p in MENU]
        self.resultado = ft.Text("Total: $0", size=24, weight=ft.FontWeight.BOLD)
        self.mensaje = ft.Text("", color=ft.Colors.RED)
        self.controls = [
            ft.Text("Dulce Anochecer", size=30, weight=ft.FontWeight.BOLD),
            ft.Text("Escribe la cantidad de cada postre:"),
            *self.filas,
            ft.Button(content="Calcular total", on_click=self.calcular_total),
            self.resultado,
            self.mensaje,
        ]

    def calcular_total(self, e):
        """Evento: se ejecuta cuando el usuario presiona el botón."""
        try:
            total = sum(fila.obtener_subtotal() for fila in self.filas)
            self.mensaje.value = ""
            self.resultado.value = f"Total: {formatear_pesos(total)}"
        except ValueError:
            self.mensaje.value = "Escribe solo números enteros (0 o más)."
        self.page.update()

def main(page: ft.Page):
    page.title = "Calculadora de pedidos de postres"
    page.padding = 30
    page.window.width = 700
    page.window.height = 520
    page.add(CalculadoraPedido())

ft.run(main)