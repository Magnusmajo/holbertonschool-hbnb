# User Models Requirements Verification

## One-to-Many Relationship between User and Place

- ✅ The User class has an attribute `places` which is a list to store multiple instances of Place.
- ✅ The `add_place` method in the User class adds a Place to the list and sets the owner of the Place to the User.

## User Class

- ✅ `id` (String): Inherited from BaseModel, it is a unique identifier for each user.
- ✅ `first_name` (String): Validated to be required and have a maximum length of 50 characters.
- ✅ `last_name` (String): Validated to be required and have a maximum length of 50 characters.
- ✅ `email` (String): Validated to be required, unique, and follow the standard email format.
- ✅ `is_admin` (Boolean): Optional attribute with a default value of False.
- ✅ `created_at` (DateTime): Inherited from BaseModel, timestamp when the user is created.
- ✅ `updated_at` (DateTime): Inherited from BaseModel, timestamp when the user is last updated.

--

Auth: Alexis Rodriguez