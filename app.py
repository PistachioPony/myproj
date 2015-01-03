import os
import sys
import pymongo
from flask import Flask, render_template, send_from_directory
from os import credentials

#----------------------------------------
# initialization
#----------------------------------------
__author__ = 'mongolab'

app = Flask(__name__)

app.config.update(
    DEBUG = True,
)

MONGODB_URI = credentials.login['mongodb_uri']

#-----------------------------------------
# main
#-----------------------------------------

def main(args):

    client = pymongo.MongoClient(MONGODB_URI)

    db = client.get_default_database()

    perfumes = db['perfumes']

#----------------------------------------
# controllers
#----------------------------------------

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
    return render_template('index.html')
#----------------------------------------
# launch
#----------------------------------------

if __name__ == "__main__":
    main(sys.argv[1:])

    # below is to run it locally
    # port = int(os.environ.get("PORT", 5000))
    # app.run(host='0.0.0.0', port=port)