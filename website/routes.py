from website import flaskApp, db#, cache
import flask
from flask import render_template, send_from_directory, request, jsonify, make_response
from flask_cache import Cache
import random
from .database import Dbase
import time

import json

quantity = 10
postNum = Dbase.numPosts()
if postNum < quantity:
    quantity = postNum    


@flaskApp.route("/", methods=['GET', 'POST'])
@flaskApp.route("/index", methods=['GET', 'POST'])
#@cache.cached(timeout=60)
def index():
#    if request.method == 'POST':
    title = {'title': 'Home'}
    return render_template("index.html", title=title)


@flaskApp.route("/load")
def load():
    if request.args:
        counter = int(request.args.get("c"))
        if counter < 0:
            print("posts out of range")
            return make_response(jsonify({}), 404)
        if counter == postNum or counter > postNum:
            print("no more posts")
            return make_response(jsonify({}), 200)
        if counter == 0:
            posts = Dbase.getPosts(counter, quantity)
            print("Returning posts 0 to ", quantity)
            return make_response(jsonify(posts), 200)
        else:
            print("Returning posts ", counter," to ", counter + quantity)
            posts = Dbase.getPosts(counter, quantity)
            return make_response(jsonify(posts), 200)


@flaskApp.route("/about") #TODO: need to add custom error handling to make routing case insensitive
def about():
    title = {'title': 'About'}
    return render_template("about.html", title=title)

@flaskApp.route("/projects")
def projects():
    title = {'title': 'Projects', 'jslink': 'projects.js'}
    return render_template("projects-template.html", title=title)
"""
@flaskApp.route("/projects/<project_url>/<project_url2>")
def projectUrlPull(project_url, project_url2):
    print(project_url)
    print(project_url2)
    x = 0"""

@flaskApp.route("/postload")
def postLoad(): 
    if request.args:
        numPosts = (request.args.get("c"))
        print("numPosts:", numPosts)
        if numPosts == "all":#FIXME: Change these to call Project instead to get specific projects. Clicking on project will then get posts
            posts = Dbase.getPostsType("all")
            return make_response(jsonify(posts), 200)
        elif numPosts == "short":
            posts = Dbase.getPostsType("short")
            return make_response(jsonify(posts), 200)
        elif numPosts == "mid":
            posts = Dbase.getPostsType("mid")
            return make_response(jsonify(posts), 200)
        elif numPosts == "long":
            posts = Dbase.getPostsType("long")
            return make_response(jsonify(posts), 200)
        else:
            response = Dbase.getPostsByProjectAbsUrl(numPosts)
            if len(response) > 0:
                return make_response(jsonify(response), 200)
            else:
                return make_response(jsonify({}), 404)

@flaskApp.route("/projectload")
def projectLoad(): 
    if request.args:
        numPosts = (request.args.get("c"))
        if numPosts == "all":
            posts = Dbase.getProjectType("all")
            return make_response(jsonify(posts), 200)
        elif numPosts == "short":
            posts = Dbase.getProjectType("short")
            return make_response(jsonify(posts), 200)
        elif numPosts == "mid":
            posts = Dbase.getProjectType("mid")
            return make_response(jsonify(posts), 200)
        elif numPosts == "long":
            posts = Dbase.getProjectType("long")
            return make_response(jsonify(posts), 200)
        else:
            response = Dbase.getProjectTitle(numPosts)
            if len(response) > 0:
                return make_response(jsonify(response), 200)
            else:
                return make_response(jsonify({}), 404)



@flaskApp.route("/projects/<url>")
def projectsSun(url):
    urlData = (Dbase.getProjectByShortUrl(url))
    urlData.update({"jslink":"project-page.js"})
    print(urlData)
    if len(urlData) > 0:
        return render_template("projects-template.html", title=urlData)
    else:
        return render_template("404.html"), 404

@flaskApp.route("/projects/<url>/<url2>")
def projectsSub2(url, url2):
    postData = Dbase.getPostByShortUrl(url2)
    postData.update({"jslink":"post.js"})
    print(postData)
    if len(postData) > 0:
        return render_template("post-template.html", title=postData)
    else:
        return render_template("404.html"), 404

@flaskApp.route("/short-term")
def shortterm():
    title = {'title': 'Short Term Projects', 'jslink' : 'short-term-projects.js'}
    return render_template("projects-template.html", title=title)

@flaskApp.route("/mid-term")
def midterm():
    title = {'title': 'Medium Term Projects', 'jslink': 'mid-term-projects.js'}
    return render_template("projects-template.html", title=title)

@flaskApp.route("/long-term")
def longterm():
    title = {'title': 'Long Term Projects', 'jslink': 'long-term-projects.js'}
    return render_template("projects-template.html", title=title)
    






@flaskApp.route("/salvador")
def salvador():
    return "Hello, Salvador"



@flaskApp.errorhandler(404) #FIXME: Fix error handling w/ capitalization
def error404(e):        
    return render_template("404.html"), 404


@flaskApp.errorhandler(405)
def error405(e):
    return render_template("405.html"), 405
