from flask import Blueprint, jsonify, request
import uuid

#Entities
from models.entitys.criatura import Criatura
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
    
@main.route('/id/<id>')
def getCriaturaById(id):
    try:
        criatura = CriaturaModel.getById(id)
        if criatura != None:
            return jsonify(criatura)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'mensaje': str(ex)}), 500
    
@main.route('/add', methods=['POST'])
def addCriatura():
    try: #Se podría realizar la validación de datos
        
        id = uuid.uuid4()
        name = request.json['name']
        image = request.json['image']
        description = request.json['description']
        location = request.json['location']
        drops = request.json['drops']
        
        criatura = Criatura(str(id), name, image, description, location, drops)
        
        affected_rows = CriaturaModel.addCriatura(criatura)
        
        if affected_rows == 1:
            return jsonify(criatura.id)
        else:
            return jsonify({'message': 'Error al añadir el elemento'}), 500
            
    except Exception as ex:
        return jsonify({'mensaje': str(ex)}), 500
    
@main.route('/delete/<id>', methods=['DELETE'])
def deleteCriatura(id):
    try: #Se podría realizar la validación de datos
        
        criatura = Criatura(id)
        
        affected_rows = CriaturaModel.deleteCriatura(criatura)
        
        if affected_rows == 1:
            return jsonify(criatura.id)
        else:
            return jsonify({'message': 'No se pudo borrar la película'}), 404
            
    except Exception as ex:
        return jsonify({'mensaje': str(ex)}), 500
    
@main.route('/update/<id>', methods=['PUT'])
def updateCriatura(id):
    try: #Se podría realizar la validación de datos
        
        name = request.json['name']
        image = request.json['image']
        description = request.json['description']
        location = request.json['location']
        drops = request.json['drops']
        
        criatura = Criatura(id, name, image, description, location, drops)
        
        affected_rows = CriaturaModel.updateCriatura(criatura)
        
        if affected_rows == 1:
            return jsonify(criatura.id)
        else:
            return jsonify({'message': 'Error al editar el elemento'}), 404
            
    except Exception as ex:
        return jsonify({'mensaje': str(ex)}), 500