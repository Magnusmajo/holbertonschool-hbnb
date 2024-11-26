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
            amenity = facade.create_amenity(data)  # llama a la fachada para crear una amenity
            return {
                'id': amenity.id,
                'name': amenity.name
                }, 201  # Return the created amenity
        except Exception as e:
            return {'error': str(e)}, 400  # Handle errors

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        # Placeholder for logic to return a list of all amenities
        amenities = facade.get_all_amenities()  # llama a la fachada para obtener las amenities
        return [
            {
                'id': amenity.id,
                'name': amenity.name
                } for amenity in amenities
                ], 200  # devuelve la lista de amenities


@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        amenity = facade.get_amenity(amenity_id)
        if amenity:
            return {
                'id': amenity.id,
                'name': amenity.name
                }, 200
        return {'error': 'Amenity not found'}, 404

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        data = api.payload
        amenity = facade.update_amenity(amenity_id, data)

        if amenity:
            return {'message': 'Amenity updated successfully'}, 200
        return {'error': 'Amenity not found'}, 404
