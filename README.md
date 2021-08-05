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

	$ set MYSQL_HOST=nombre del host(puede ser localhost)
	$ set MYSQL_USER=nombre del usuario del servidor de BD
	$ set MYSQL_PASSWORD=password
	$ set API_KEY= valor del header x-api-key
	$ set FLASK_APP=run.py
	$ set FLASK_ENV=development

En Linux:

	$ export MYSQL_HOST=nombre del host(puede ser localhost)
	$ export MYSQL_USER=nombre del usuario del servidor de BD
	$ export MYSQL_PASSWORD=password
	$ export API_KEY= valor del header x-api-key
	$ export FLASK_APP=run.py
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

Retorna todos los jugadores que pertenezcan a un equipo. Hay que enviar el header **x-api-key** con la clave válida.

* **URL** 

  /api/v1/team/:team_name

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


### Buscar Coincidencias

Retorna datos de los jugadores buscados por nombre completo o parcial, devolviendo todas las coincidencias.<br /> Ordena los resultados de forma ascendente o descendente. Por defecto el orden es ascendente. Hay que enviar el header **x-api-key** con la clave válida.

* **URL** 

  /api/v1/players?search=name&order=

* **Métodos:**
  
  `GET`

* **Parámetros de URL**

  **Requerido:**

  `name=[string o char]`
  
  **Opcional:**

  `order=[asc o desc]`

* **Respuesta exitosa:**

  * **Código:** 200 <br />
    **Contenido:** `{club: FC Barcelona, id: 14, name: Luis Suárez, nation: Uruguay, position: ST}, {club: Real Madrid, id: 2, name: Luka Modric, nation: Croatia, position: CM}`

* **Respuesta de Error:**
  
  * **Código:** 404 NOT FOUND <br />
    **Contenido:** `{Error: Not Found}`

   O

  * **Código:** 401 UNAUTHORIZED <br />
    **Contenido:** `{message: Not Authorized}`

### Ejemplo

Con la herramienta `curl` hacemos una petición al endpoint **/api/v1/team/** enviando el header **x-api-key**:

    $ curl -i -H "x-api-key: 1234" -X GET http://localhost:5000/api/v1/team/Icons
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 675
    Server: Werkzeug/2.0.1 Python/3.7.11
    Date: Thu, 05 Aug 2021 06:16:27 GMT

    [
    {
        "club": "Icons",
	"id": 9,
	"name": "Edson Arantes Nascimento",
	"nation": "Brazil",
	"position": "CAM"
			  
    },
    {
        "club": "Icons",
	"id": 23,
	"name": "Diego Maradona",
	"nation": "Argentina",
	"position": "CAM"
			  
    },
    {
        "club": "Icons",
	"id": 36,
	"name": "Ronaldo Luis Nazário de Lima",
	"nation": "Brazil",
	"position": "ST"
			  
    },
    {
        "club": "Icons",
	"id": 81,
	"name": "Edson Arantes Nascimento",
	"nation": "Brazil",
	"position": "CAM"
			  
    },
    {
        "club": "Icons",
	"id": 95,
	"name": "Diego Maradona",
	"nation": "Argentina",
	"position": "CAM"
			  
      }
    ]

Si hacemos el request sin el header x-api-key:

    $ curl -i -X GET http://localhost:5000/api/v1/team/Icons
    HTTP/1.0 401 UNAUTHORIZED
    Content-Type: application/json
    Content-Length: 34
    Server: Werkzeug/2.0.1 Python/3.7.11
    Date: Thu, 05 Aug 2021 06:21:28 GMT

    {
    	"message": "Not Authorized"
    }

Si hacemos el request con un header x-api-key erróneo:

    $ curl -i -H "x-api-key: 1234i" -X GET http://localhost:5000/api/v1/team/Icons
    HTTP/1.0 401 UNAUTHORIZED
    Content-Type: application/json
    Content-Length: 34
    Server: Werkzeug/2.0.1 Python/3.7.11
    Date: Thu, 05 Aug 2021 06:24:42 GMT
    {
      "message": "Not Authorized"
    }

El endpoint **/api/v1/players** funciona de la siguiente manera:

    $ curl -i -H "x-api-key: 1234" -X GET http://localhost:5000/api/v1/players?search=d

    [
     {
      "club": "Manchester United",
      "id": 27,
      "name": "David De Gea Quintana",
      "nation": "Spain",
      "position": "GK"
		      
    },
    {
     "club": "Atlético Madrid",
     "id": 40,
     "name": "Diego Godín",
     "nation": "Uruguay",
     "position": "CB"
		      
    },
    {
     "club": "Icons",
     "id": 23,
     "name": "Diego Maradona",
     "nation": "Argentina",
     "position": "CAM"
		      
    },
    {
     "club": "Icons",
     "id": 95,
     "name": "Diego Maradona",
     "nation": "Argentina",
     "position": "CAM"
		      
      }
    ]

El resultado es retornar todos los jugadores cuyos nombres empiecen por la letra d. Si se envía un querystring adicional **order** <br />
podemos invertir el orden en el que se muestran los jugadores:

    $ curl -i -H "x-api-key: 1234" -X GET "http://localhost:5000/api/v1/players?search=d&order=desc"

    [
     {
     "club": "Icons",
     "id": 23,
     "name": "Diego Maradona",
     "nation": "Argentina",
     "position": "CAM"
     },
     {
     "club": "Icons",
     "id": 95,
     "name": "Diego Maradona",
     "nation": "Argentina",
     "position": "CAM"
     },
     {
     "club": "Atlético Madrid",
     "id": 40,
     "name": "Diego Godín",
     "nation": "Uruguay",
     "position": "CB"
     },
     {
     "club": "Manchester United",
     "id": 27,
     "name": "David De Gea Quintana",
     "nation": "Spain",
     "position": "GK"		      
     }
    ]
