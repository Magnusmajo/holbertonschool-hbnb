# Diagrama de Clases de HBNB

## Descripción General

Este diagrama de clases de HBNB representa la estructura y las relaciones entre las clases principales en la plataforma. Expone los elementos que intervienen en las interacciones de los usuarios, la gestión de propiedades y los procesos de reseñas.

## Clases Principales y sus Relaciones

### Clase `Identifier`
- **Descripción**: Esta clase actúa como base para las clases `User`, `Place`, y `Review`, implementando un identificador único (`UUID4`) y registros de tiempo de creación y actualización.
- **Herencia**: `User`, `Place`, y `Review` heredan de `Identifier`, por lo que cada instancia tiene un identificador único y marcas de tiempo de creación y actualización.

### Clase `User`
- **Atributos**:
  - `firstName`: Nombre del usuario.
  - `lastName`: Apellido del usuario.
  - `email`: Dirección de correo electrónico del usuario.
  - `password`: Contraseña del usuario.
  - `isAdmin`: Indica si el usuario tiene permisos administrativos.
- **Relaciones**:
  - **User ↔ Review**: Un `User` puede tener múltiples `Review`, lo que indica que un usuario puede dejar varias reseñas en diferentes lugares.
  - **User ↔ Place**: Un `User` puede crear múltiples `Place`, mientras que cada `Place` tiene un solo propietario `User`.

### Clase `Place`
- **Atributos**:
  - `title`: Título del lugar.
  - `description`: Descripción del lugar.
  - `price`: Precio del lugar.
  - `latitude`: Latitud del lugar.
  - `longitude`: Longitud del lugar.
  - `owner`: Referencia al `User` propietario del lugar.
  - `amenities`: Lista de `Amenity` asociadas al lugar.
- **Relaciones**:
  - **Place ↔ User**: Cada `Place` está vinculado a un `User` como su propietario.
  - **Place ↔ Review**: Un `Place` puede tener múltiples `Review`, pero cada `Review` está asociada a un solo `Place`.
  - **Place ↔ Amenity**: Un `Place` puede tener varias `Amenity`, representando los servicios disponibles en ese lugar.

### Clase `Review`
- **Atributos**:
  - `rating`: Calificación del lugar.
  - `comment`: Comentario sobre el lugar.
  - `place`: Referencia al `Place` que está siendo reseñado.
  - `user`: Referencia al `User` que realizó la reseña.
- **Relaciones**:
  - **Review ↔ User**: Cada `Review` tiene un autor (`User`), indicando que un usuario puede escribir múltiples reseñas.
  - **Review ↔ Place**: Cada `Review` está dirigida a un solo `Place`.

### Clase `Amenity`
- **Atributos**:
  - `name`: Nombre de la amenidad.
  - `description`: Descripción de la amenidad.
- **Relaciones**:
  - **Amenity ↔ Place**: Un `Amenity` puede estar asociado con múltiples `Place`, permitiendo que un lugar tenga diversos servicios y que un servicio esté disponible en varios lugares.

## Resumen de las Relaciones

- **Herencia**: La clase `Identifier` es la base de `User`, `Place`, y `Review`.
- **Asociaciones**:
  - `User` ↔ `Review`: Un `User` puede dejar múltiples reseñas (`Review`).
  - `User` ↔ `Place`: Un `User` puede crear múltiples `Place`, pero cada `Place` pertenece a un solo `User`.
  - `Place` ↔ `Review`: Un `Place` puede tener múltiples `Review`, y cada `Review` está asociada a un solo `Place`.
  - `Place` ↔ `Amenity`: Un `Place` puede tener varios `Amenity`, y un `Amenity` puede estar asociado a varios `Place`.