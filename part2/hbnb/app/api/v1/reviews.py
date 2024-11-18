from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self):
        """Register a new review"""
        data = api.payload # Get the JSON data from the request
        try:
            review = facade.create_review(data)
            return review, 201
        except ValueError as e:
            api.abort(400, str(e))
            user_id = get_jwt_identity()  # Get the ID of the authenticated user

            # Check if the place belongs to the user
            place = facade.get_place_by_id(data['place_id'])
            if place.owner_id == user_id:
                api.abort(400, 'You cannot review your own place.')

            # Check if the user has already reviewed the place
            existing_review = facade.get_review_by_user_and_place(user_id, data['place_id'])
            if existing_review:
                api.abort(400, 'You have already reviewed this place.')
    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        reviews = facade.get_all_reviews()
        return reviews, 200

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        try:
            review = facade.get_review_by_id(review_id)
            if review:
                return review, 200
            api.abort(404, 'Review not found')
        except ValueError as e:
            api.abort(400, str(e))

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Unauthorized action')
    @jwt_required()
    def put(self, review_id):
        """Update a review's information"""
        data = api.payload
        user_id = get_jwt_identity()  # Get the ID of the authenticated user
        try:
            review = facade.get_review_by_id(review_id)
            if not review:
                api.abort(404, 'Review not found')
            
            if review.user_id != user_id:
                api.abort(403, 'Unauthorized action')
            
            updated_review = facade.update_review(review_id, data)
            return updated_review, 200
        except ValueError as e:
            api.abort(400, str(e))

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    @jwt_required()
    def delete(self, review_id):
        """Delete a review"""
        try:
            result = facade.delete_review(review_id)
            if result:
                return {'message': 'Review deleted successfully'}, 200
            api.abort(404, 'Review not found')
        except ValueError as e:
            api.abort(400, str(e))
            user_id = get_jwt_identity()  # Get the ID of the authenticated user
            try:
                review = facade.get_review_by_id(review_id)
                if not review:
                    api.abort(404, 'Review not found')
                    
                if review.user_id != user_id:
                    api.abort(403, 'Unauthorized action')
                    
                result = facade.delete_review(review_id)
                if result:
                    return {'message': 'Review deleted successfully'}, 200
                api.abort(404, 'Review not found')
            except ValueError as e:
                api.abort(400, str(e))

@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place"""
        try:
            reviews = facade.get_reviews_by_place_id(place_id)
            if reviews:
                return reviews, 200
            api.abort(404, 'Place not found')
        except ValueError as e:
            api.abort(400, str(e))
