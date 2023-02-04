#!/bin/bash
#1. Creamos el usuario y grupo de sistema 'odoo':
sudo adduser --system --quiet --shell=/bin/bash --home=/opt/odoo --gecos 'odoo' --group odoo
#2. Creamos en directorio en donde se almacenará el archivo de configuración y log de odoo:
sudo mkdir /etc/odoo && sudo mkdir /var/log/odoo/
#3. Instalamos Postgres y librerías base del sistema:
sudo apt update && sudo apt install  postgresql postgresql-server-dev-14 git python3 python3-pip build-essential python3-dev  libldap2-dev  libsasl2-dev python3-setuptools libjpeg-dev nodejs npm -y
#4. Descargamos odoo version 15 desde git: 
sudo git clone --depth 1 --branch 15.0 https://github.com/odoo/odoo /opt/odoo/odoo
#5. Damos permiso al directorio que contiene los archivos de OdooERP  e instalamos las dependencias de python3:
sudo chown odoo:odoo /opt/odoo/ -R && sudo chown odoo:odoo /var/log/odoo/ -R && sudo rm /usr/lib/python3/dist-packages/_cffi_backend.cpython-310-x86_64-linux-gnu.so 
sudo pip3 install -r /opt/odoo/odoo/requirements.txt
#6. Descargamos dependencias e instalar wkhtmltopdf para generar PDF en odoo
sudo apt install fontconfig xfonts-base xfonts-75dpi -y
cd /tmp
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.jammy_amd64.deb && sudo dpkg -i wkhtmltox_0.12.6.1-2.jammy_amd64.deb
sudo ln -s /usr/local/bin/wkhtmltopdf /usr/bin/ && sudo ln -s /usr/local/bin/wkhtmltoimage /usr/bin/
#7. Creamos un usuario 'odoo' para la base de datos:
sudo su - postgres -c "createuser -s odoo"
#8. Creamos la configuracion de Odoo:
sudo su - odoo -c "/opt/odoo/odoo/odoo-bin --addons-path=/opt/odoo/odoo/addons -s --stop-after-init"
#9. Creamos el archivo de configuracion de odoo:
sudo mv /opt/odoo/odoo/debian/odoo.conf /etc/odoo/odoo.conf
#10. Agregamos los siguientes parámetros al archivo de configuración de odoo:
sudo sed -i "s,^\(logfile = \).*,\1"/var/log/odoo/odoo-server.log"," /etc/odoo/odoo.conf
#11. Creamos el archivo de inicio del servicio de Odoo:
sudo cp /opt/odoo/odoo/debian/odoo.service /etc/systemd/system/odoo.service && sudo chmod +x /etc/systemd/system/odoo.service
sudo ln -s /opt/odoo/odoo/odoo-bin /usr/bin/odoo
sudo systemctl enable odoo.service
# crear un usuario postgres root