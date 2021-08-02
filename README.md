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

## script.py

Ya que tenemos todo configurado, podemos hacer uso del archivo **script.py**:
	
	$ python script.py

Luego de la ejecución del script, se creará la tabla **playersdata** yla consola se pausará un momento; esto significa que
ya ha recolectado los datos de la primera página, los habrá guardado en nuestra base de datos
anteriormente creada y preguntará si se desea continuar con los datos de la siguiente página. 
Una vez consideremos que tenemos suficientes datos, podemos empezar a hacer uso de la API para probar su funcionamiento.

Por ultimo, se debe ejecutar las siguientes instrucciones:


	$ flask init-db * Este comando solo nos sirve si no hemos creado la tabla con la ejecución del script
	$ flask run
