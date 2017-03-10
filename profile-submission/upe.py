#!/usr/bin/env python

# Created by Disa Mhembere on 2017-03-09.
# Email: disa@jhu.edu
# Copyright (c) 2017. All rights reserved.

from flask import Flask, request, render_template
import json, os

STORE_DIR = "submit/"

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def upe():
    if request.method == "POST":
        name = request.form["name"].split()
        img = request.files["file"]
        img.save(STORE_DIR + ("_".join(name)) + ".png")

        fn = STORE_DIR + ("_".join(name)) + ".json"
        if os.path.exists(fn):
            os.remove(fn)

        with open(fn, "wb") as f:
            json.dump(request.form, f)

        return "Submission Successful!"
    else:
        return render_template('profiles.html')

if __name__ == "__main__":
    app.run()
