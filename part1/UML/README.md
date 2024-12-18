# Diagrama de Clases de HBNB

![img](https://github.com/user-attachments/assets/0d034769-76d2-4b23-abcc-9ddc4aa50139)

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

# Diagramas de Secuencia

Este documento describe los flujos de interacción representados en los diagramas de secuencia. Cada diagrama ilustra cómo los componentes de un sistema interactúan para realizar una funcionalidad específica.

---

## 1. Registro de Usuario

### Descripción:
Este diagrama muestra el flujo para registrar un nuevo usuario en el sistema.

1. **Usuario**: Envía una solicitud de registro con su nombre, correo electrónico y contraseña.
2. **API**: Valida el formato de los datos y los envía a la capa de lógica de negocio.
3. **Lógica de Negocio**:
   - Verifica si el correo electrónico ya está registrado.
   - Si el correo no está registrado, guarda los datos en la base de datos y confirma el registro.
   - Si el correo ya está registrado, devuelve un mensaje de error.
4. **Base de Datos**: Interactúa para comprobar y almacenar los datos del usuario.

### Resultado:
El usuario recibe una respuesta de éxito o error dependiendo de si el correo electrónico ya estaba registrado.

---

## 2. Solicitud de Lista con Filtros

### Descripción:
Este diagrama describe el flujo para obtener una lista de lugares basada en filtros específicos.

1. **Usuario**: Envía una solicitud con los filtros deseados.
2. **API**: Valida los filtros y envía la solicitud a la lógica de negocio.
3. **Lógica de Negocio**: Realiza una consulta en la base de datos utilizando los filtros.
4. **Base de Datos**: Devuelve los resultados que coinciden con los filtros.
5. **API**: Procesa los resultados y los devuelve al usuario.

### Resultado:
El usuario recibe una lista de lugares que cumplen con los filtros proporcionados.

---

## 3. Envío de Reseña

### Descripción:
Este diagrama muestra el flujo para enviar y guardar una reseña de un lugar.

1. **Usuario**: Envía los datos de la reseña.
2. **API**: Valida los datos y los pasa a la lógica de negocio.
3. **Lógica de Negocio**:
   - Verifica si el lugar existe en la base de datos.
   - Confirma que el usuario tiene permisos para realizar la reseña.
   - Guarda la reseña en la base de datos.
4. **Base de Datos**: Almacena los datos de la reseña.
5. **API**: Envía una confirmación de éxito o un mensaje de error al usuario.

### Resultado:
El usuario recibe una confirmación del registro exitoso de la reseña o un mensaje de error si hubo algún problema.

---

## 4. Creación de Lugar

### Descripción:
Este diagrama muestra el flujo para crear un nuevo lugar en el sistema, donde un usuario envía información sobre el lugar a través de la API.

### Flujo de interacción:

1. *Usuario*: Envía los datos del lugar (nombre, ubicación y precio) al sistema.
2. *API*: Realiza la validación del formato de los datos y verifica la autenticación del usuario.
3. *Lógica de Negocio*:
   - Verifica que el usuario tenga permisos necesarios y que se cumplan las reglas de negocio para la creación del lugar.
   - Si todo es correcto, envía los datos del lugar a la base de datos para guardarlos.
4. *Base de Datos*:
   - Guarda los datos del lugar.
   - Confirma el registro del lugar.
5. *Lógica de Negocio*: 
   - Recibe la confirmación de que el lugar ha sido registrado con éxito y envía una respuesta de éxito.
6. *API*: Procesa la respuesta de éxito y devuelve los detalles del lugar creado al usuario.

### Resultado:
El usuario recibe los detalles del lugar creado y la confirmación de que el registro se ha completado con éxito.

---