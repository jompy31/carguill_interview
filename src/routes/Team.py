from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.Team import Team
# Models
from models.TeamModel import TeamModel

main = Blueprint('team_blueprint', __name__)


@main.route('/')
def get_teams():
    try:
        teams = TeamModel.get_teams()
        return jsonify(teams)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>')
def get_team(id):
    try:
        team = TeamModel.get_team(id)
        if team != None:
            return jsonify(team)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_team():
    try:
        name = request.json['name']
        role = int(request.json['role'])
        released = request.json['released']
        id = uuid.uuid4()
        team = Team(str(id), name, role, released)

        affected_rows = TeamModel.add_team(team)

        if affected_rows == 1:
            return jsonify(team.id)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_team(id):
    try:
        name = request.json['name']
        role = int(request.json['role'])
        released = request.json['released']
        team = Team(id, name, role, released)

        affected_rows = TeamModel.update_team(team)

        if affected_rows == 1:
            return jsonify(team.id)
        else:
            return jsonify({'message': "No team updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_team(id):
    try:
        team = Team(id)

        affected_rows = TeamModel.delete_team(team)

        if affected_rows == 1:
            return jsonify(team.id)
        else:
            return jsonify({'message': "No team deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
