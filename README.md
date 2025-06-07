[documentación]: https://ni.srht.site/nxt-python/latest/
[tutorial]: https://ni.srht.site/nxt-python/latest/handbook/tutorial.html

###### 1.2 Instalación de la librería con PIP
```
python3 -m pip install --upgrade nxt-python 
//NXT-Python es un paquete para controlar un robot LEGO NXT utilizando el lenguaje de programación Python. Puede comunicarse mediante USB o Bluetooth.
```
###### 1.3 Librerías utilizadas
1.3.1 nxt: Es el paquete principal que permite la comunicación con el LEGO NXT.

1.3.2 nxt.locator: Se encarga de encontrar y conectar con el NXT (ya sea via USB o Bluetooth).

1.3.3 nxt.motor: Controla los motores del NXT.

1.3.4 sys: Interactúa con el sistema (en este caso, se usa para leer la entrada del teclado).

1.3.5 Para ejecutar las teclas pulsadas en tiempo real utilizamos las siguientes librerías:

1.3.5.1 tty: Configura el modo de la terminal para leer teclas sin esperar "Enter".

1.3.5.2 termios: Controla opciones avanzadas de la terminal (útil para leer inputs en tiempo real).
```
import nxt #1.3.1
import nxt.locator #1.3.2 
from nxt.motor import Motor #1.3.3
import sys #1.3.4
import tty #1.3.5.1
import termios #1.3.5.2
```
### 1.4 Resumen - Tabla de librerías

| Librería       | Función Principal                          |
|----------------|--------------------------------------------|
| `nxt`          | Comunicación con el LEGO NXT.              |
| `nxt.locator`  | Busca y conecta al NXT.                    |
| `nxt.motor`    | Controla los motores (velocidad/dirección).|
| `sys`          | Acceso a la entrada del teclado.           |
| `tty` + `termios` | Lectura de teclas en tiempo real.        |
