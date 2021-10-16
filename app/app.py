from flask import Flask, render_template, request, abort, redirect
from flask.helpers import url_for
import config
import pymongo
import random

app = Flask(__name__)
mongo_cluster = pymongo.MongoClient(config.mongo_db_url)
db = mongo_cluster["projects"]
col = db['urls']


@app.route("/", methods=['GET', 'POST'])
def hello():
    rand_picked = random.randrange(1, 10000)
    url = request.form.get("URL")
    aaaaa_pain = {
        "_id": rand_picked,
        "url": url
    }

    try:
        col.insert_one(aaaaa_pain)
    except Exception:
        aaaaa_pain["_id"] = rand_picked = random.randrange(1, 10000)
        col.insert_one(aaaaa_pain)
    

    rand_picked_url = f"localhost:5000/url/{rand_picked}"
    return render_template("index.html", rand_picked=rand_picked, rand_picked_url=rand_picked_url)


@app.route("/url/<int:url_id>")
def sh_url(url_id):
    val = col.find({"_id": url_id})
    if not val:
        return abort(404)
    
    v = val[0]
    _url = v.get("url")

    return redirect(_url)


def run():
    app.run(debug=True)
