import bottle, pathlib
from bottle import get, route, run, error, view, static_file

STATIC_ROOT = str(pathlib.Path(__file__).parent.absolute()) + '/static'
CSS_ROOT = STATIC_ROOT + '/css/'
JS_ROOT = STATIC_ROOT + '/js/'


# @routes
# @static css
@get('/static/css/<filepath>')
def css(filepath):
    return static_file(filepath, root=CSS_ROOT)


# @static css
@get('/static/js/<filepath>')
def css(filepath):
    return static_file(filepath, root=JS_ROOT)


# @routes-errors
@error(404)
def not_found(error):
    return 'Nothing here, sorry'


@error(500)
def server_error(error):
    return 'Server error :('


@route('/')
@view('index')
def index():
    return None


# @run app server
if __name__ == "__main__":
    # local
    run(host='localhost', port=8080)
# gunicorn
app = bottle.default_app()
