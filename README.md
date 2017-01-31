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


##Despliegue en IaaS : AWS

En este apartado se va a desplegar la aplicacion automaticamente en amazon AWS. Para ello usamos Ansible y vagrant. Estas dos aplicaciones nos van a hacer que todo este despliegue se haga automatico una vez que las configuremos correctamente.

instalamos ansile

```sudo pip install ansible```

Este es su archivo ansile.yml:

```

- hosts: all
  sudo: true
  tasks:
  - name: Actualizar cache
    apt: update_cache=yes
  - name: Actualizamos repos.
    shell: sudo apt-get update && sudo apt-get upgrade -y
  - name: Instalar python-setuptools
    apt: name=python-setuptools state=present
  - name: Instalar build-essential
    apt: name=build-essential state=present
  - name: Instalar pip
    apt: name=python-pip state=present
  - name: Instalar git
    apt: name=git state=present
  - name: Ins Pyp
    apt: pkg=python-pip state=present
  - name: Instalar python-dev
    apt: pkg=python-dev state=present
  - name: Obtener aplicacion de git
    git: repo=https://github.com/edugr87/proyecto-iv.git  dest=TheWeather clone=yes force=yes
  - name: Permisos de ejecucion
    command: chmod -R +x TheWeather
  - name: Instalar requisitos
    command: sudo pip install -r TheWeather/requirements.txt
  - name: ejecutar
    command: nohup sudo python TheWeather/manage.py runserver 0.0.0.0:80

```

archivo ansile.cfg

```

[defaults]

private_key_file=/eduardo.pem

[ssh_connection]
control_path = %(directory)s/ssh-%%C
```

El siguiente paso es la instalacion de [vagrant](https://www.vagrantup.com), para instalarlo buscamos en su web oficial.
Es necesario instalar el plugin aws:
```vagrant plugin install vagrant-aws```

Ahora creamos un [vagrantfile](/Vagrantfile)

```
#-*- mode: ruby -*-
#vi: set ft=ruby :


Vagrant.configure('2') do |config|
    config.vm.box = "dummy"
    config.vm.box_url = "https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box"


    config.vm.provider :aws do |aws, override|
        aws.access_key_id = 'access_key_id'
        aws.secret_access_key = 'secret_access_key'
        aws.keypair_name = 'eduardo'
        aws.ami = "ami-01f05461"
        aws.region = "us-west-2"
        aws.security_groups = ['cc']
        aws.instance_type = "t2.micro"
        override.ssh.username = "ubuntu"
        override.ssh.private_key_path = "archivo.pem"
    end

    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "ansible.yml"
  end
end
```

ejecutamos la orden:
```
vagrant up -provider=aws
```

![Imagen resultado vagrant](/iv-img/resultadovagrant1.png)

![Imagen resultado vagrant](/iv-img/resultadovagrant0.png)

Al final despues de un resultado correcto,tenemos una instancia creada con el despliegue:

![Imagen resultado vagrant](/iv-img/instancia.png)

y ponemos ver nuestra app desplegada en [web](http://ec2-35-164-82-197.us-west-2.compute.amazonaws.com/index/)

![Imagen resultado vagrant](/iv-img/appinamazon.png)
