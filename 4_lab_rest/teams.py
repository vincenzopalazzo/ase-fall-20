"""
4th ASE2020 lab

@author Vincenzo Palazzo v.palazzo1@studenti.unipi.it
"""
from flask import Blueprint, jsonify

teams = Blueprint('teams', __name__)

_DEVS = ['tarek', 'Bob']
_OPS = ['Bill']
_TEAMS = {1: _DEVS, 2: _OPS}


@teams.route('/teams')
def get_all():
    return jsonify(_TEAMS)


@teams.wroute('/teams/<int:person_id>')
def get_team(person_id):
    return jsonify(_TEAMS[person_id])
