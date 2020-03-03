import bottle
from bottle import route, run, error, view


# @routes

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
