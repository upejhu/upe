/// <reference path=".typings/node/node.d.ts"/>
var express = require("express"),
	bodyParser = require("body-parser"),
	Datastore = require("nedb"),
	multer = require("multer"),
	app = express();

// middleware to automagically parse (some) requests
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(multer( {dest: './uploads/'} ));

// db
var db = new Datastore({ filename: "db", autoload: true });

// expose things to the public
app.use(express.static("public", { root: __dirname }));

// suppy register endpoint
app.get("/register", function(req, res) {
	res.sendFile("public/register.html", { root: __dirname });
});
// callback from register 
app.post("/register", function(req, res) {
	var user = req.body.user;
	// clean up booleans
	user.alumni = user.alumni == "on" ? true : false;
	user.create_profile = user.create_profile == "on" ? true : false;
	// add image
	if (req.files.image) {
		user.image = req.files.image.name;
	}
	db.insert(user);
	res.sendFile("public/index.html", { root: __dirname });
});

// listen on port 8080
var server = app.listen(8080, function() {
	var host = server.address().address;
	if (host == "::") {
		host = "localhost" + host;
	}
	var port = server.address().port;
	console.log("server listening at http://%s%s", host, port);
});