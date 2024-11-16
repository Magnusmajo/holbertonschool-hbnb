from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        data = api.payload
        try:
            amenity = facade.create_amenity(data)  # Calling the facade method
            return {'id': amenity.id, 'name': amenity.name}, 201  # Return the created amenity
        except Exception as e:
            return {'message': str(e)}, 400  # Handle errors

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        # Placeholder for logic to return a list of all amenities
        amenities = facade.get_all_amenities()  # Call the facade method
        return [{'id': amenity.id, 'name': amenity.name} for amenity in amenities], 200  # Return the list of amenities


@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        amenity = facade.get_amenity(amenity_id)  # Call the facade method
        if amenity:
            return {'id': amenity.id, 'name': amenity.name}, 200  # Return the amenity
        return {'message': 'Amenity not found'}, 404  # Handle not found

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        data = api.payload
        amenity = facade.update_amenity(amenity_id, data)  # Call the facade method
        if amenity:
            return {'message': 'Amenity updated successfully'}, 200  # Return success message
        return {'message': 'Amenity not found'}, 404  # Handle not found