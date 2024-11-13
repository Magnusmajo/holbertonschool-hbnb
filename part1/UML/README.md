# documentacion de diagramas:

## diagrama de clases 

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
 