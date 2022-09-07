# Mini analizador sintáctico

Este proyecto fue realizado en el lenguage de programación Python, utilizando la versión 3.10 y empleando el entorno de Visual Studio Code para su desarrollo. No obstante, se trabajó a modo de consola e interfaz(utilizando la librería de Pyside2 del entorno QT), realizando esta compactación hibrida para un mejor manejo de la información procesada.

## Instalación
#### 1ra forma. 
Dar clic en Code, luego en Donwload ZIP y después de que termine la descarga, descomprimirlo.
#### 2da forma. 
Crear una carpeta, ingresar a git bash y ejecutar el siguiente comando:
https://github.com/OTG-16/Mini_analizador_sintactico.git
###Nota
Es importante resaltar que en este proyecto se utilizan herramientas que deben ser instaladas previamente para el correcto funcionamiento de este analizador. Entre ellas están las siguientes:
- IDE QT Creator
- Librería Pyside2 (Se podría consultar el siguiente video para su instalación https://www.youtube.com/watch?v=INSimE1tW34&list=PLNN_J-C1-lZvgVgnoYXeZo49Boz6CDGTf&index=4 y este otro como introducción para su manejo https://www.youtube.com/watch?v=T0qJdF1fMqo&list=PLNN_J-C1-lZvgVgnoYXeZo49Boz6CDGTf&index=5&t=1533s)
- Librería Colorama (Utlizar en el cmd el comando: pip install colorama)
## Probando el programa
En un principio, al momento de correr el programa este muestra lo siguiente:

Puede apreciarse una interfaz. Al lado izquierdo se cuenta con un cuadro de texto (ignorar el de la derecha) para ingresar la información a analizar. En la parte de a medias se tiene un botón, este se usa para comenzar con el análisis tanto léxico como sintáctico.
Ahora bien, se ingresa en el cuadro correspondiente, el texto "hola+mundo" y se da click en el botno de analizar. Al ser una cadena válida el programa muestra una ventana con el mensaje de "cadena aceptada!" y despliega la siguiente información:

Ahí se puede ver en la parte de la interfaz tanto el texto ingresado como el resultado del análisis léxico y en la de la consola se despliega la tabla LR(1) y más abajo su respectivo análisis sintáctico.

No obstante, como se pidió en la tarea, de forma más específica en el ejercicio 1. Se ingresa la cadena "a+b" para su respectivo análisis. Como también es una cadena válida se muestra la ventana con el mensaje de "cadena aceptada!" y también la siguiente información de interfaz y consola tal y como en la corrida anterior pero con sus datos específicos de la cadena analizada.

