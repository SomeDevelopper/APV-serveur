from flask import Flask, render_template, request
import json
import traceback
from datetime import datetime
from controller import DirectorC, ActorC, MovieC, SystadminC, MovieDirectorC, RoleC, DirectorGenreC, MovieGenreC

from model import DirectorM, ActorM, MovieM, RoleM, MovieDirectorM, MovieGenreM, DirectorGenreM

app = Flask(__name__)

# DIRECTOR


@app.route(f'/api/amz/director/get_all_director', methods=['GET'])
def _get_all_director():
    '''
        Get all information for director
    '''
    directorc = DirectorC.Director.get_all_director()

    list_director = []

    if type(directorc) == list:
        for dc in directorc:
            director = {
                "id_director": dc.getid_director(),
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
            "id_director": directC.getid_director(),
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
                "id_director": dc.getid_director(),
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

    id_movie = request.json.get('id_movie')
    mdC = MovieDirectorC.MovieDirector.get_movie_director(id_movie)
    if mdC == 'ERROR':
        return {"response": "Erreur lors de la récupération de données"}
    if mdC:
        id_movie_res = mdC.getMovieId()
        id_director_res = mdC.getDirectorId()
        mC = MovieC.Movie.searchMovie(id_movie_res)
        dC = DirectorC.Director.searchDirector(id_director_res)
        if (dC == 'ERROR') or (mC == 'ERROR'):
            return {"response": "Erreur lors de la récupération de données"}
        if mC and dC:
            res = {
                "id_movie": mC.getMovieId(),
                "title": mC.getMovieName(),
                "year_movie": mC.getMovieYear(),
                "rank": mC.getMovieRank(),
                "id_director": dC.getid_director(),
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
        return {"response": f"Le classement moyen pour l'annnée {year} est de {movieC[0]}"}

@app.route(f'/api/amz/actor/get_ntile', methods=['GET'])
def _get_ntile_actor():
    aC = ActorC.Actor.get_ntile_actor()
    if type(aC) == list:
        list_actor_group = []
        for a in aC:
            res = {
                'id_actor': a[0],
                'firstname': a[1],
                'lastname': a[2],
                'groupe': a[3]
            }
            list_actor_group.append(res)
        return {"response": list_actor_group}
    if aC == 'ERROR':
        return {'response': 'Erreur lors du groupage des acteurs'}

@app.route(f'/api/amz/movie/get_case_movie', methods=['GET'])
def _get_case_movie():
    mC = MovieC.Movie.get_case_movie()
    if mC == 'ERROR':
        return {'reponse': 'Erreur lors de la récupération de données'}
    else:
        list_res_case = []
        for r in mC:
            res = {
                'id_movie': r[0],
                'title': r[1],
                'year_movie': r[2],
                'rank': r[3],
                'Evaluation': r[4]
            }
            list_res_case.append(res)
        return {'response': list_res_case}

@app.route(f'/api/amz/request/get_initiale', methods=['GET'])
def _get_initiale():
    start = request.json.get('start')
    nb_letter = request.json.get('nb_letter')
    r = DirectorC.Director.get_initiale(start, nb_letter)
    if r == 'ERROR':
        return {'response': "Une erreur s'est produite"}
    else:
        list_d_init = []
        for d in r:
            res = {
                'id_actor': d[0],
                'firstname': d[1],
                'lastname': d[2],
                'initiale': d[3]
            }
            list_d_init.append(res)
        return {'response': list_d_init}

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

@app.route(f'/api/amz/admin/insert_movie', methods=['POST'])
def _insert_movie():
    try:
        req = request.json
        m = MovieM.Movie()
        m.setMovieId(req.get('id_movie'))
        m.setMovieName(req.get('name'))
        m.setMovieYear(req.get('year_movie'))
        m.setMovieRank(req.get('rank'))
        a = ActorM.Actor()
        a.setActorId(req.get('id_actor'))
        a.setFirstname(req.get('firstname_a'))
        a.setLastname(req.get('lastname_a'))
        d = DirectorM.Director()
        d.setid_director(req.get('id_director'))
        d.setDirectorFirstname(req.get('firstname_d'))
        d.setDirectorLastname(req.get('lastname_d'))
        dg = DirectorGenreM.DirectorGenre()
        dg.setDirectorId(req.get('id_director'))
        dg.setGenre(req.get('genre'))
        md = MovieDirectorM.MovieDirector()
        md.setDirectorId(req.get('id_director'))
        md.setMovieId(req.get('id_movie'))
        mg = MovieGenreM.MovieGenre()
        mg.setMovieId(req.get('id_movie'))
        mg.setGenre(req.get('genre'))
        r = RoleM.Role()
        r.setMovieId(req.get('id_movie'))
        r.setActorId(req.get('id_actor'))
        r.setRole(req.get('role'))
        mC = MovieC.Movie.insert_data(m)
        aC = ActorC.Actor.insert_data(a)
        dC = DirectorC.Director.insert_data(d)
        dgC = DirectorGenreC.DirectorGenre.insert_data(dg)
        mdC = MovieDirectorC.MovieDirector.insert_data(md)
        mgC = MovieGenreC.MovieGenre.insert_data(mg)
        rC = RoleC.Role.insert_data(r)
        if (dC == 'ERROR') or (mC == 'ERROR') or (aC == 'ERROR') or (dgC == 'ERROR') or (mgC == 'ERROR') or (mdC == 'ERROR') or (rC  == 'ERROR'):
            return {"response": "Erreur lors de la récupération de données"}
        if mC and aC and dC and dgC and mdC and mgC and rC:
            return {"response": "Informations ajoutées"}
    except Exception as exception:
        print(f"Erreur lors de l'insertion de données ::: {exception}")
        return {'response': 'Internal Error Server'}