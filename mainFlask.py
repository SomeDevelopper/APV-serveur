from flask import Flask, render_template, request
import json
import traceback
from datetime import datetime
from controller import DirectorC, ActorC, MovieC, SystadminC, MovieDirectorC

from model import DirectorM, ActorM, MovieM

app = Flask(__name__)

# DIRECTOR


@app.route(f'/api/amz/director/search_dir', methods=['GET'])
def _get_all_director():
    '''
        Get all information for director
    '''
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


@app.route('/api/amz/director/search_director', methods=['GET'])
def _search_director():
    '''
        Search director by id in database
    '''
    id_director = request.json.get('id_director')
    directC = DirectorC.Director.searchDirector(id_director)
    if type(directC) == DirectorM.Director:
        res = {
            "id_director": directC.getIdDirector(),
            "firstname": directC.getDirectorFirstname(),
            "lastname": directC.getDirectorLastname()
        }
        return {'response': res}
    if directC == 'ERROR':
        return {'response': 'Erreur, aucun director trouvé'}


@app.route(f'/api/amz/director/search_with_name', methods=['GET'])
def _search_director_name():
    '''
        Search director by name in database
    '''
    name_director = request.json.get('name_director')
    directC = DirectorC.Director.search_director_by_name(name_director)
    list_director = []
    if type(directC) == list:
        for dc in directC:
            director = {
                "id_director": dc.getIdDirector(),
                "firstname": dc.getDirectorFirstname(),
                "lastname": dc.getDirectorLastname()
            }
            list_director.append(director)
        return {'response': list_director}
    if directC == 'ERROR':
        return {'response': 'Erreur, aucun director trouvé'}

# ACTOR


@app.route(f'/api/amz/actor/get_all_actor', methods=['GET'])
def _get_all_actor():
    '''
        Get all actor from database
    '''
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


@app.route(f'/api/amz/actor/search_actor', methods=['GET'])
def _search_actor():
    '''
        Search one specific actor from database
    '''
    id_actor = request.json.get('id_actor')
    actorC = ActorC.Actor.searchActor(id_actor)
    if type(actorC) == ActorM.Actor:
        res = {
            "id_actor": actorC.getActorId(),
            "firstname": actorC.getFirstname(),
            "lastname": actorC.getLastname()
        }
        return {'response': res}
    if actorC == 'ERROR':
        return {'response': 'Erreur, aucune valeur trouver'}


@app.route(f'/api/amz/actor/search_with_name', methods=['GET'])
def _search_actor_with_name():
    '''
        Get all movie with filter title from database
    '''
    pattern = request.json.get('name')
    actorC = ActorC.Actor.search_actor_by_title(pattern)

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
    if actorC == 'ERROR':
        return {'response': 'Erreur, aucun acteur trouvé'}

# MOVIE


@app.route(f'/api/amz/movie/search_movie', methods=['GET'])
def _search_movie():
    '''
        Search one specific movie from database
    '''
    id_movie = request.json.get('id_movie')
    movieC = MovieC.Movie.searchMovie(id_movie)
    if type(movieC) == MovieM.Movie:
        res = {
            "id_movie": movieC.getMovieId(),
            "title": movieC.getMovieName(),
            "year_movie": movieC.getMovieYear(),
            "rank": movieC.getMovieRank()
        }
        return {'response': res}
    if movieC == 'ERROR':
        return {'response': 'Erreur, aucune valeur trouver'}


@app.route(f'/api/amz/movie/get_all_movie', methods=['GET'])
def _get_all_movie():
    '''
        Get all movie from database
    '''
    movieC = MovieC.Movie.get_all_movie()

    list_movie = []
    if type(movieC) == list:
        for mv in movieC:
            movie = {
                "id_movie": mv.getMovieId(),
                "title": mv.getMovieName(),
                "year_movie": mv.getMovieYear(),
                "rank": mv.getMovieRank()
            }
            list_movie.append(movie)
        return {'response': list_movie}
    if movieC == 'ERROR':
        return {'response': 'Erreur, aucun film trouvé'}


@app.route(f'/api/amz/movie/search_with_title', methods=['GET'])
def _search_movie_with_title():
    '''
        Get all movie with filter title from database
    '''
    pattern = request.json.get('title')
    movieC = MovieC.Movie.search_movie_by_title(pattern)

    list_movie = []
    if type(movieC) == list:
        for mv in movieC:
            movie = {
                "id_movie": mv.getMovieId(),
                "title": mv.getMovieName(),
                "year_movie": mv.getMovieYear(),
                "rank": mv.getMovieRank()
            }
            list_movie.append(movie)
        return {'response': list_movie}
    if movieC == 'ERROR':
        return {'response': 'Erreur, aucun film trouvé.'}


@app.route(f'/api/amz/movie/get_infos_movie', methods=['GET'])
def _get_all_infos_movie():
    '''
        Get all information for one movie from database
    '''
    colonne_name = request.json.get('colonne_name')
    id_value = request.json.get('id_value')
    pattern = [colonne_name, id_value]
    mdC = MovieDirectorC.MovieDirector.get_movie_director(pattern)
    if mdC == 'ERROR':
        return {"response": "Errur lors de la récupération de données"}
    if mdC:
        id_movie_res = mdC.getMovieId()
        id_director_res = mdC.getDirectorId()
        mC = MovieC.Movie.searchMovie(id_movie_res)
        dC = DirectorC.Director.searchDirector(id_director_res)
        if (dC == 'ERROR') or (mC == 'ERROR'):
            return {"response": "Errur lors de la récupération de données"}
        if mC and dC:
            res = {
                "id_movie": mC.getMovieId(),
                "title": mC.getMovieName(),
                "year_movie": mC.getMovieYear(),
                "rank": mC.getMovieRank(),
                "id_director": dC.getIdDirector(),
                "director": f'{dC.getDirectorFirstname()} {dC.getDirectorLastname()}'
            }
            return {'response': res}


# Custom REQUEST FROM CLASS

@app.route(f'/api/amz/request/get_rank_average_by_year', methods=['GET'])
def _get_average_rank_year():
    '''
        Get average movie's rank for specific year from database
    '''
    year = request.json.get('year')
    movieC = MovieC.Movie.get_average_movie_rank_with_year(year)
    if movieC == 'ERROR':
        return {"response": "Erreur lors du classement moyen."}
    if movieC:
        return {"response": f"Le classement moyen pour l'annnée {year} est {movieC[0]}"}


# ADMIN
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
