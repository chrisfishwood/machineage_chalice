from chalice import Chalice
import pprint
import json

app = Chalice(app_name='machineage_chalice')


@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/', methods=['POST'], content_types=['application/json'])
def message():
    pp = pprint.PrettyPrinter(indent=4)
    body = app.current_request.json_body
    headers = app.current_request.headers
    print("====================")
    print(body)
    print(app.current_request.to_dict())
    print("====================")
    #return app.current_request.to_dict()
    return {"headers":body["Hi"]}


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
