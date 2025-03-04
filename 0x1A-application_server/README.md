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
