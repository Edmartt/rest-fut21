# REST-FUT21

## Instalacion en Virtualenv

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
	$ set  FLASK_APP=run.py
	$ set FLASK_ENV=development

En Linux:

	$ export DB_HOST=nombre del host(puede ser localhost)
	$ export DB_USERNAME=nombre del usuario del servidor de BD
	$ export DB_PASSWORD=password
	$ export API_KEY= valor del header x-api-key
	$ export  FLASK_APP=run.py
	$ export FLASK_ENV=development



Por ultimo, se debe ejecutar las siguientes instrucciones, tanto en Windows como en Linux:

	$ flask init-db 
	$ flask run

## Despliegue con Docker:

    $ docker-compose build
    # docker-compose up

### NOTA
Una vez se haya completado el despliegue, podemos hacer uso del script [datagetter](https://github.com/Edmartt/datagetter) para recolectar los datos y realizar las respectivas pruebas a los distintos endpoints del API REST.





Documentación de la API
-----------------------

### Mostrar Jugadores

Retorna todos los jugadores que pertenezcan a un equipo.

* **URL** 

  /api/v1/team/<string:team_name>

* **Métodos:**
  
  `GET`

* **Parámetros de URL**

  **Requerido:**

  `name=[string]`

* **Respuesta exitosa:**

  * **Código:** 200 <br />
    **Contenido:** `{club: Icons, id: 9, name: Diego Armando Maradona, nation: Argentina, position: CAM}`

* **Respuesta de Error:**
  
  * **Código:** 404 NOT FOUND <br />
    **Contenido:** `{Error: Not Found}`

   O

  * **Código:** 401 UNAUTHORIZED <br />
    **Contenido:** `{message: Not Authorized}`

