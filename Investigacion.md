# 2.Investigación
# Deberán responder las siguientes preguntas:
# 1.¿Qué es la biblioteca seleccionada y cuál es su propósito principal?

Flet es un framework de interfaces gráficas multiplataforma para Python. Permite a desarrolladores Python sin experiencia previa en Flutter (ni en front-end) construir aplicaciones con interfaz Flutter. Su propósito es crear interfaces modernas solo con Python, sin escribir HTML, CSS ni JavaScript.

# 2. ¿Qué tipo de aplicaciones permite desarrollar?

Está pensado para aplicaciones interactivas y multiusuario en web, escritorio y móvil, todo con Python. Sirve para contadores, formularios, listas de tareas, paneles de datos y herramientas internas.

# 3. Instalación y requisitos
  * Python: 3.10 o superior. 
  * flet
  * Sistema operativo: macOS 12 o posterior, Windows 10/11 de 64 bits y Linux. 
  * flet
  * Instalación: la documentación recomienda un entorno virtual. Se instala con pip install 'flet[all]'. 
  * flet
  * Verificación: se usa flet --version o flet doctor.

# 4. Componentes o elementos gráficos principales

En Flet todo es un control, y se agregan a una página (Page), que es la ventana o pestaña de la app. Los más comunes son:

  * Texto y entrada: Text, TextField.
  * Botones: Button, FilledButton, IconButton.
  * Organización (layout): Column, Row, Container.
  * Navegación y avisos: NavigationBar, AlertDialog.

El listado completo está en la sección Controls de la documentación oficial.

# 5. Manejo de eventos

Las acciones del usuario, como clics o escritura, disparan eventos, y todo manejador de eventos recibe un objeto Event. El patrón es: 

Escribes una función que procesa el evento.
La conectas al control mediante una propiedad como on_click o on_change.
El objeto del evento da acceso al control que lo originó (e.control) y a datos adicionales (e.data). 

Para el teclado hay un evento global: se implementa page.on_keyboard_event y el parámetro es un KeyboardEvent. Ese objeto indica la tecla (key) y si estaban presionadas Shift, Ctrl, Alt o Meta. 

# 6. Ventajas y limitaciones frente a Tkinter

Esta comparación sale de mi conocimiento general sobre ambas bibliotecas, no de una fuente puntual.

  # Ventajas

  - Apariencia moderna y consistente (Material Design) sin configuración extra.
  - La misma app puede correr en escritorio, web y móvil.
  - Estructura declarativa: controles anidados en Column o Row, más sencillo que pack, grid  o place.
  - Tiene recarga en vivo con flet run durante el desarrollo.

   # Limitaciones

  - Tkinter viene incluido con Python y Flet requiere instalación.
  - Flet es más joven y cambia rápido. Por ejemplo, la documentación actual usa ft.run(main), mientras que tutoriales antiguos usan ft.app(target=main). Revisa que lo que copies coincida con tu versión.
  - Tiene menos tutoriales y respuestas en foros que Tkinter.
  - Depende de Flutter por detrás, así que es más pesado que Tkinter.
  - Según un reporte de la comunidad en GitHub, el teclado se maneja con un único manejador a nivel de página, que recibe las teclas sin importar qué control tenga el foco

# Fuente consultada

  - Documentación oficial, instalación: https://docs.flet.dev/getting-started/installation
  - Documentación oficial, atajos de teclado: https://docs.flet.dev/cookbook/  keyboard-shortcuts
  - Documentación oficial, KeyboardEvent: https://docs.flet.dev/types/keyboardevent
  - Documentación oficial, Page: https://flet.dev/docs/controls/page
  - Reporte en GitHub sobre el teclado: https://github.com/flet-dev/flet/issues/6261
  - Sitio oficial de Flet: https://flet.dev

  # 4. Explicación del funcionamiento

  # 1. Cómo se crea la ventana principal

La ventana se crea con ft.run(main), al final del archivo. Flet abre una ventana de escritorio y llama a la función main, pasándole como parámetro un objeto page, que representa esa ventana. En el método construir_pantalla se configura con page.title (el título), page.padding (el margen interno) y page.window.width y page.window.height (el tamaño).

 # 2. Cómo se crean y muestran los componentes gráficos

En Flet cada elemento visual es un control. En construir_pantalla se crean los controles y se agregan a la ventana con page.add(...):

ft.Text para el título, las instrucciones, el total y el mensaje de error.
ft.TextField para el campo de cantidad de cada postre.
ft.Row para poner en la misma línea el nombre del postre con su campo de cantidad.
ft.Button para el botón “Calcular total”.

Los campos de cantidad se crean dentro de un ciclo for que recorre la lista de postres. Así, si se agrega un postre a la lista, aparece su fila automáticamente.

 # 3. Qué evento se implementó y cómo se detecta

El evento es el clic del usuario sobre el botón “Calcular total”. Se detecta con la propiedad on_click del botón, que se configura así: on_click=self.calcular_total. Esto le indica a Flet que, cada vez que el usuario haga clic en ese botón, debe ejecutar ese método.

 # 4. Qué método responde al evento

Responde el método calcular_total de la clase CalculadoraPedido. Hace lo siguiente:

  - Recorre los postres y lee la cantidad escrita en cada campo.
  - Convierte esa cantidad a número entero con int().
  - Multiplica cada cantidad por el precio del postre y suma todo en total.
  - Si el usuario escribió algo que no es un número entero mayor o igual a cero, captura el error con try/except y prepara un mensaje de aviso.

   # 5. Cómo se modifica la interfaz después de la interacción

Dentro de calcular_total se cambia la propiedad value de los textos:

  - Si todo está bien, self.resultado.value pasa a mostrar el total, por ejemplo “Total: $169.500”, y el mensaje de error se borra.
  
  - Si hay un dato inválido, self.mensaje.value muestra en rojo “Escribe solo números enteros (0 o más).”

Esos cambios no se ven hasta que se ejecuta self.page.update(), la última línea del método. Esa instrucción le pide a Flet que redibuje la ventana con los valores nuevos. Por eso la aplicación no solo se abre, sino que responde a una acción del usuario.

Si te piden la explicación más corta o con capturas, te la ajusto. Para el README te conviene incluir tu captura del total calculado y otra con el mensaje de error.