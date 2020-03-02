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
run(host='0.0.0.0', port=80)
