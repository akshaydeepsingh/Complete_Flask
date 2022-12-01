from flask import Blueprint,request
from flask_restful import Api,Resource
from model.user_details import User
from model.posts import Posts,PostsSchema
from marshmallow.exceptions import ValidationError
from config.dbConnection import db_session
from model.channel import Channel


postBlueprint = Blueprint("postBlueprint",__name__)
postsRoute=Api(postBlueprint)

class PostClass(Resource):
    def post(self,id):
        user = User.query.filter_by(id=id).first()
        requestData = request.json
        post = Posts(title=requestData["title"],category=  requestData["category"],Description= requestData["Description"])
        channeL = Channel(name="fb")
        post.channel = [channeL]
        user.posts.append(post)
        db_session.add(user)

        db_session.commit()
        return {"status":"created"}
    def get(self,id,postid=None):
        if postid is None:
            user = User.query.filter_by(id=id).first()
            postschema = PostsSchema(many=True)
            response = postschema.dump(user.posts.all())
            return response
        else:
            user = User.query.filter_by(id = id).first()
            postschema = PostsSchema()
            if user:
                response = postschema.dump(user.posts.filter(Posts.id == postid).first())
                
            else:
                response = postschema.dump(Posts.query.filter(Posts.id == postid,Posts.userid == id).first())
            
            return response
    def put(self,id,postid):
        user = User.query.filter_by(id = id).first()
        post_ = user.posts.filter(Posts.id == postid).first()
        postschema = PostsSchema()
        postschema.load(request.json,instance=post_,partial = True,session=db_session)
        db_session.commit()
        response = postschema.dump(post_)
        return response
    def delete(self,id,postid):
        user = User.query.filter_by(id = id).first()
        user.posts.filter(Posts.id == postid).delete()
        db_session.commit()
        return {"status":"Deleted"}

postsRoute.add_resource(PostClass,"/users/<id>/posts/","/users/<id>/posts/<postid>")
        # user.posts.append()