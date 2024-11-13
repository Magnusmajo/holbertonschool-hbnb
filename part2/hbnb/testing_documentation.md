# Documentación de Pruebas de Endpoints

## Descripción General

**Nombre del Proyecto:** HBnB Evolution  
**Fecha de Documentación:** 27/10/2024  
**Autores:** Bryan Alemán, Luna Leguisamo, Julieta Bobadilla  
**Versión del Proyecto:** 1.0

**Objetivo de la Prueba:**  
Verificar que los endpoints respondan correctamente a peticiones válidas e inválidas, siguiendo las reglas de validación establecidas y devolviendo los códigos de estado HTTP correspondientes.

---

## Resumen de Pruebas Realizadas Utilizando cURL

Probar la validación de los datos en los endpoints

- Pruebas de respuesta con datos válidos
- Pruebas de manejo de errores con datos inválidos
- Verificación de códigos de respuesta HTTP esperados

---

## Prueba de Creación de Usuario Válida



| **Endpoint** | `/api/v1/users/` |
|--------------|-------------------------|
| **Descripción** | Crea un nuevo usuario. |
| **Cuerpo de la Petición** | JSON con atributos `first_name`, `last_name`, `email`. |
| **Tipo de Petición** | POST |
  
   - **Descripción:** Comprobar que el endpoint acepta una solicitud con datos válidos y crea correctamente el usuario.
   - **Datos de Entrada:** Usamos cURL para enviar una solicitud con datos válidos para crear un usuario y retornar código de estado.  

     ```bash
     curl -X POST "http://127.0.0.1:5000/api/v1/users/" -H "Content-Type: application/json" -d '{
     "first_name": "Lidia",
     "last_name": "Butterley",
     "email": "lbutterley0@bravesites.com"
     }' -w "%{http_code}\n"
     ```
   - **Respuesta Esperada:**  
     Código de estado: `201 Created`  
     Cuerpo de respuesta:
     ```json
     {
       "id": "<generated_id>", // ID generado automáticamente
       "first_name": "Lidia",
       "last_name": "Butterley",
       "email": "lbutterley0@bravesites.com"
     }
     ```
   - **Resultado de la Prueba:** `Pasó`  
     Código de estado: `201 Created`  
     Cuerpo de respuesta:
     ```json
     {
       "id": "a4ec44b7-8734-4116-9492-9aeb44eec988", // ID generado
       "first_name": "Lidia",
       "last_name": "Butterley",
       "email": "lbutterley0@bravesites.com"
     }
     ```


## Prueba de Creación de Usuario Inválida (campos vacíos)



| **Endpoint** | `/api/v1/users/` |
|--------------|-------------------------|
| **Descripción** | Crea un nuevo usuario con campos vacíos. |
| **Cuerpo de la Petición** | JSON con atributos `first_name`, `last_name`, `email`. |
| **Tipo de Petición** | POST |
  
   - **Descripción:** Confirmar que el sistema rechaza entradas con campos vacíos, mostrando un error en la respuesta.
   - **Datos de Entrada:** Usamos cURL para enviar una solicitud con campos vacíos y retornar código de estado.   

     ```bash
     curl -X POST "http://127.0.0.1:5000/api/v1/users/" -H "Content-Type: application/json" -d '{
     "first_name": "",
     "last_name": "",
     "email": ""
     }' -w "%{http_code}\n"
     ```
   - **Respuesta Esperada:**  
     Código de estado: `400 Bad Request`  
     Cuerpo de respuesta:
     ```json
     {
     "error": "Invalid input data"
     }
     ```
     
   - **Resultado de la Prueba:** `Falló`  
     Código de estado: `201 Created`  
     Cuerpo de respuesta:
     ```json
     {
     "id": "9511d94b-e374-4165-9f76-a5a5b6064987", // ID generado
     "first_name": "",
     "last_name": "",
     "email": ""
     }
     ```
     Descripción del error: El sistema aceptó datos inválidos (`first_name`, `last_name` y `email` vacíos) y generó un nuevo usuario en lugar de rechazar la solicitud.


## Prueba de Creación de Usuario Inválida (email inválido)



| **Endpoint** | `/api/v1/users/` |
|--------------|-------------------------|
| **Descripción** | Crea un nuevo usuario con email inválido. |
| **Cuerpo de la Petición** | JSON con atributos `first_name`, `last_name`, `email`. |
| **Tipo de Petición** | POST |
  
   - **Descripción:** Confirmar que el sistema rechaza la entrada de un campo inválido, mostrando un error en la respuesta.
   - **Datos de Entrada:** Usamos cURL para enviar una solicitud con email inválido y retornar código de estado.   

     ```bash
     curl -X POST "http://127.0.0.1:5000/api/v1/users/" -H "Content-Type: application/json" -d '{
     "first_name": "Lidia",
     "last_name": "Butterley",
     "email": "lbutterley"
     }' -w "%{http_code}\n"
     ```
   - **Respuesta Esperada:**  
     Código de estado: `400 Bad Request`  
     Cuerpo de respuesta:
     ```json
     {
     "error": "Invalid email format"
     }
     ```
     
   - **Resultado de la Prueba:** `Falló`  
     Código de estado: `201 Created`  
     Cuerpo de respuesta:
     ```json
     {
     "id": "9511d94b-e374-4165-9f76-a5a5b6064987", // ID generado
     "first_name": "Lidia",
     "last_name": "Butterley",
     "email": "lbutterley"
     }
     ```
     Descripción del error: El sistema aceptó datos inválidos (`email` inválido) y generó un nuevo usuario en lugar de rechazar la solicitud.


## Prueba de Creación de Lugar (place) Válida



| **Endpoint** | `/api/v1/places/` |
|--------------|-------------------------|
| **Descripción** | Crear un nuevo lugar. |
| **Cuerpo de la Petición** | JSON con los atributos `title`, `description`, `price`, `latitude`, `longitude`, `owner_id` y `amenities`. |
| **Tipo de Petición** | POST |
  
   - **Descripción:** Comprobar que el endpoint acepta una solicitud con datos válidos y crea correctamente un lugar.
   - **Datos de Entrada:** Usamos cURL para enviar una solicitud con datos válidos para crear un lugar y retornar el código de estado, `owner_id` y `amenities` deben ser creados antes de la prueba y sustituir con sus `id` correspondientes.  

     ```bash
     curl -X POST "http://127.0.0.1:5000/api/v1/places/" \
     -H "Content-Type: application/json" \
     -d '{
     "title": "Hermosa Casa",
     "description": "Lugar tranquilo con una gran vista",
     "price": 150.00,
     "latitude": 45.0,
     "longitude": -70.0,
     "owner_id": "a062b085-9432-489b-9bdf-0bab29b4e27a",
     "amenities": ["54bd4f2b-b122-4706-93f6-9b0952dce101"]
     }' -w "%{http_code}\n"
     ```
   - **Respuesta Esperada:**  
     Código de estado: `201 Created`  
     Cuerpo de respuesta:
     ```json
     {
     "id": "15db46c2-66db-48d4-afbb-8f6e8466e46a",
     "title": "Hermosa Casa",
     "description": "Lugar tranquilo con una gran vista",
     "price": 150.0,
     "latitude": 45.0,
     "longitude": -70.0,
     "owner_id": "a4ec44b7-8734-4116-9492-9aeb44eec988",
     "amenities": [
        {
           "id": "54bd4f2b-b122-4706-93f6-9b0952dce101",
           "name": "wifi"
        }
     ],
     "reviews": []
     }
     ```
   - **Resultado de la Prueba:** `Pasó`  
     Código de estado: `201 Created`  
     Cuerpo de respuesta:
     ```json
     {
     "id": "15db46c2-66db-48d4-afbb-8f6e8466e46a",
     "title": "Hermosa Casa",
     "description": "Lugar tranquilo con una gran vista",
     "price": 150.0,
     "latitude": 45.0,
     "longitude": -70.0,
     "owner_id": "a4ec44b7-8734-4116-9492-9aeb44eec988",
     "amenities": [
        {
           "id": "54bd4f2b-b122-4706-93f6-9b0952dce101",
           "name": "wifi"
        }
     ],
     "reviews": []
     }
     ```


## Prueba de Creación de Lugar (place) Inválida



| **Endpoint** | `/api/v1/places/` |
|--------------|-------------------------|
| **Descripción** | Intenta crear un nuevo lugar con el campo del título vacío, un precio negativo y coordenadas fuera de rango. |
| **Cuerpo de la Petición** | JSON con los atributos `title`, `description`, `price`, `latitude`, `longitude`, `owner_id` y `amenities`. |
| **Tipo de Petición** | POST |
  
   - **Descripción:** Confirmar que el sistema rechaza entradas inválidas, mostrando un error en la respuesta.
   - **Datos de Entrada:** Usamos cURL para enviar una solicitud con datos inválidos para crear un lugar y retornar el código de estado, `owner_id` y `amenities` deben ser creados antes de la prueba y sustituir con sus `id` correspondientes.    

     ```bash
     curl -X POST "http://127.0.0.1:5000/api/v1/places/" \
     -H "Content-Type: application/json" \
     -d '{
     "title": "",
     "description": "Lugar tranquilo con una gran vista",
     "price": -150.00,
     "latitude": 95.0,
     "longitude": -200.0,
     "owner_id": "a4ec44b7-8734-4116-9492-9aeb44eec988",
     "amenities": ["54bd4f2b-b122-4706-93f6-9b0952dce101"]
     }' -w "%{http_code}\n"
     ```
   - **Respuesta Esperada:**  
     Código de estado: `400 Bad Request`  
     Cuerpo de respuesta:
     ```json
     {
     "error": "Invalid input data"
     }
     ```
   - **Resultado de la Prueba:** `Falló`  
     Código de estado: `201 Created`  
     Cuerpo de respuesta:
     ```json
     {
     "id": "330c9a51-4ab4-4e40-b39f-6aa77f621f8c",
     "title": "",
     "description": "Lugar tranquilo con una gran vista",
     "price": -50.0,
     "latitude": 95.0,
     "longitude": -200.0,
     "owner_id": "a4ec44b7-8734-4116-9492-9aeb44eec988",
     "amenities": [
        {
            "id": "54bd4f2b-b122-4706-93f6-9b0952dce101",
            "name": "wifi"
        }
     ],
     "reviews": []
     }
     ```
Descripción del error: El sistema aceptó datos inválidos (`title` vacío, `price` negativo y `latitude` y `longitude` fuera de rango) y generó un nuevo lugar en lugar de rechazar la solicitud.



## Prueba de Creación de Reseña Válida



| **Endpoint** | `/api/v1/reviews/` |
|--------------|-------------------------|
| **Descripción** | Crea una nueva reseña asociada a un usuario y un lugar. |
| **Cuerpo de la Petición** | JSON con atributos `test`, `rating`, `place_id` y `user_id`. |
| **Tipo de Petición** | POST |
  
   - **Descripción:** Comprobar que el endpoint crea una reseña con datos válidos.
   - **Datos de Entrada:** Usamos cURL para enviar una solicitud con datos válidos para crear una reseña y retornar código de estado.  

     ```bash
     curl -X POST "http://127.0.0.1:5000/api/v1/reviews/" \
     -H "Content-Type: application/json" \
     -d '{
     "text": "Un lugar espectacular para descansar",
     "rating": 5,
     "place_id": "15db46c2-66db-48d4-afbb-8f6e8466e46a",
     "user_id": "a4ec44b7-8734-4116-9492-9aeb44eec988"
     }' -w "%{http_code}\n"
     ```
   - **Respuesta Esperada:**  
     Código de estado: `201 Created`  
     Cuerpo de respuesta:
     ```json
     {
     "id": "4f763cc8-a23e-46c1-8087-aeb44ad8b2fc",
     "text": "Un lugar espectacular para descansar",
     "rating": 5,
     "user_id": "a4ec44b7-8734-4116-9492-9aeb44eec988",
     "place_id": "15db46c2-66db-48d4-afbb-8f6e8466e46a"
     }
     ```
   - **Resultado de la Prueba:** `Pasó`  
     Código de estado: `200 OK`  
     Cuerpo de respuesta:
     ```json
     {
     "id": "4f763cc8-a23e-46c1-8087-aeb44ad8b2fc",
     "text": "Un lugar espectacular para descansar",
     "rating": 5,
     "user_id": "a4ec44b7-8734-4116-9492-9aeb44eec988",
     "place_id": "15db46c2-66db-48d4-afbb-8f6e8466e46a"
     }
     ```
Notas: El servidor procesó la solicitud, pero no devolvió el código `201 Created` que sería el más adecuado para indicar la creación de un nuevo recurso.



## Prueba de Creación de Reseña Inválida



| **Endpoint** | `/api/v1/reviews/` |
|--------------|-------------------------|
| **Descripción** | Intenta crear una reseña con datos inválidos. |
| **Cuerpo de la Petición** | JSON con atributos `test`, `rating`, `place_id` y `user_id`. |
| **Tipo de Petición** | POST |
  
   - **Descripción:** Confirmar que el sistema rechaza entradas inválidas, mostrando un error en la respuesta.
   - **Datos de Entrada:** Usamos cURL para enviar una solicitud con `rating` fuera del rango permitido y sin `text`, y retornar código de estado.  

     ```bash
     curl -X POST "http://127.0.0.1:5000/api/v1/reviews/" \
     -H "Content-Type: application/json" \
     -d '{
     "text": "",
     "rating": 6,
     "place_id": "15db46c2-66db-48d4-afbb-8f6e8466e46a",
     "user_id": "a4ec44b7-8734-4116-9492-9aeb44eec988"
     }' -w "%{http_code}\n"
     ```
   - **Respuesta Esperada:**  
     Código de estado: `400 Bad Request`  
     Cuerpo de respuesta:
     ```json
     {
     "error": "Invalid input data"
     }
     ```
   - **Resultado de la Prueba:** `Falló`  
     Código de estado: `200 OK`  
     Cuerpo de respuesta:
     ```json
     {
     "id": "f5da6870-ba21-4121-9ae6-61c7e09493c9",
     "text": "",
     "rating": 6,
     "user_id": "a4ec44b7-8734-4116-9492-9aeb44eec988",
     "place_id": "15db46c2-66db-48d4-afbb-8f6e8466e46a"
     }
     ```
Descripción del error: El sistema aceptó datos inválidos (`text` vacío y `rating` fuera de rango) y generó una nueva reseña en lugar de rechazar la solicitud.



## Prueba de Creación de Amenity Válida



| **Endpoint** | `/api/v1/amenities/` |
|--------------|-------------------------|
| **Descripción** | Crea un nuevo "Amenity" (servicio) que luego puede ser asociado a un lugar. |
| **Cuerpo de la Petición** | JSON con atributo `name`. |
| **Tipo de Petición** | POST |
  
   - **Descripción:** Comprobar que el endpoint acepta una solicitud con datos válidos y crea el servicio correctamente.
   - **Datos de Entrada:** Usamos cURL para enviar una solicitud con datos válidos para crear un amenity y retornar código de estado.  

     ```bash
     curl -X POST "http://127.0.0.1:5000/api/v1/amenities/" \
     -H "Content-Type: application/json" \
     -d '{
     "name": "Estacionamiento"
     }' -w "%{http_code}\n"
     ```
   - **Respuesta Esperada:**  
     Código de estado: `201 Created`  
     Cuerpo de respuesta:
     ```json
     {
     "id": "<generated_id>", // ID generado automáticamente
     "name": "Estacionamiento"
     }
     ```
   - **Resultado de la Prueba:** `Pasó`  
     Código de estado: `201 Created`  
     Cuerpo de respuesta:
     ```json
     {
     "id": "204d1b70-c817-4ae4-9c30-82fc7a995a08", // ID generado
     "name": "Estacionamiento"
     }
     ```


## Prueba de Creación de Amenity Inválida



| **Endpoint** | `/api/v1/amenities/` |
|--------------|-------------------------|
| **Descripción** | Intenta crear una amenity con datos inválidos. |
| **Cuerpo de la Petición** | JSON con atributo `name`. |
| **Tipo de Petición** | POST |
  
   - **Descripción:** Comprobar que el endpoint acepta una solicitud con datos inválidos y muestra un error en la respuesta.
   - **Datos de Entrada:** Usamos cURL para enviar una solicitud con datos inválidos (`name` exceda el límite permitido) para crear un amenity y retornar código de estado.  

     ```bash
     curl -X POST "http://127.0.0.1:5000/api/v1/amenities/" \
     -H "Content-Type: application/json" \
     -d '{
     "name": "Amenity con un nombre demasiado largo para probar la validación en el sistema"
     }' -w "%{http_code}\n"
     ```
   - **Respuesta Esperada:**  
     Código de estado: `400 Bad Request`  
     Cuerpo de respuesta:
     ```json
     {
     "error": "Name is too long"
     }
     ```
   - **Resultado de la Prueba:** `Falló`  
     Código de estado: `201 Created`  
     Cuerpo de respuesta:
     ```json
     {
     "id": "fec550ce-c10d-499d-9380-ea7234d972f3",
     "name": "Amenity con un nombre demasiado largo para probar la validación en el sistema"
     }
     ```
Descripción del error: El sistema aceptó datos inválidos (`name` demasiado largo) y generó un nuevo amenity en lugar de rechazar la solicitud.


# Documentación de Pruebas con Pytest

## Introducción
Esta sección documenta las pruebas automatizadas realizadas utilizando `pytest` en el proyecto **HBnB**. A continuación, se describen las pruebas específicas y los resultados obtenidos.

#### Entorno de Prueba
- **Sistema Operativo**: Linux
- **Python**: 3.10.12
- **Framework de pruebas**: Pytest 8.3.3
---

## Prueba: `test_users.py`

#### Descripción
El archivo `test_users.py` contiene pruebas para la funcionalidad relacionada con los usuarios en el sistema. Estas pruebas aseguran que las funcionalidades básicas de creación y validación de usuarios cumplen con los requisitos especificados.

#### Comando de Ejecución
Para ejecutar la prueba, se utilizó el siguiente comando desde el directorio `tests`:

```bash
pytest test_users.py
```
### Resultado Esperado
El sistema debe pasar todas las pruebas definidas en test_users.py sin errores.
### Resultado Obtenido
```txt
=========================================================================================== test session starts ============================================================================================
platform linux -- Python 3.10.12, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/balemansteve/holbertonschool-hbnb/part2/tests
collected 3 items                                                                                                                                                                                          

test_users.py .FF                                                                                                                                                                                    [100%]

================================================================================================= FAILURES =================================================================================================
_____________________________________________________________________________________ test_user_creation_empty_fields ______________________________________________________________________________________

    def test_user_creation_empty_fields():
        '''
        User creation test with empty fields.
        '''
        data = {
            "first_name": "",
            "last_name": "",
            "email": ""
        }
        response = requests.post(f"{BASE_URL}/users/", json=data)
>       assert response.status_code == 400
E       assert 201 == 400
E        +  where 201 = <Response [201]>.status_code

test_users.py:33: AssertionError
_____________________________________________________________________________________ test_user_creation_invalid_email _____________________________________________________________________________________

    def test_user_creation_invalid_email():
        '''
        User creation test with invalid email.
        '''
        data = {
            "first_name": "Lidia",
            "last_name": "Butterley",
            "email": "lbutterley"
        }
        response = requests.post(f"{BASE_URL}/users/", json=data)
>       assert response.status_code == 400
E       assert 201 == 400
E        +  where 201 = <Response [201]>.status_code

test_users.py:47: AssertionError
========================================================================================= short test summary info ==========================================================================================
FAILED test_users.py::test_user_creation_empty_fields - assert 201 == 400
FAILED test_users.py::test_user_creation_invalid_email - assert 201 == 400
======================================================================================= 2 failed, 1 passed in 0.16s ========================================================================================
```



### Análisis del Resultado
 - **Prueba `test_user_creation_valid`**  
     Descripción: Crea un usuario con datos válidos.  
     Código de estado esperado: `201 Created`  
     Código de estado recibido: `201 Created`   
     Resultado: `Pasó`, el usuario fue creado exitosamente.      

 - **Prueba `test_user_creation_empty_fields`**  
     Descripción: Crea un usuario con campos vacíos.   
     Código de estado esperado: `400 Bad Request`  
     Código de estado recibido: `201 Created`   
     Resultado: `Falló`, el sistema permitió la creación de un usuario con campos vacíos.

 - **Prueba `test_user_creation_invalid_email`**  
     Descripción: Crea un usuario con email inválido.    
     Código de estado esperado: `400 Bad Request`  
     Código de estado recibido: `201 Created`   
     Resultado: `Falló`, el sistema permitió la creación de un usuario con email inválido.




## Prueba: `test_places.py`

#### Descripción
El archivo `test_places.py` contiene pruebas para la funcionalidad relacionada con la creación de lugares (places) en el sistema. Estas pruebas aseguran que las funcionalidades básicas de creación y validación de lugares cumplen con los requisitos especificados.

#### Comando de Ejecución
Para ejecutar la prueba, se utilizó el siguiente comando desde el directorio `tests`:

```bash
pytest test_places.py
```
### Resultado Esperado
El sistema debe pasar todas las pruebas definidas en test_places.py sin errores.
### Resultado Obtenido
```txt
balemansteve@DESKTOP-PPJI7L7:~/holbertonschool-hbnb/part2/tests$ pytest test_places.py 
=========================================================================================== test session starts ============================================================================================
platform linux -- Python 3.10.12, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/balemansteve/holbertonschool-hbnb/part2/tests
collected 2 items                                                                                                                                                                                          

test_places.py .F                                                                                                                                                                                    [100%]

================================================================================================= FAILURES =================================================================================================
_______________________________________________________________________________________ test_place_creation_invalid ________________________________________________________________________________________

create_user = '698a05fd-42f2-4b8e-83a8-be955f216f25', create_amenity = '49cd2459-de1d-4438-84ab-3ada9b5d50f8'

    def test_place_creation_invalid(create_user, create_amenity):
        """
        Place creation test with invalid data.
        """
        data = {
            "title": "",
            "description": "Lugar tranquilo con una gran vista",
            "price": -150.00,
            "latitude": 95.0,
            "longitude": -200.0,
            "owner_id": create_user,  # Replace with valid owner_id
            "amenities": [create_amenity]  # Replace with valid amenity
        }
        response = requests.post(f"{BASE_URL}/places/", json=data)
>       assert response.status_code == 400
E       assert 201 == 400
E        +  where 201 = <Response [201]>.status_code

test_places.py:65: AssertionError
========================================================================================= short test summary info ==========================================================================================
FAILED test_places.py::test_place_creation_invalid - assert 201 == 400
======================================================================================= 1 failed, 1 passed in 0.17s ========================================================================================
```



### Análisis del Resultado
 - **Prueba `test_place_creation_valid`**  
     Descripción: Crea un lugar con datos válidos.  
     Código de estado esperado: `201 Created`  
     Código de estado recibido: `201 Created`   
     Resultado: `Pasó`, el lugar fue creado exitosamente.      

 - **Prueba `test_place_creation_invalid`**  
     Descripción: Crea un lugar con el título vacío, precio negativo y coordenadas fuera de rango.   
     Código de estado esperado: `400 Bad Request`  
     Código de estado recibido: `201 Created`   
     Resultado: `Falló`, el sistema permitió la creación de un lugar con campos inválidos.



## Prueba: `test_reviews.py`

#### Descripción
El archivo `test_reviews.py` contiene pruebas para la funcionalidad relacionada con la creación de reseñas en el sistema. Estas pruebas aseguran que las funcionalidades básicas de creación y validación de reseñas cumplen con los requisitos especificados.

#### Comando de Ejecución
Para ejecutar la prueba, se utilizó el siguiente comando desde el directorio `tests`:

```bash
pytest test_reviews.py
```
### Resultado Esperado
El sistema debe pasar todas las pruebas definidas en test_reviews.py sin errores.
### Resultado Obtenido
```txt
balemansteve@DESKTOP-PPJI7L7:~/holbertonschool-hbnb/part2/tests$ pytest test_reviews.py 
=========================================================================================== test session starts ============================================================================================
platform linux -- Python 3.10.12, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/balemansteve/holbertonschool-hbnb/part2/tests
collected 4 items                                                                                                                                                                                          

test_reviews.py FFFF                                                                                                                                                                                 [100%]

================================================================================================= FAILURES =================================================================================================
________________________________________________________________________________________ test_review_creation_valid ________________________________________________________________________________________

create_place = '119fd582-0cd8-4088-9743-018a845a062f', create_user = 'cdea5c05-149b-4ed7-b33c-459066912941'

    def test_review_creation_valid(create_place, create_user):
        """
        Create a valid review.
        """
        data = {
            "text": "Lugar excelente, me gustó mucho.",
            "rating": 5,
            "place_id": create_place,
            "user_id": create_user
        }
        response = requests.post(f"{BASE_URL}/reviews/", json=data)
>       assert response.status_code == 201
E       assert 200 == 201
E        +  where 200 = <Response [200]>.status_code

test_reviews.py:55: AssertionError
_____________________________________________________________________________________ test_review_creation_empty_text ______________________________________________________________________________________

create_place = '119fd582-0cd8-4088-9743-018a845a062f', create_user = 'cdea5c05-149b-4ed7-b33c-459066912941'

    def test_review_creation_empty_text(create_place, create_user):
        """
        Create a review with empty text.
        """
        data = {
            "text": "",
            "rating": 5,
            "place_id": create_place,
            "user_id": create_user
        }
        response = requests.post(f"{BASE_URL}/reviews/", json=data)
>       assert response.status_code == 400
E       assert 200 == 400
E        +  where 200 = <Response [200]>.status_code

test_reviews.py:70: AssertionError
___________________________________________________________________________________ test_review_creation_invalid_user_id ___________________________________________________________________________________

create_place = '119fd582-0cd8-4088-9743-018a845a062f'

    def test_review_creation_invalid_user_id(create_place):
        """
        Create a invalid review with invalid user_id.
        """
        data = {
            "text": "Review con usuario inválido.",
            "rating": 5,
            "place_id": create_place,
            "user_id": "invald_id"
        }
        response = requests.post(f"{BASE_URL}/reviews/", json=data)
>       assert response.status_code == 400
E       assert 200 == 400
E        +  where 200 = <Response [200]>.status_code

test_reviews.py:85: AssertionError
__________________________________________________________________________________ test_review_creation_invalid_place_id ___________________________________________________________________________________

create_user = 'cdea5c05-149b-4ed7-b33c-459066912941'

    def test_review_creation_invalid_place_id(create_user):
        """
        Create a invalid review with invalid place_id.
        """
        data = {
            "text": "Review con lugar inválido.",
            "rating": 5,
            "place_id": "invalid_id",
            "user_id": create_user
        }
        response = requests.post(f"{BASE_URL}/reviews/", json=data)
>       assert response.status_code == 400
E       assert 200 == 400
E        +  where 200 = <Response [200]>.status_code

test_reviews.py:100: AssertionError
========================================================================================= short test summary info ==========================================================================================
FAILED test_reviews.py::test_review_creation_valid - assert 200 == 201
FAILED test_reviews.py::test_review_creation_empty_text - assert 200 == 400
FAILED test_reviews.py::test_review_creation_invalid_user_id - assert 200 == 400
FAILED test_reviews.py::test_review_creation_invalid_place_id - assert 200 == 400
============================================================================================ 4 failed in 0.19s =============================================================================================
```



### Análisis del Resultado
 - **Prueba `test_review_creation_valid`**  
     Descripción: Crea una reseña válida.  
     Código de estado esperado: `201 Created`  
     Código de estado recibido: `200 OK`   
     Resultado: `Falló`, el sistema no devolvió el estado correcto para la creación de una reseña válida.      

 - **Prueba `test_review_creation_empty_text`**  
     Descripción: Intenta crear una reseña con el texto vacío.   
     Código de estado esperado: `400 Bad Request`  
     Código de estado recibido: `200 OK`   
     Resultado: `Falló`, el sistema permitió la creación de una reseña con un campo de texto vacío.

 - **Prueba `test_review_creation_invalid_user_id`**  
     Descripción: Intenta crear una reseña con un `user_id` inválido.   
     Código de estado esperado: `400 Bad Request`  
     Código de estado recibido: `200 OK`   
     Resultado: `Falló`, el sistema aceptó una reseña con un id de usuario inválido.

 - **Prueba `test_review_creation_invalid_place_id`**  
     Descripción: Intenta crear una reseña con un `place_id` inválido.   
     Código de estado esperado: `400 Bad Request`  
     Código de estado recibido: `200 OK`   
     Resultado: `Falló`, el sistema aceptó una reseña con un identificador de lugar inválido.

