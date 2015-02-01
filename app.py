import os
from os import environ
import sys
import pymongo
from flask import Flask, render_template, send_from_directory
from flask.ext.stormpath import StormpathManager
import config

app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['STORMPATH_API_KEY_ID'] = environ.get('STORMPATH_API_KEY_ID')
app.config['STORMPATH_API_KEY_SECRET'] = environ.get('STORMPATH_API_KEY_SECRET')
app.config['STORMPATH_APPLICATION'] = environ.get('STORMPATH_URL')

#----------------------------------------
# initialization
#----------------------------------------
__author__ = 'mongolab'

app = Flask(__name__)

stormpath_manager = StormpathManager(app)

app.config.update(
    DEBUG = True,
)

MONGODB_URI = config.development.login

#----------------------------------------
# controllers
#----------------------------------------

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

@app.route("/")
def index():
  client = pymongo.MongoClient(MONGODB_URI)

  db = client.get_default_database()

  perfumes = db['perfumes']

  example = perfumes.find_one({"name":"888"})

  context = {'example': example}
  
  return render_template('index.html', **context)
  
#----------------------------------------
# launch
#----------------------------------------
# client.close()


if __name__ == '__main__':
    # main(sys.argv[1:])

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)