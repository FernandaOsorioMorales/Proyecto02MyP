## Proyecto02MyP
"Proyecto 2 para la materia de Modelado y Programación (Semestre 2023-1) FC-UNAM"

 ## Integrantes

    De la Rosa Hernández Carlos Joel
    319229185
    Domínguez Barrón Anshar Shamash Aarón
    420138170
    Osorio Morales Fernanda Ameyalli
    319092846

## Instalación de dependencias para correr el código
EL proyecto Identificador de Figuras Geométricas está desarrollado enteramente en python3, por lo que pedimos por favor instales primeramente python en tu entorno de trabajo, posteriormente, se ha utilizado la biblioteca OpenCV y PIL por lo que también será necesario su instalación, a continuación mostramos la forma de llevar a cabo dichos procedimientos tanto en Windows como en Linux.

### Windows
* Instala Python a través de la web oficial: https://www.python.org/downloads/ y continúa con las instrucciones del instalador.
* Instala pip para manejar las dependencias necesarias siguiendo https://www.geeksforgeeks.org/how-to-install-pip-on-windows/#:~:text=Step%201%3A%20Download%20the%20get,where%20the%20above%20file%20exists.&text=Step%204%3A%20Now%20wait%20through%20the%20installation%20process.
* Con pip instalado corre los siguientes comandos en shell: 
```
$pip install python-csv
```
```
$pip install opencv-python
```
```
$pip install Pillow
```

### Linux-based
* Instala python mediante tu administrador de paquetes (dnf, snap, etc) con el comando en terminal: 
```
$ sudo [package_manager] install python3.6
```
* Instala **pip** mediante tu administrador de paquetes (dnf, snap, etc) con el comando en terminal: 
```
$ sudo [package_manager] install python3-pip
```
* Con pip instalado corre los siguientes comandos en shell: 
```
$pip install python-csv
```
```
$pip install opencv-python
```
```
$pip install Pillow
```

## Cómo correr el proyecto
Por favor abre tu terminal y colócate en la carpeta del proyecto, añade las imágenes que quieras pasarle al programa a la carpeta "ImagenesEjemplos",posteriormente corre el siguiente código: 
```
$python3 Main.py
```
Una vez que haya compilado ingresa el path de tu imagen en la forma
```
ImagenesEjemplos/nombredetuimagen.bmp
```
Por ejemplo:
```
ImagenesEjemplos/example_1.bmp
```
## Cómo correr las pruebas
Antes que nada, para las pruebas se necesita la instalacion de la libreria unittest, por lo que si no lo tiene instalado debera hacerlo primero para la utilizacion de estas.
Para correr las pruebas posicionandonos en la carpeta del proyecto y daremos el siguiente comando:
```
python3 -m unittest test_lectura.py
```
enseguida tnedremos que poner el path de la imagen para prueba el cual puede ser cualquiera de las que se encuentran en la carpeta ImagenesEjemplos, por ejemplo:
```
/home/charly/Proyecto02MyP/ImagenesEjemplos/example_1.bmp
```
multiples veces, hasta que se termine de correr el programa, muestre el resultado de las pruebas y se cierre.

