from flask import Flask, render_template, request
import json
import traceback
from datetime import datetime
from controller import DirectorC, ActorC

from model import DirectorM

app = Flask(__name__)


@app.route(f'/api/amz/director/getAllDir', methods=['GET'])
def get_all_director():
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


@app.route(f'/api/amz/actor/getAllAct', methods=['GET'])
def get_all_actor():
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
