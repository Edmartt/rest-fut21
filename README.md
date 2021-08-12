# REST-FUT21

## Install on Virtualenv

After cloning, a virtual environment must be created. On Linux:

	$ python3 -m venv virtualenv name 
	$ source env/bin/activate
	(virtualenv name)$ pip3 install requirements.txt

On Linux:

	$ python -m venv nombre del ambiente
	$ venv\Scripts\activate
	(virtualenv name)$ pip install requirements.txt

## Running

### Note

The database server can be MySQL/MariaDB. The database must be created first of all.

To run the server, you have to set the environment variables. On Windows:

	$ set MYSQL_HOST=hostname (localhost)
	$ set MYSQL_USER=server username
	$ set MYSQL_PASSWORD=server password
	$ set MYSQL_DATABASE=database name
	$ set API_KEY= header x-api-key value
	$ set FLASK_APP=run.py
	$ set FLASK_ENV=development

En Linux:

	$ export MYSQL_HOST=hostname (localhost)
	$ export MYSQL_USER=server username
	$ export MYSQL_PASSWORD=server password
	$ export MYSQL_DATABASE=database name
	$ export API_KEY= header x-api-key value
	$ export FLASK_APP=run.py
	$ export FLASK_ENV=development



Finally, the following instruction must be used, on Linux and Windows:

	$ flask init-db 
	$ flask run

## Docker deployment:

    $ docker-compose build
    # docker-compose up

### NOTE

Once the deployment is complete, we can make use of the datagetter script [datagetter](https://github.com/Edmartt/datagetter) to collect the data and perform the respective tests on the different endpoints of the REST API.





API Documentation
-----------------------

### Show Players

Returns all the players that belong to a team. The right **x-api-key** header must be sent.

* **URL** 

  /api/v1/team/:team_name

* **Methods:**
  
  `GET`

* **URL Parameters**

  **Required:**

  `name=[string]`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{club: Icons, id: 9, name: Diego Armando Maradona, nation: Argentina, position: CAM}`

* **Error Response:**
  
  * **Code:** 404 NOT FOUND <br />
    **Content:** `{Error: Not Found}`

   Or

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{message: Not Authorized}`


### Search Coincidences:

Returns the players data searched by partial or full name, returning all the coincidences.<br /> Sort the results in a ascending or descending way. By default, the order is ascending. The right x-api-key header must be sent.

* **URL** 

  /api/v1/players?search=name&order=

* **Methods:**
  
  `GET`

* **URL Parameters**

  **Required:**

  `name=[string o char]`
  
  **Optional:**

  `order=[asc o desc]`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{club: FC Barcelona, id: 14, name: Luis Suárez, nation: Uruguay, position: ST}, {club: Real Madrid, id: 2, name: Luka Modric, nation: Croatia, position: CM}`

* **Error Response:**
  
  * **Code:** 404 NOT FOUND <br />
    **Content:** `{Error: Not Found}`

   Or

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{message: Not Authorized}`

### Example

With a tool like `curl` we can make a request to the endpoint **/api/v1/team/** sending the **x-api-key** header:

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

If we do the request without the **x-api-key** header:

    $ curl -i -X GET http://localhost:5000/api/v1/team/Icons
    HTTP/1.0 401 UNAUTHORIZED
    Content-Type: application/json
    Content-Length: 34
    Server: Werkzeug/2.0.1 Python/3.7.11
    Date: Thu, 05 Aug 2021 06:21:28 GMT

    {
    	"message": "Not Authorized"
    }

If we do the request with a wrong **x-api-key** header:

    $ curl -i -H "x-api-key: 1234i" -X GET http://localhost:5000/api/v1/team/Icons
    HTTP/1.0 401 UNAUTHORIZED
    Content-Type: application/json
    Content-Length: 34
    Server: Werkzeug/2.0.1 Python/3.7.11
    Date: Thu, 05 Aug 2021 06:24:42 GMT
    {
      "message": "Not Authorized"
    }

The endpoint **/api/v1/players** works like this:

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

The result is to return all the players whose names begin with the letter d. If an additional querystring is sent **order** <br />
we can reverse the order in which the players are displayed:

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

## Credits

* [Edmartt's Profile](https://github.com/Edmartt)
  - The developer of this REST API Demo

* [vishnubob's Profile](https://github.com/vishnubob)
  - for the development of the [wait-for-it script](https://github.com/vishnubob/wait-for-it)
