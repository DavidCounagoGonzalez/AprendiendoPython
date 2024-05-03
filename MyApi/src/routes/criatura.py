from flask import Blueprint, jsonify

#Models
from models.criatura_model import CriaturaModel

main = Blueprint('criatura_blueprint', __name__)

@main.route('/')
def get_criaturas():
    try:
        criaturas = CriaturaModel.get_criaturas()
        return jsonify(criaturas)
    except Exception as ex:
        return jsonify({'mensaje': str(ex)}), 500
    
@main.route('/<name>')
def getCriaturaByName(name):
    try:
        name = name.capitalize()
        print(name)
        criaturas = CriaturaModel.getByName(name)
        return jsonify(criaturas)
    except Exception as ex:
        return jsonify({'mensaje': str(ex)}), 500