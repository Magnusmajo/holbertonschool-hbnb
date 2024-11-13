# Relacion entre clases

### Clase Place

Relación con User y Review

La clase `Place` se relaciona con las clases `User` y `Review` de la siguiente manera:

- **User**: Cada instancia de `Place` tiene un atributo `owner` que referencia a una instancia de `User`. Esto indica que un usuario es el propietario del lugar.
- **Review**: La clase `Place` tiene una lista de reseñas (`reviews`). Cada reseña es una instancia de la clase `Review` y contiene referencias tanto al `Place` como al `User` que escribió la reseña.

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



