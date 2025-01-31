from flask import Blueprint, jsonify

pet_route_bp = Blueprint('pet_route_bp', __name__)

@pet_route_bp.route('/pets', methods=['GET'])
def list_pets():
    return jsonify({'message': 'Hello, pets!'}), 200
