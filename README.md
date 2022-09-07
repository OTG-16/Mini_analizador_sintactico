# Mini analizador sintáctico

Este proyecto fue realizado en el lenguage de programación Python, utilizando la versión 3.10 y empleando el entorno de Visual Studio Code para su desarrollo. No obstante, se trabajó a modo de consola e interfaz (utilizando la librería de Pyside2 del entorno QT), realizando esta compactación hibrida para un mejor manejo de la información procesada.

## Instalación
#### 1ra forma. 
Dar clic en Code, luego en Donwload ZIP y después de que termine la descarga, descomprimirlo.
#### 2da forma. 
Crear una carpeta, ingresar a git bash y ejecutar el siguiente comando:
https://github.com/OTG-16/Mini_analizador_sintactico.git
### Nota
Es importante resaltar que en este proyecto se utilizan herramientas que deben ser instaladas previamente para el correcto funcionamiento de este analizador. Entre ellas están las siguientes:
- IDE QT Creator
- Librería Pyside2 (Se podría consultar el siguiente video para su instalación https://www.youtube.com/watch?v=INSimE1tW34&list=PLNN_J-C1-lZvgVgnoYXeZo49Boz6CDGTf&index=4 y este otro como introducción para su manejo https://www.youtube.com/watch?v=T0qJdF1fMqo&list=PLNN_J-C1-lZvgVgnoYXeZo49Boz6CDGTf&index=5&t=1533s)
- Librería Colorama (Utlizar en el cmd el comando: pip install colorama)
## Probando el programa
En un principio, al momento de correr el programa este muestra lo siguiente:
![s1](https://user-images.githubusercontent.com/70919055/188969450-78bd0a97-49ee-4e8a-8d33-5376481a6d55.png)

Puede apreciarse una interfaz. Al lado izquierdo se cuenta con un cuadro de texto (ignorar el de la derecha) para ingresar la información a analizar. En la parte de a medias se tiene un botón, este se usa para comenzar con el análisis tanto léxico como sintáctico.
Ahora bien, se ingresa en el cuadro correspondiente, el texto "hola+mundo" y se da click en el botón de analizar. Al ser una cadena válida el programa muestra una ventana con el mensaje de "cadena aceptada!" y despliega la siguiente información:
![s2](https://user-images.githubusercontent.com/70919055/188969285-368927d2-1332-41a4-82a1-5cc9ddca6431.png)

Ahí se puede ver en la parte de la interfaz tanto el texto ingresado como el resultado del análisis léxico y en la de la consola se despliega la tabla LR(1) y más abajo su respectivo análisis sintáctico.

No obstante, como se pidió en la tarea, de forma más específica en el ejercicio 1. Se ingresa la cadena "a+b" para su respectivo análisis. Como también es una cadena válida se muestra la ventana con el mensaje de "cadena aceptada!" y también la siguiente información de interfaz y consola tal y como en la corrida anterior pero con sus datos específicos de la cadena analizada.
![s3](https://user-images.githubusercontent.com/70919055/188969551-1d52a259-3694-45e6-833b-cec9d06760af.png)

Finalmente, como se pidió en la tarea, de forma más específica en el ejercicio 2. Se ingresa la cadena "a+b+c+d+e+f" para su respectivo análisis. Como también es una cadena válida se muestra la ventana con el mensaje de "cadena aceptada!" y también la siguiente información de interfaz y consola tal y como en las corridas anteriores (solo que en este caso son más capturas para presentar la info por que son más tokens los que se ingresan) ,pero con sus datos específicos de la cadena analizada.

Információn de la interfaz gráfica:
![s4](https://user-images.githubusercontent.com/70919055/188969621-3b903b95-a018-4114-877c-a91c20d32276.png)
![s5](https://user-images.githubusercontent.com/70919055/188969682-14026e72-d121-44c6-87c1-30da8febbe98.png)

Información de la consola:
![s6](https://user-images.githubusercontent.com/70919055/188969762-afc32274-36a1-4fb6-9e36-d96ce8c112d1.png)
