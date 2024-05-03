# Pruebas automatizadas para Urban Routes con Selenium[]
- Necesitas tener instalados los paquetes de selenium, pytest y request para ejecutar las pruebas.
- Necesitas instalar el driver de Selenium, puedes encontrarlo en el siguiente enlace: https://googlechromelabs.github.io/chrome-for-testing/
- Abre la carpeta del proyecto en Pycharm.
- Para instalar Selenium abre la consola y ejecuta el comando: pip install selenium
- Para instalar Pytest abre la consola y ejecuta el comando: pip install -U pytest
- Una vez instalado Pytest, en la consola ejecuta el comando: pytest -s -o log_cli=true -log_cli_level=DEBUG
- Para el proyecto se siguio patron de diseño llamado POM, donde se crea la clase para la pagina, se definen los localizadores, los metodos y posteriormente se hace una clase para los test.
- Descripion:
En el proyecto se testean las principales funciones al pedir un taxi mediante la tarifa "Comfor", donde testeamos que los numeros de telefono y tarjeta sean los mismos que ingresamos, asi como la restriccion de cantidad de caracteres maxima en los comentarios, que esten funcionando los botones para agregar mantas y helados y por ultimo la funcion de pedir el taxi y que muestre la informacion del conductor. Esto se realizo dibidiendo las clases y los metodos en distintas paginas, donde una pagina tiene el metodo especifico para recibir el codigo del celular, otra pagina tiene los metodos y localizadores para las funciones de la pagina, mientras que en la ultima contiene el codigo para realizar las pruebas. 
- Comprueba las pruebas que fallaron. 
- Jorge Caceres - Corte 8 - Sprint 7