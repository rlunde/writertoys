from flask import jsonify, request

from . import api
from .. import db
from ..models.names import Names
from ..schemas.names import names_schema, names_schema


@api.route('/names', methods=['GET'])
def get_names():
    pass


@api.route('/names/<int:id>', methods=['GET'])
def get_names(id):
    pass


@api.route('/names', methods=['POST'])
def create_names():
    pass


@api.route('/names/<int:id>', methods=['PUT'])
def update_names(id):
    pass


@api.route('/names/<int:id>', methods=['DELETE'])
def delete_names(id):
    pass
