import bottle
import pathlib
from bottle import get, route, run, error, view, static_file
from api.app import api

STATIC_ROOT = str(pathlib.Path(__file__).parent.absolute()) + '/static'
CSS_ROOT = STATIC_ROOT + '/css/'
JS_ROOT = STATIC_ROOT + '/js/'


# @routes
# @static css
@get('/static/css/<filepath>')
def css(filepath):
    return static_file(filepath, root=CSS_ROOT)


# @static js
@get('/static/js/<filepath>')
def js(filepath):
    return static_file(filepath, root=JS_ROOT)


# @routes-errors
@error(404)
@view('404')
def not_found(error):
    pass


@error(500)
@view('500')
def server_error(error):
    pass


@route('/')
@view('index')
def index():
    pass


# @run app server
if __name__ == "__main__":
    # local
    app = bottle.default_app()
    app.merge(api)
    app.run(host='localhost', port=8080)
# gunicorn
app = bottle.default_app()
app.merge(api)
