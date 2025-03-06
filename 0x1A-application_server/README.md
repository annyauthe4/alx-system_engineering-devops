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


## TO SERVE A PAGE USING NGINX
  - log in to the web server
  - configure the nginx configuration file
  sudo vi /etc/nginx/sites-available/config-file-name
  There in insert under server {
	  location /airbnb-onepage/ {
		  proxy_pass http:127.0.0.1:5000/;  # This ensures it is directed to Gunicorn
		  proxy_set_header Host $host;
        	  proxy_set_header X-Real-IP $remote_addr;
        	  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    	  }

  - Test nginx configuration: sudo nginx -t
  - Restart nginx: sudo nginx systemctl restart nginx
  - Then test on the terminal: curl -sI 127.0.0.1/airbnb-onepage/
  - Expected output: HTTP/1.1 200 OK ...


## CHALLENGE AND RESOLUTION
  During the cause of the configuration, the test was bringing page not found error, 404 error.
  I checked if Gunicorn was listening on port 5000: sudo lsof -i :5000
  It was listening on Port 5000. Had it not, I would start it manually:
  gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
  That was a file named 0-hello_route.py inside a web_flask directory. The app is the Flask Object.
  As gunicorn was listening on port 5000, I tested if it was serving the expected route:
  curl 127.0.0.1:5000/airbnb-onepage/
  As that was working, I tried fixing Nginx configuration file:
  sudo vi /etc/nginx/sites-available/default
  I added the lines of instruction under how to serve a page usig Nginx above.
  I tested if the configuration was successful and then restarted Nginx, then tested it on the terminal as above.
  Then check the content: curl 127.0.0.1/airbnb-onepage/
  It brought the expected output.
