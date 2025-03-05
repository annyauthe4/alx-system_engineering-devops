# APPLICATION SERVER
````````````````````
An application server provides its clients with access to a dynnamic content i.e the business logic.
On the contrary, the web server fulfill requests from clients for static content.
```````````

## HOW TO SERVE FLASK APPLICATIONS WITH GUNICORN AND Nginx on UBUNTU
	- Install the Components from the Ubuntu Repositories
	  $ sudo apt-get update
	  $ sudo apt-get install python3-pip python3-dev nginx

	- Create a Python Virtual Environment
	  $ sudo pip3 install virtualenv

	- Make a parent directory for the Flask project and move into it
	  $ mkdir ~/myproject && cd ~/myproject

	- Create a virtual environment to store the Flask project's Python requirements
	  $ virtualenv myprojectenv  # This will install a local copy of Python and pip into a dir called myprojectenv

	- Activate the virtual environment
	  $ source myprojectenv/bin/activate

	- Set up a Flask Application
	  (myprojectenv) $ pip install gunicorn flask

	- Now we can create a sample app
	  (myprojectenv) $ vi ~/myproject/myproject.py

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

	  - Allow Firewall on port 5000
	  (myprojectenv) $ sudo ufw allow 5000

	  - Test the Flask app
	  (myprojectenv) $ python myproject.py

## TO SET UP PRODUCTION WITH GUNICORN
  - Log in to the web server - ssh web-username@web-IP-address
  eg ssh ubuntu@35.153.67.170
  - install gunicorn and flask on the web server
  sudo apt update
  sudo apt install -y python3-pip
  sudo apt install gunicorn flask
  - clone the AirBnB_v2 on the web server
  git clone https:/www.github.com/annyauthe4/AirBnB_clone_v2

  - bind gunicorn to the flask route
  gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
