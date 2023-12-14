from flask import Flask, render_template, request
import json
import traceback
from datetime import datetime
from controller import DirectorC, ActorC, SystadminC

from model import DirectorM

app = Flask(__name__)


@app.route(f'/api/amz/director/search_dir', methods=['GET'])
def _get_all_director():
    directorc = DirectorC.Director.findDirector()

    list_director = []

    if type(directorc) == list:
        for dc in directorc:
            director = {
                "id_director": dc.getIdDirector(),
                "firstname": dc.getDirectorFirstname(),
                "lastname": dc.getDirectorLastname()
            }
            list_director.append(director)

        return {'response': list_director}
    return {'response': directorc}


@app.route(f'/api/amz/actor/search_actor', methods=['GET'])
def _search_actor():
    actorC = ActorC.Actor.findAllActor()

    list_actor = []
    if type(actorC) == list:
        for act in actorC:
            actor = {
                'id_actor': act.getActorId(),
                'firstname': act.getFirstname(),
                'lastname': act.getLastname()
            }
            list_actor.append(actor)
        return {'response': list_actor}
    return {'response': actorC}


@app.route(f'/api/amz/admin/create_user', methods=['POST'])
def _create_user():
    try:
        password = request.json.get('password')
        user = request.json.get('user')
        res = SystadminC.SystadminC.createUser(password, user)
        if res == 'ERROR':
            return {'response': f"Erreur lors de la creation de l'utilisateur {user}"}
        else:
            return {'response': res}
    except Exception as exception:
        print(f"Erreur lors de la creation d'utilisateur ::: {exception}")
        return {'response': "Internal Error Server"}


@app.route(f'/api/amz/admin/create_role', methods=['POST'])
def _create_role():
    try:
        role = request.json.get('role')
        res = SystadminC.SystadminC.createRole(role)
        if res == 'ERROR':
            return {'response': "Erreur lors de la creation de role"}
        else:
            return {'response': res}
    except Exception as exception:
        print(f"Error lors de la creation de role ::: {exception}")
        return {'response': 'Internal Error Server'}


@app.route(f'/api/amz/admin/grant_privilege', methods=['POST'])
def _attribute_privilege():
    try:
        privileges = request.json.get('privileges')
        tables = request.json.get('tables')
        roles = request.json.get('roles')
        res = SystadminC.SystadminC.attributePrivilegeRole(
            privileges, tables, roles)
        if res == 'ERROR':
            return {'response': "Erreur lors de l'attribution des privilèges"}
        else:
            return {'responses': res}

    except Exception as exception:
        print(f"Error lors de l'attribution des privilèges ::: {exception}")
        return {'response': "Internal Error Server"}


@app.route(f'/api/amz/admin/grant_role_user', methods=['POST'])
def _grand_role_user():
    try:
        user = request.json.get('user')
        role = request.json.get('role')
        res = SystadminC.SystadminC.attributeRoleUser(user, role)
        if res == 'ERROR':
            return {'response': f"Erreur lors de l'attribution des roles au user {user}"}
        else:
            return {'response': res}
    except Exception as exception:
        print(f"Erreur lors de l'attribution des roles ::: {exception}")
        return {'response': 'Internal Error Server'}
