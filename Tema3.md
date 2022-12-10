# Configuración inicial de Odoo

Una vez instalado odoo, podemos comprobar que todo ha ido bien si con el servicio arrancado desde la máquina que actúa como servidor, intentamos acceder desde un navegador de la red a la dirección IP_SERVIDOR:8069. Además de esta comprobación podremos hacer la comprobacion del servicio que soporta odoo

```bash
systemctl status odoo.service
```

Otra cosa importante antes de continuar es el tema de los archivos de configuración. Tenemos que tener muy claro los siguientes:

- /etc/odoo.conf: archivo de configuración donde se ubican los parámetros de la configuración, como por ejemplo base de datos de la que se tira, usuario y contraseña con permisos, etc..
- /etc/systemd/system/odoo.service: archivo que contiene la configuración del servicio que soporta la ejecución del ERP

Una vez entendido esto podemos empezar con la configuración básica. Desde el navegador, introduciremos el nombre del usuario, contraseña, base de datos, idioma y demás información que se nos pode. Con esto la base de datos quedará creada. Es posible llenarla con datos de prueba si así se le indica. Una cosa muy importante es la contraseña del database master que se indica, ya que será la necesaria para poder gestionar las bases de datos si se desea.

Una vez creada la base de datos podremos acceder al sistema bien con el usuario que acabamos de crear (el correo indicado) o bien con el usuario administrador que viene por defecto (admin / admin) en el caso de haber seleccionado datos de prueba. 

Antes de entrar y configurar el ERP vamos a comentar un par de consideraciones

## Seleccionar la base de datos con la que se quiere trabajar

Con el asistente seguido en el punto anterior, se ha creado una base de datos dentro del servidor (que ahora comentaremos). Pero en algunos casos es posible querer tener dos bases de datos para por ejemplo hacer entornos de prueba. En este caso será necesario crearla desde la opción de gestión de bases de datos. Desde aquí se podrá:

- crear una nueva base de datos (iniciando el asistente primero)
- realizar un backup de una base de datos
- borrar una base de datos

En el momento que tengamos más de una base de datos, en el momento de iniciar sesión podremos seleccionar cual de ellas queremos utilizar. 

Este proceso se puede hacer manual (como acabamos de ver) o se puede hacer por comandos. Para ello lo primero que debemos hacer es crear la base de datos (ojo que hay que estar logeado con el usuario con permisos postgresql que se creó en el tema anterior) ejecutando el comando

```bash
createdb nombreNuevo
```

Una vez hecho esto es necesario inicializarla con todas las tablas necesarias, para lo cual se ejecuta el siguiente comando

```bash
/opt/odoo/odoo/odoo-bin -d nombreNuevo
```

Este comando inicializa el esquema de la base de datos y además asígna la base de datos como base de datos por defecto de odoo. 

Para poder comprobar que el proceso ha funcionado (tanto si se ha hecho de forma manual o si se ha hecho mediante comandos) podemos conectarnos a la consola de postgres y evaluar. Para ello seguiremos los siguientes pasos:

1. Dar permisos de acceso a IPs diferentes a la 127.0.0.1 (esto no es obligatorio). Para poder hacer esto editaremos el fichero main ubicado en la siguiente ruta: /etc/postgresql/14/main . Cuidado que el 14 puede diferir dependiendo de la version de postgresql que tengamos instalada. En parte donde indica que direcciones se deben escuchas, modificaremos el 127.0.0.1 por *

```bash
listen_addresses = '*'
```
2. Modificaremos el archivo de peticiones entrantes ubicado en /etc/postgresql/14/pg_hba.conf para que admita peticiones entrantes desde cualquier IP. Para ello en la parte de IPv4 podremos lo siguiente:

psql -h 192.168.4.6 -d odoo -U odoo -W

```bash
host    all             all             0.0.0.0/0
```

3. Por último será necesario resetear el servico para que se apliquen todos los cambios realizados

```bash
sudo service postgresql restart
```

Con todos estos pasos hechos, podremos conectarnos a la consla de postresql mediante el siguiente comando

```bash
psql -h 192.168.4.6 -d odoo -U odoo -W
```

Donde -d es la base de datos a la que nos queremos conectar
Donde -U es el usuario con el que nos conectamos

En el caso de no quererse conectar a ninguna base de datos simplemente tendremos que poner el comando 

```bash
psql -h 192.168.4.6
```
Una vez en la consola pueden ser útiles los siguientes comandos:
- \q para salir de la conexión
- \l lista todas las bases de datos
- \connect nombreBD conecta con la base de datos seleccionada
- \dt una vez conectado a una base de datos muestra todas las tablas de dicha base de datos. Una vez dentro, se pueden hacer consultas sobre las tablas. Por ejemplo para poder ver todos los usuarios del sistema actual podemos ejecutar la query

```sql
SELECT * FROM res_users;
```

## Acceso al servidor de forma remota. 

Para poder acceder de forma remota al servidor se puede hacer de dos formas

- Gráficamente: Lo podremos hacer desde cualquier cliente ligero, simplemente indicando los parámetros de configuracion del servidor. Clientes como UltraVNC, RealVNC o Chicken of the VNC son suficientes
- Por consola: Para poder acceder por consola el método más aceptado es ssh. En el caso de conectar desde un linux o un mac lo podremos hacer directamente desde consola instalando los paquetes necesarios. En el caso de hacerlo desde un windows tendremos que descargar un cliente como por ejemplo putty

Para poder utilizar shh en linux es necesario instalar el paquete openssh-server en la máquina destino, en nuestro caso el servidor de odoo donde están instaladas las cosas.

```bash
apt get install openssh-server
```

Una vez hecho esto y con el servicio activo, bastaría con ir a cualquier cliente y acceder con el siguiente comando:

```bash
ssh usuario@direccion_ip
```

La primera vez que conecta pide la verificación de confianza (fingerprint) de forma que la siguiente vez que conecta no sería necesaria está verificación


# Primeros pasos

Todo ERP basa su funcionalidad en los módulos, que no es más que un conjunto software que realiza una funcionalidad concreta con los datos que tiene el ERP. Principalmente existen dos tipos de módulos
- Adicionales: aquellos que se pueden instalar tras la puesta en marcha del sistema
- Bases: aquellos que vienen instalados de base y sin los cuales no funcionaría el sistema. Entre estos podemos diferenciar dos: empresas y administración (el cual permite añadir nuevos módulos adicionales)

Para poder instalar módulos, es tan sencillo como seleccionar el módulo que queremos instalar y seleccionarlo. Una vez hecho esto, podremos comprobar que el módulo aparece dentro de las opciones del sistema. En el caso de querer ver donde se ubica en el servidor, tendríamos que ir a la ruta donde se guardan todos los elementos del sistema

```bash
cat /opt/odoo/odoo/addons
```