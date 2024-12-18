from flask_restx import Namespace, Resource, fields
# from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade

api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    # 'owner': fields.Nested(user_model, description='Owner of the place'),
    # 'amenities': fields.List(fields.String, required=True, description="List of amenities ID's"),
    # 'reviews': fields.List(fields.String, required=True, description="List of reviews ID's")
})

# Adding the review model
review_model = api.model('PlaceReview', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Text of the review'),
    'rating': fields.Integer(description='Rating of the place (1-5)'),
    'user_id': fields.String(description='ID of the user')
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    # @jwt_required()
    def post(self):
        """Register a new place"""
        # current_user = get_jwt_identity()
        data = api.payload
        try:
            place = facade.create_place(data)
            return {
                'id': place.id,
                'title': place.title,
                'price': place.price,
                'latitude': place.latitude,
                'longitude': place.longitude,
                'owner_id': place.owner_id
                }, 201
        except Exception as e:
            return {'error': str(e)}, 400
    
    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        places = facade.get_all_places()
        return [
            {
                'id': place.id,
                'title': place.title,
                'price': place.price,
                'latitude': place.latitude,
                'longitude': place.longitude
                } for place in places
                ], 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        try:
            place = facade.get_place(place_id)
            if not place:
                return {'error': 'Place not found'}, 404
            
            return {
                'id': place.id if place.id else None,
                'title': place.title if place.title else None,
                'description': place.description if place.description else None,
                'latitude': place.latitude if place.latitude else None,
                'longitude': place.longitude if place.longitude else None,
                'owner': {
                    'id': place.owner.id if place.owner and place.owner.id else None,
                    'first_name': place.owner.first_name if place.owner and place.owner.first_name else None,
                    'last_name': place.owner.last_name if place.owner and place.owner.last_name else None,
                    'email': place.owner.email if place.owner and place.owner.email else None
                } if place.owner else None,
                'amenities': [{
                    'id': amenity.id,
                    'name': amenity.name
                } for amenity in place.amenities] if place.amenities else []
            }, 200
        except Exception as e:
            return {'error': str(e)}, 500


    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Unauthorized action')
    # @jwt_required()
    def put(self, place_id):
        """Update a place's information"""
        # current_user = get_jwt_identity()
        data = api.payload
        place = facade.update_place(place_id, data)
        if place:
            return {'message': 'Place updated successfully'}, 200
        return {'error': 'Place not found'}, 404
