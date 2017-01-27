# The weather. Proyecto IV 16-17


[![Build Status](https://travis-ci.org/edugr87/proyecto-iv.svg?branch=master)](https://travis-ci.org/edugr87/proyecto-iv)

##Descripción del proyecto

En esta asignatura voy a aprovechar para avanzar en la formacion con Python y Django. Voy a hacer una aplicacion web donde se pretende mostrar informacion sobre el tiempo en un determinado sitio.
Como proveedor de informacion meteorologica se usara openweathermap, en concreto usaremos su API para hacer consultas sobre el tiempo.


##Infraestructura

En este caso se va a usar el lenguaje Python y se usara con un framework Django que sigue el diseño Modelo, Vista, Template.
Como base de datos se usará sqlite3 que es la que se usa por defecto en Django.

##openweathermap

Un ejemplo de consulta a la api de openweathermap:
* http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=b1b15e88fa797225412429c1c50c122a1

##integración continua
[![Build Status](https://travis-ci.org/edugr87/proyecto-iv.svg?branch=master)](https://travis-ci.org/edugr87/proyecto-iv)

[Enlace a mi proyecto](https://github.com/edugr87/proyecto-iv/blob/master/.travis.yml)
El sistema de integración continua comprueba de forma continua que cada cambio realizado al repositorio, siga funcionando correctamente.

Travis permite testear el código del proyecto. Para llevar a cabo esto hay que adjuntar en el directorio raíz de nuestro proyecto el fichero [GitHub](https://github.com/edugr87/proyecto-iv/blob/master/.travis.yml) .travis.yml

##Makefile

Se ha creado un archivo Makefile para automatizar la creacion de proyecto. [GitHub](https://github.com/edugr87/proyecto-iv/blob/master/Makefile) Makefile

##Travis

He creado mi archivo travis.yml, igual que antes registrado con github previamente. Dejo unas imagenes donde comprobamos que todo el proceso se ha realizado con exito:


![Imagen travis](/iv-img/captura2.png)

##Despliegue en un PaaS.

Se ha realizado el despliegue de la aplicación en Heroku. Se porporciona un script con el que automatizamos el despliegue en Heroku tras clonar el proyecto.

![Imagen Heroku](/iv-img/captura6.png)
![Imagen de la aplicacion online](/iv-img/captura4.png)
