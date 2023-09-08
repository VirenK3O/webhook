# import flask dependencies
from flask import Flask, request, make_response, jsonify
from flask_ngrok import run_with_ngrok

# initialize the flask app
app = Flask(__name__)
run_with_ngrok(app)

# default route
@app.route('/')
def index():
	return 'Hello World!'

# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)

    # Check if 'queryResult' is present in the request JSON
    if 'queryResult' in req:
        # fetch action from json
        action = req['queryResult'].get('action')

        # Return a fulfillment response
        return {'fulfillmentText': 'This is a response from webhook.'}
    else:
        # If 'queryResult' is not present in the request JSON, return an error response
        return {'fulfillmentText': 'Invalid request. Missing queryResult field.'}

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
	# return response
	return make_response(jsonify(results()))

# run the app
if __name__ == '__main__':
	app.run()
