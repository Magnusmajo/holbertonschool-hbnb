# Relacion entre clases

### Clase Place

Relación con User y Review

La clase `Place` se relaciona con las clases `User` y `Review` de la siguiente manera:

- **User**: Cada instancia de `Place` tiene un atributo `owner` que referencia a una instancia de `User`. Esto indica que un usuario es el propietario del lugar.
- **Review**: La clase `Place` tiene una lista de reseñas (`reviews`). Cada reseña es una instancia de la clase `Review` y contiene referencias tanto al `Place` como al `User` que escribió la reseña.
- Utilizamos el metodo < add_review > para agregar una reseña y asegurarnos de que se sepa a cual lugar pertenece., lo mismo funciona con las < amenities >

#### Ejemplo de Relación

```python
from app.models.user import User
from app.models.place import Place
from app.models.review import Review

def main():
    # Crear instancias de User y Place
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    place = Place(title="Lovely Cottage", description="A charming place to stay.", price=100.0, latitude=50.0, longitude=-0.1, owner=user)

    # Crear instancias de Review
    review1 = Review(text="Amazing experience!", rating=5, place=place, user=user)
    review2 = Review(text="Very comfortable stay.", rating=4, place=place, user=user)

    # Agregar reseñas al lugar
    place.add_review(review1)
    place.add_review(review2)

    # Ver los resultados
    print(place.reviews)  # Debería mostrar las reseñas asociadas al lugar
    print(review1.place)  # Debería mostrar el lugar asociado a la reseña
    print(review2.place)  # Debería mostrar el lugar asociado a la reseña

if __name__ == '__main__':
    main()
```

En este ejemplo, un `User` crea un `Place` y luego escribe `Review`s para ese lugar. Las reseñas se agregan al lugar utilizando el método `add_review`, que también establece la referencia del lugar en cada reseña.


### Clase Review

Cómo Funciona la Relación

Instancia de Place: Cuando creas una instancia de Place, puedes agregarle múltiples reseñas utilizando el método add_review.

Referencias Mutuas: El método add_review en la clase Place no solo agrega una Review a la lista de reseñas del lugar, sino que también establece el lugar de esa Review al Place correspondiente. Esto asegura que ambas entidades están al tanto de su relación.

Ejemplo Práctico
-------------------------------------------

from app.models.user import User
from app.models.place import Place
from app.models.review import Review

def main():
    # Crear instancias de User y Place
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    place = Place(title="Lovely Cottage", description="A charming place to stay.", price=100.0, latitude=50.0, longitude=-0.1, owner=user)

    # Crear instancias de Review
    review1 = Review(text="Amazing experience!", rating=5, place=place, user=user)
    review2 = Review(text="Very comfortable stay.", rating=4, place=place, user=user)

    # Agregar reseñas al lugar
    place.add_review(review1)
    place.add_review(review2)

    # Ver los resultados
    print(place.reviews)  # Debería mostrar las reseñas asociadas al lugar
    print(review1.place)  # Debería mostrar el lugar asociado a la reseña
    print(review2.place)  # Debería mostrar el lugar asociado a la reseña

if __name__ == '__main__':
    main()
-----------------------------------------
Resumen
Lugar (Place): Tiene una lista de reseñas (reviews).

Reseña (Review): Tiene atributos place y user para referenciar al lugar y al usuario.

Método add_review: Añade una reseña al lugar y establece el lugar de la reseña.


### Clase User

Relación con Place y Review

La clase `User` se relaciona con las clases `Place` y `Review` de la siguiente manera:

- **Place**: Cada instancia de `User` puede ser propietaria de múltiples instancias de `Place`. Esto se indica mediante el atributo `owner` en la clase `Place`, que referencia a una instancia de `User`.
- **Review**: Cada instancia de `User` puede escribir múltiples reseñas (`Review`). Cada reseña contiene una referencia al `User` que la escribió y al `Place` que está siendo reseñado.

#### Ejemplo de Relación
-----------------------------
```python
from app.models.user import User
from app.models.place import Place
from app.models.review import Review

def main():
    # Crear instancias de User y Place
    user = User(first_name="Jane", last_name="Doe", email="jane.doe@example.com")
    place = Place(title="Cozy Apartment", description="A nice place to relax.", price=80.0, latitude=40.0, longitude=-3.7, owner=user)

    # Crear instancias de Review
    review1 = Review(text="Great location!", rating=5, place=place, user=user)
    review2 = Review(text="Very clean and tidy.", rating=4, place=place, user=user)

    # Agregar reseñas al lugar
    place.add_review(review1)
    place.add_review(review2)

    # Ver los resultados
    print(user.places)  # Debería mostrar los lugares asociados al usuario
    print(user.reviews)  # Debería mostrar las reseñas escritas por el usuario

if __name__ == '__main__':
    main()
----------------------------------------
```

En este ejemplo, un `User` crea un `Place` y luego escribe `Review`s para ese lugar. Las reseñas se agregan al lugar utilizando el método `add_review`, y el usuario es referenciado tanto en el lugar como en las reseñas.
