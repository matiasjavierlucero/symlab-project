# Symlab Project

Test para **Symlab**.  Desarrollado en **Django-REST-Framework**

## Como correrlo. 

 - Clonar el repositorio `git clone https://github.com/matiasjavierlucero/symlab-project.git`
 - `cd symlab-project`
 - `pip install -r requirements.txt`
 - `cd symlab`
 - `python manage.py runserver`

## Endpoints disponibles

Se encuentran disponibles todos los endpoints que hacen a un CRUD para los modelos de 

> Clientes, Vehiculos, Reparaciones

## Acceder a los endpoints

Del 01/11/2021 al 01/02/2022 se puede acceder a ellos desde 
 - http://matiasjavierlucero.pythonanywhere.com/clientes/
 - http://matiasjavierlucero.pythonanywhere.com/clientes/`<id>`
 - http://matiasjavierlucero.pythonanywhere.com/vehiculos/
 - http://matiasjavierlucero.pythonanywhere.com/vehiculos/`<id>`
 - http://matiasjavierlucero.pythonanywhere.com/reparaciones/
 - http://matiasjavierlucero.pythonanywhere.com/reparaciones/`<id>`
 
 O bien desde :
- http://localhost:8000/clientes/
- http://localhost:8000/clientes/`<id>`
- http://localhost:8000/vehiculos/
- http://localhost:8000/vehiculos/`<id>`
- http://localhost:8000/reparaciones/
- http://localhost:8000/reparaciones/`<id>`

## Como crear un elemento

- CLIENTES Method POST :
	

	    {
		    "apellido":"Lucero",
		    "nombre":"Matias Javier",
		    "dni": 12345678,
		    "telefono":358444444
	    }
- VEHICULOS Method POST:
	

		{
			"placa": "B-1234",
			"marca": "VW",
			"modelo":"Gol",
			"anio": 2009,
			"cliente": 1
		}
- REPARACIONES Method POST:

		{
			"vehiculo":1,
			"fecha":"2020-01-10",
			"descripcion":"Reparacion de bomba inyectora",
			"costo":15412.00
		}
