from flask import Flask, render_template, request
import json
import traceback
from datetime import datetime
from controller import DirectorC

from model import DirectorM

app = Flask(__name__)


@app.route(f'/api/amz/director/getAllDir', methods=['GET'])
def get_all_actor():
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
