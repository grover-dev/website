from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Post, Project
from config import Config
from datetime import datetime
from website import db
from .utils import Utils



class Dbase():

    def __init__(self):
        print("initializing database")
        # an Engine, which the Session will use for connection
        # resources
        engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

        # at the module level, the global sessionmaker,
        # bound to a specific Engine
        Session = sessionmaker(bind=engine)
        session = Session()
        #self.session = session

    def getPosts(index, numPosts):
        print("get posts by index and numPosts")
        posts = Post.query.all()
        tempPosts = []
        temp = 0
        for p in posts[::-1]:
            if temp >= index and temp <= (numPosts+index):
                tempPosts.append({"title": p.title, "text": p.text, "blurb": p.blurb, "url":p.abs_url})
            elif temp > (numPosts+index):
                return tempPosts
            temp += 1
        return tempPosts

    def getPostsType(typePost):
        print("get posts by type")
        posts = Post.query.filter(Post.type_post.contains(typePost)).order_by(Post.id).all()
        tempPosts = []
        for p in posts[::-1]:
            tempPosts.append({"title": p.title, "text": p.text, "blurb": p.blurb, "url":p.abs_url})
        if len(tempPosts) == 0:
            print("no posts with tag "+typePost + " found")
        return tempPosts

    def getPostByShortUrl(url):
        print("get post by url")
        posts = Post.query.filter(Post.url == url).order_by(Post.id).all()
        tempPosts = {}
        for p in posts[::-1]:
            tempPosts.update({"title": p.title, "text": p.text, "timestamp": p.timestamp, "type_post":p.type_post, "user_id": p.user_id, "project": p.project, "blurb": p.blurb, "url":p.abs_url})
        if len(tempPosts) == 0:
            print("no posts with url "+ url + " found")
        return tempPosts

    def getProjectType(typeProject):
        print("get project by type")
        projects = Project.query.filter(Project.type_project.contains(typeProject)).order_by(Project.id).all()
        tempProjects = []
        for p in projects[::-1]:
            tempProjects.append({"title": p.title, "blurb": p.blurb, "url": p.abs_url})
        if len(tempProjects) == 0:
            print("no projects with tag "+typeProject + " found")
        return tempProjects
    
    def getProjectTitle(titleProject):
        print("get project by title")
        projects = Project.query.filter(Project.title == titleProject).order_by(Project.id).all()
        tempProjects = []
        for p in projects[::-1]:
            tempProjects.append({"title": p.title, "blurb": p.blurb, "url": p.abs_url})
        if len(tempProjects) == 0:
            print("no projects with title "+ titleProject + " found")
        return tempProjects

    def getProjectByShortUrl(url):
        print("get project by url")
        project = Project.query.filter(Project.url == url).order_by(Project.id).all()
        tempProject = {}
        for p in project:
            tempProject.update({"title": p.title, "blurb":p.blurb, "type_project":p.type_project, "status": p.status})
            return tempProject
        return tempProject
        

    def getProjectUrlByTitle(title):
        print("get project url by name ", title)
        project = Project.query.filter(Project.title == title).order_by(Project.id).all()
        tempProject = ["",""]
        for p in project:
            tempProject[0] = p.url 
            tempProject[1] = p.abs_url
            return tempProject
        return tempProject

    def getPostsByProjectTitle(project):
        print("get project posts by title", project)
        posts = Post.query.filter(Post.project == project).order_by(Post.id).all()
        tempPosts = []
        for p in posts:
            tempPosts.append({"title": p.title, "blurb": p.blurb, "url": p.abs_url , "timestamp":p.timestamp})
        return tempPosts


    def numPosts():
        rows = Post.query.count()
        return rows

    def newProject(projectTitle, blurbText, projectTypeVal):
        urlTmp = Utils.urlGen(projectTitle, Project)
        if urlTmp is not None:
            p = Project(title=projectTitle, blurb=blurbText, type_project=projectTypeVal, url=urlTmp, abs_url="/projects/"+urlTmp, status="0")
            db.session.add(p)
            db.session.commit()
            return
        else:
            print("error occured in url generation")     
    
    def newPost(postTitle, postText, blurbText, user, postTypeVal, sourceProject):
        projectUrl = Dbase.getProjectUrlByTitle(sourceProject)
        if len(projectUrl) < 2:
            print("project not found")
            return
        urlHead = projectUrl[1]
        urlTmp = Utils.urlGen(postTitle, Post)
        if urlTmp is not None:
            p = Post(title=postTitle, text=postText, timestamp=datetime.now(), type_post=postTypeVal, project=sourceProject, user_id=user, url=urlTmp, abs_url = urlHead  + "/" + urlTmp, blurb=blurbText)
            db.session.add(p)
            db.session.commit()
            return
        else:
            print("error occured in url generation") 
            return

    def createNewProject():
        print("creating project")
        print("input title")
        title = input()
        print("input blurb")
        blurb = input()
        print("project type")
        projectType = input()
        Dbase.newProject(title, blurb, projectType)

    def createPost(): 
        print("creating post")
        print("input title")
        title = input()
        print("input blurb")
        blurb = input()
        

        print("post text")
        text = input()

        print("post type")
        projectType = input()
        print("post user")
        user = input()

        print("post sourceProject")
        sourceProject = input()

        Dbase.newPost(title, text, blurb, user, projectType, sourceProject)
