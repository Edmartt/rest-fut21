# rest-fut21 

## Instalacion

Despues de clonar, hay que crear un ambiente virtual e instalar las dependencias. En Linux:
	$ python3 -m venv nombre del ambiente
	$ source env/bin/activate
	(nombre del ambiente)$ pip3 install requirements.txt

En Windows se deben usar los siguientes comandos:
	$ python -m venv nombre del ambiente
	$ venv\Scripts\activate
	(nombre del ambiente)$ pip install requirements.txt

## Ejecucion

### Nota
El servidor de base de datos usado puede ser MySQL/MariaDB. 
Hay que crear la base de datos, primero que nada.

Para correr el servidor hay que configurar las variables de entorno. En Windows:
	$ set DB_HOST=nombre del host(puede ser localhost)
	$ set DB_USERNAME=nombre del usuario del servidor de BD
	$ set DB_PASSWORD=password
	$ set API_KEY= valor del header x-api-key
	$ set  FLASK_APP=api
	$ set FLASK_ENV=development

En Linux:
	$ export DB_HOST=nombre del host(puede ser localhost)
	$ export DB_USERNAME=nombre del usuario del servidor de BD
	$ export DB_PASSWORD=password
	$ export API_KEY= valor del header x-api-key
	$ set  FLASK_APP=api/
	$ set FLASK_ENV=development

Por ultimo, se debe ejecutar las siguientes instrucciones:
	$ flask init-db
	$ flask run
