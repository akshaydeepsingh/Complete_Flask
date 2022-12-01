from flask import Blueprint,request
from flask_restful import Api,Resource
from model.comment import Comments,CommentSchema
from model.posts import Posts
from config.dbConnection import db_session
commentBlueprint= Blueprint("commentBlueprint",__name__)
commentRoute= Api(commentBlueprint)

class CommentClass(Resource):
    def post(self,postid):
        serverData = {}
        clientData = request.json
        post = Posts.query.filter_by(id = postid).first()
        userUrl = f"http://127.0.0.1:4541/users/{post.userid}"
        serverData["comment"]=clientData["comment"]
        serverData["user"]=userUrl
        addComment = Comments(**serverData)
        post.comment.append(addComment)
        db_session.add(post)
        db_session.commit()
        return serverData
    def get(self,postid,commentid=None):
        if commentid !=None:
            # posts = Posts.query.filter_by(id=postid).first()
            # print(posts)
            commentschema = CommentSchema()
            response = commentschema.dump(Comments.query.filter(Comments.id==commentid,Comments.post_id==postid).first())
            return response
        else:
            # posts = Posts.query.filter_by(id=postid).first()
            commentschema = CommentSchema(many=True)
            response = commentschema.dump(Comments.query.filter(Comments.post_id==postid).all())
            
            return response
    def put(self,postid,commentid=None):
        payload = request.json
        commentschema = CommentSchema()
        comment = Comments.query.filter(Comments.id==commentid,Comments.post_id==postid).first()
        updated = commentschema.load(payload,instance=comment,partial=True,session=db_session)
        db_session.commit()
        response = commentschema.dump(comment)
        return response


commentRoute.add_resource(CommentClass,"/posts/<postid>/comments/","/posts/<postid>/comments/<commentid>")