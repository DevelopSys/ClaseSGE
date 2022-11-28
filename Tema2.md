# ERPs libres

El mercado de los ERPs se puede diferenciar entre los ERPs libres (aquellos que cuya licencia no es propietaria y no requiere de un pago) y los propietarios de pago. Nosotros nos vamos a centrar en los ERP libres, y en concreto en Odoo. Antes de empezar a ver cuales son las características de este ERP es importante recalcar las principales características de un software libre
-  Es gratuito, por lo que los constes de implantación se reducen bastante
-  No requiere de pago por mantenimiento, por lo que el trabajo lo realiza o bien el administrador/es de la empresa o una empresa que sea contratada.
-  Cuenta con una comunidad por detrás que dá mucho "soporte" gratuito, ya que hay gran cantidad de documentación que puede servir
-  Al ser libre y tener un código abierto, los desarrolladores pueden crear sus extensiones y publicarlas para que estas sean utilizadas por el resto de la gente


## Proceso de instalación

Como todo proyecto software, implantar un ERP no es un proceso sencillo y requiere de una serie de pasos que son necesarios. No se trata de instalar y configurar un ERP, sino que es necesario ver las necesidades, disponibilidades, infraestructuras, situación actual de la empresa donde se quiera implantar, etc... ya que de no hacer todos estos pasos se puede llegar al no existo de la implantación. Como veremos ahora, dentro de estos pasos no solo tenemos que tener en cuenta elementos, que por supuesto al tratarse de la implantación de un software, sino que también tendremos quq tener en cuenta elementos psicológicos y sociales ya que se está implantando un software para que lo utilicen las personas, y si estas no aceptan el cambio, por mucho que el software sea bueno el proceso se viene abajo. Por ello antes de implantar el sistema es necesario realizar los siguientes pasos: 

1. Análisis de necesidades y requisitos: No es lo mismo implantar un ERP para una empresa pequeña con 10 empleados que para una empresa que tiene 100 empleados. Antes de seleccionar el erp y el tipo de instalación es obligatorio hacer un análisis de mercado con los que existen, sus características y una vez evaluados todos, decidir cual es el que mejor se acopla a las necesidades de la empresa
2. Diseño de la instalación: Cuando se ha decidido el sistema que se va a instalar, es necesario diseñar cuales son los datos que se van a incluir, como se van a mapear, que informes se querrán incluir dentro del sistema, etc...
3. Instalación de equipos: Dependiendo de cual sea el ERP seleccionado y el tipo de instalación seleccionada, será necesaria una actualización de HW para que pueda soportar la carga del sistema que se va a implementar. Más adelante veremos los diferentes tipos de instalaciones, pudiendo encontrarnos en algunos casos que no necesitamos una instalación local como tal ya que se accede remotamente a través de la nube, por lo que en este caso no necesitaríamos una actualización de equipos
4. Adaptar y configurar el programa: Cada empresa es un mundo, por lo que una vez instalado el software será necesita una configuración inicial para que este pueda cubrir todos los requisitos necesarios para la empresa para la que se está desplegando
5. Migración de datos: Uno de los puntos críticos del proceso, ya que si con algo hace un erp es la administración de la empresa y esto solo se puede hacer con datos. En el caso de que estemos migrando de un sistema analógico a un sistema digital, este paso puede ser bastante tedioso ya que será necesario recopilar datos de muy diferentes fuentes. En el caso de estar haciendo una migración de sistema este proceso será algo más liviano ya que todos los sistemas por regla general trabajan con estándares
6. Pruebas: Una vez se han completados todos los pasos anteriores, antes de poner el sistema en producción es necesario realizar pruebas de funcionamiento para poder asegurar la calidad del producto. Las pruebas pueden ser de muy diferentes tipos: funcionalidad, rendimiento, integración, seguridad, etc...
7. Documentación: En realidad este es un paso transversal, es decir que pertenece a todo el proceso de implantación. La documentación es la generación de informes, manuales, ayudas, etc... que ayuda tanto al usuario final como al usuario administrador del sistema a comprender como funciona el sistema y en el caso de necesitar una administración profunda como poder hacerlo. La documentación es uno de los pasos básicos en el desarrollo software, ya que por ejemplo sin ella estaríamos muy perdidos ante un sistema que no hemos hecho nosotros
8. Formación: Último paso antes de la puesta en producción. Al principio se ha comentado que en el proceso de implantación no solo se van a tratar aspectos tecnológicos, sino que también se tratan aspectos psicológicos. En este caso es muy importante dar una buena formación a las personas que van a utilizar el sistema ya que si un usuario no sabe utilizar un sistema al fin y al cabo es como no tener nada, y más aún es posible que muchas de las funcionalidades las haga más y esto redunde en los datos de la empresa. Normalmente en los ERP se suelen diferenciar dos tipos de formaciones: una para los responsables del proyecto donde se les forma en como configurar el sistema, parametrizar, extractar datos, configurar informes nativos, etc... y otra formación para los usuarios finales donde se les indica como realizar su trabajo diario, más centrado en la parte del fronend

## Tipo de instalación

A grandes rasgos nos podemos encontrar con los siguientes tipos de instalación 

1. Mediante máquina: instalación basada en un servidor desde el cual se presta servicio a todos los clientes que solicitan acceso al servicio a traves de TCP/IP. Se trata de la arquitectura cliente-servidor por excelencia. En el caso de querer hacer un servicio de prueba para poder evaluar el software, se puede hacer esta infraestructura en una máquina virtual para no tener que desempeñar una máquina local completa para este cometido
2. Instalación mediante entrono gráfico: mediante un asistente de instalación se instala el software de la manera tradicional. Mediante esta opción se pueden configurar los programas y/o módulos que queremos que tenga instalado el sistema desde un inicio
3. Acceso al servicio desde la nube: en este caso no necesitaremos de ningún hardware adicional sino que lo haremos todo con acceso a servicios que una tercera empres nos brindará. Estos servicios pueden ser de tres grandes formas
   1. IaaS: infraestructura como servicio. En este caso el servicio web que se nos ofrece es un servicio de hardware a cambio de una cuota que representaría un alquiler. Los ejemplos más claros de este tipo de servicios son AWS y Azure
   2. PasS: plataforma como servicio. A diferencia del caso anterior, con este tipo de servicios la empresa que se contrata da acceso a una plataforma sobre la cual se puede crear aplicaciones o elementos directamente en la nube. Es totalmente diferente a la anterior, ya que antes simplemente nos daban acceso a la máquina. El ejemplo más claro de este tipo de servicios es google app engine
   3. SaaS. software como servicio. Este es el caso de los ERP online. Aquí, las empresas nos dan la posibilidad de acceder a un software para poder ejecutar sus funcionalidades sin necesidad de tener nada instalado en local. 

# Odoo

Odoo en la actualidad cuenta con dos versiones: 

- Community: Se trata de la versión limitada, ya que no cuenta con todas las características como por ejemplo soporte, actualizaciones, SaaS, así como la personalización de alguno de los módulos que se pueden instalar
- Enterprise: Aquella que cuenta con todas las características del software. Tiene un coste adicional y es facturado por usuarios / mes. Vá desde los 12 € hasta los 18€ en el caso de querer una instalación personalizada con conexiónAPI

Las características completas de cada una de las versiones las podemos encontrar aquí: https://www.odoo.com/es_ES/page/editions

## Instalación

Para poder realizar la instalación se va a realizar mediante máquina virtual sobre un sistema ubuntu server. En el caso de querer hacer la instalacion mediante paquete gráfico tendremos que descargarlos desde el siguiente link

https://www.odoo.com/es_ES/page/download

Antes de empezar la instalación, algunas de las cosas que se deben cumplir son las siguientes: 

- Que contemos con una segunda máquina con acceso a traves de la red para poder acceder al servidor a través de navegador
- Que la dirección IP de la máquina servidor cuente con uns IP fija o un nombre DNS reconocible para poder acceder a ella sin problema. En el caso de hacerlo en un entorno de pruebas podemos dejar el adaptador de red de forma automática con conexión con el host, siempre teniendo en cuenta que nos tendremos que asegurar en todo momento que la dirección IP a la que accedemos es la válida

Una vez creada la máquina virtual los pasos serán los siguienteS: 

1. Crear un usuario de sistema llamado odoo con el home localizado en /opt/odoo y las shell /bin/bash

2. Instalación de los servicios de postgre

```shell
sudo apt-get install postgresql postgresql-server-dev-14 postfregre
```
Logearse con el usuario creado por el servicio

```shell
su postgres
```

Crear un usuario en la base de datos 

```shell
createuser --createdb --pwprompt odoo
```

3. Logeados con el usuario creado en el punto 1, es necesaria la descarga del software. Actualmente está en producción la versión 16 (lanzada en octubre 22). En este caso y al ser una versión tan reciente optaremos por instalar la versión justo anterior

```shell
cd /opt/odoo
git clone https://www.github.com/odoo/odoo --depth 1 --branch 15.0 --single-branch
```

4. Instalación de las librerías necesarias

```shell
sudo apt-get install build-essential python3-pillow python3-lxml python3-dev python3-pip python3-setuptools libpq-dev npm nodejs git gdebi libldap2-dev libsasl2-dev libxml2-dev libxslt1-dev libjpeg-dev apache2 -y
```

5. Instalación de dependencias pip3 (sistema de gestor de paquetes de python)

```shell
pip3 install --upgrade pip
sudo pip3 install -r /opt/odoo/odoo/requirements.txt
```

6. Una vez descargados todos los elementos necesarios, se arranca el servidor odoo para comprobar que todos los elementos funcionan correctamente. Para ello, y situados en la ruta /opt/odoo/odoo/ se ejecuta el binario odoo-bin

```shell
./odoo-bin
```

Con la ejecución se mostrará que los servicios están corriendo. Sin embargo salta un aviso que falta por instalar un paquete que es el wkhtmltopdf el cual permite imprimir los informes gestionados dentro de la web. En el caso que además del paquete comentado, el comando indicase que falta algún módulo, será necesario instalarlo meddiante el siguiente comando

```shell
sudo pip3 install nombre_libreria
```

8. Antes de la instalación del paquete que falta, es recomendable actualizar los paquetes del sistema. Una vez hecho esto, se procede a la instalación del mismo. Para ello es necesesario agregar algún repositorio extra que tienen dependencias de seguridad que el paquete de pdf utiliza

```shell
sudo apt-get install -y software-properties-common
sudo apt-add-repository -y "deb http://security.ubuntu.com/ubuntu focal-security main"
sudo apt-get -yq update
```

Con el repositorio agregado al sistema (y un update - upggrade), se procede a descargar e instalar el servicio de pdf.

```shell
wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb 
// tras descarga
sudo gdebi -n wkhtmltox_0.12.5-1.bionic_amd64.deb 
```

Por último, para que los binarios estén disponibles para cualquier usuario desde cualquier perfil, se realiza un enlace de los binarios

```shell
sudo ln -s /usr/local/bin/wkhtmltopdf /usr/bin/ 
sudo ln -s /usr/local/bin/wkhtmltoimage /usr/bin/
```

Con estas instalaciones odoo ya está preparado para trabajar. Antes de arrancarlo y configurar el servicio de arranque automático, se crean una carpeta dentro de /var/log/ llamada odoo donde se guardarán los registros del sistema. Es importante que esta carpeta tenga los permisos bien configurados para que el usuario owner sea el usuario odoo

```shell
mkdir /var/log/odoo/
chown odoo:root /var/log/odoo
```

9. El siguiente paso es realizar una copia del fichero de configuración para que el sistema sepa cuales son los elementos de los que consta el servicio.Para ello se realiza una copia del fichero odoo.conf en la ruta del los archivos de configuración. Además es necesario darle la propiedad al usuario odoo y poner una máscara de 640

```shell
cp /opt/odoo/odoo/debian/odoo.conf  /etc/odoo.conf
chown odoo: /etc/odoo.conf
chmod 640 /etc/odoo.conf
```

10. Con el fichero de configuración creado, será necesario verificar su contenido, abriendolo con el editor de texto que queramos

```shell
db_user = odoo
db_password = odoo
addons_path = /opt/odoo/odoo/addons
logfile = /var/log/odoo/odoo-server.log
```

11. Por último queda la configuración del servicio para que este se arranque automáticamente cuando se inicia el servicio. Para ello es necesario copiar el servicio de la carpeta clonada y dejarlo en la ruta de los servicios de ubuntu

```shell
sudo cp /opt/odoo/odoo/debian/odoo.service /etc/systemd/system/odoo.service
```

Una vez copiado es necesario modificar algunos elementos del servicio. Para ello abrimos el fichero copiado con editor de texto

```shell
[Service]
Type= simple
User=odoo
Group= odoo
ExecStart=/opt/odoo/odoo/odoo-bin --config /etc/odoo.conf 
```

Es muy importante que el el atributo de ExecStart se ponga la ruta del binario de odoo y en el de config la ruta del fichero de configuración que se ha copiado en pasos anteriores

12. Con todo esto hecho el servicio ya está completo y lo único que haría falta es activarlo mediante systemctl.

```shell
sudo systemctl enable odoo.service
```

Con el servicio activado y mediante systemctl podemos parar, arrancar, reiniciar y consultar el status del servicio.

13. Para acceder a odoo, desde un navegador dentro de la red del servidor ponemos la dirección https://IP_SERVIDOR:8069