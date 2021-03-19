"""
Running this application:

1. In your terminal, export the FLASK_APP environment variable.
>>> export FLASK_APP=hello_world.py

2. Run the app.
>>> flask run
- Alternatively >>> python -m flask run

3. Visit the numerical URL address on your browser.
- Note that this is a development server and not meant for deployment.
- Check here to deploy: https://flask.palletsprojects.com/en/1.1.x/deploying/

"""

from flask import Flask
app = Flask(__name__)		# __name__ can change depending on whether the app
							# is started as an app or imported as a module.
							# This tells Flask where to look for stuff.

@app.route('/')				# route() tells Flask what URL should trigger our func.
							# '/' is the root directory. You can try '/test' and
							# visit http://127.0.0.1:5000/test to see this.
def hello_world():
	return "Hello World"

"""
Tips:
- Other users on a network cannot access your server. Server is launched in debugging
mode where users can execute code on your computer. If you trust users on your network,
run this when executing the Flask app:
>>> flask run --host=0.0.0.0

This tells your OS to listen to all public IPs.

- You can enable debug mode so the server will reload itself on code changes.
Enable development features (+ debug mode) by exporting and setting the FLASK_ENV variable
before starting the server.
[NOTE: Never use the debugger on production machine as it is a security risk]
>>> export FLASK_ENV=development
>>> flask run

"""