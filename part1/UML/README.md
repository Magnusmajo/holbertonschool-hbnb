# Documentacion de diagramas:

## Diagrama de clases 

### Descripción General
Objetivo: Este diagrama de clases de HBNB muestra la organización y las conexiones entre las clases en la plataforma. Describe los elementos que participan en las interacciones de los usuarios, la administración de propiedades y los procedimientos de reseñas.

### clases:
#### lista de clases:

##### Users
- atributos: ("firstName", "lastName", "email", "password" and "isAdmin")
- metodos: ("register", "login", "update" and "delete")

##### Review
- atributos: ("rating", "comment", "place" and "user")
- metodos: ("create", "update", "delete" and "listByPlace")

##### Place
- atributos: ("title", "description", "price", "latitude", "owner" and "amenities")
- metodos: ("create", "update", "delete" and "list")

##### Amenity
- atributos: ("name" and "description")
- metodos: ("create", "update", "delete" and "list")


## Relaciones 
- **Clase User ↔ Clase Review**: La clase User mantiene una referencia a la clase Review, lo que sugiere que un usuario puede realizar múltiples reseñas para distintos lugares.

- **Clase User ↔ Clase Place**: La clase Place está vinculada con la clase User, ya que cada lugar debe ser creado por un usuario.

- **Clase Place ↔ Clase Review**: La clase Review hace referencia a la clase Place, indicando que cada reseña corresponde a un lugar específico.

##### Dependencias:

- **Clase Place ↔ Clase Amenities**: La clase Place se asocia con la clase Amenities, permitiendo que un lugar tenga varios servicios adicionales, como Wi-Fi, estacionamiento o piscina.