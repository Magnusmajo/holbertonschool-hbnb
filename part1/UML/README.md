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



  # Diagrama de Capas del Sistema

Este diagrama muestra la arquitectura del sistema dividiéndolo en tres capas principales: Capa de Presentación, Capa de Lógica de Negocio, y Capa de Persistencia. Cada una de estas capas tiene responsabilidades específicas y se comunica con las demás a través de interfaces definidas.

## Descripción de las Capas

### 1. Capa de Presentación (Presentation Layer)
- **Descripción**: Es la capa encargada de la interacción con el usuario. Proporciona los elementos visuales y los puntos de acceso que permiten a los usuarios interactuar con el sistema.
- **Componentes**:
  - **User Interface (Interfaz de Usuario)**: Maneja la presentación de la información y la interacción directa con el usuario.
  - **API Endpoints**: Expone los endpoints de la API que permiten que otras aplicaciones o servicios interactúen con el sistema a través de solicitudes HTTP.
- **Relación**: La Capa de Presentación tiene acceso a la Capa de Lógica de Negocio, lo que permite que las interacciones de los usuarios se traduzcan en operaciones dentro de la lógica de negocio.

### 2. Capa de Lógica de Negocio (Business Logic Layer)
- **Descripción**: Es la capa central del sistema donde se implementa la lógica de negocio. Esta capa actúa como un intermediario entre la capa de presentación y la capa de persistencia, gestionando las operaciones principales del sistema.
- **Componentes**:
  - **Facade Pattern (Patrón de Fachada)**: Sirve como interfaz simplificada para la interacción con la lógica de negocio. Facilita el acceso a las funcionalidades de negocio sin exponer la complejidad interna.
  - **Core Logic (Lógica Central)**: Contiene la lógica y reglas de negocio del sistema. Aquí se procesan y ejecutan las operaciones principales que siguen las reglas definidas por la empresa.
  - **Business Entities (Entidades de Negocio)**: Representa los objetos principales que intervienen en la lógica de negocio, como usuarios, lugares, reseñas, y amenidades. Estas entidades encapsulan los atributos y comportamientos necesarios para el negocio.
- **Relación**: 
  - La Capa de Lógica de Negocio se comunica con la Capa de Persistencia para almacenar o recuperar datos.
  - El **Patrón de Fachada** accede tanto a la **Lógica Central** como a las **Entidades de Negocio** para proporcionar una interfaz simplificada hacia la lógica del sistema.

### 3. Capa de Persistencia (Persistence Layer)
- **Descripción**: Esta capa se encarga del almacenamiento de datos en el sistema. Asegura que los datos persistan y puedan ser recuperados cuando sea necesario.
- **Componentes**:
  - **Database Storage (Almacenamiento de Base de Datos)**: Es el componente responsable de la persistencia de datos. Puede estar compuesto por bases de datos relacionales, no relacionales, o cualquier sistema de almacenamiento que permita guardar la información estructurada del sistema.
- **Relación**: La Capa de Persistencia es accedida por la Capa de Lógica de Negocio para realizar operaciones de almacenamiento y recuperación de datos. No interactúa directamente con la Capa de Presentación.

## Flujo de Interacción Entre Capas

1. **Interacción del Usuario**: Los usuarios interactúan con el sistema a través de la **Interfaz de Usuario** en la Capa de Presentación.
2. **Acceso a la Lógica de Negocio**: Las solicitudes del usuario son enviadas a través de los **API Endpoints** a la Capa de Lógica de Negocio, donde el **Patrón de Fachada** gestiona la interacción.
3. **Procesamiento de la Lógica Central**: El **Patrón de Fachada** delega las solicitudes a la **Lógica Central** y utiliza las **Entidades de Negocio** para procesar las operaciones.
4. **Acceso a la Persistencia**: La Capa de Lógica de Negocio se comunica con la Capa de Persistencia para almacenar o recuperar datos según las operaciones realizadas.
5. **Respuesta al Usuario**: Los resultados son enviados de vuelta a la Capa de Presentación, donde se muestran al usuario a través de la **Interfaz de Usuario**.
