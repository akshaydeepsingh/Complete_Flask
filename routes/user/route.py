from flask import Blueprint,request
from flask_restful import Api,Resource
from model.user_details import User,UserSchema
from marshmallow.exceptions import ValidationError
from config.dbConnection import db_session
import json
userBlueprint = Blueprint("userBlueprint",__name__,url_prefix='/users')

userRoute = Api(userBlueprint)

class UserClass(Resource):
    def get(self,id=None):
        if id is None:
            user = User.query.all()
            userschema = UserSchema(many=True)
            response = userschema.dump(user)
<<<<<<< HEAD
            print(response)
            # del response["id"]
=======
            
>>>>>>> a92bdc5b52984a5df98f0427f0e07039627da414
            return response
        else:
            user = User.query.filter_by(id=id).first()
            userschema = UserSchema()
            response = userschema.dump(user)
            del response["id"]
            return response
            
    def post(self):
        userdata = request.json
        userschema = UserSchema()
        try:
            user  = userschema.load(userdata,session=db_session)
            db_session.add(user)
            db_session.commit()
            print(user)
            return userdata
        except ValidationError as e:
            return {'message': json.dumps(e.messages)}
    def put(self,id):
        userdata = request.json
        userschema = UserSchema()
        try:
            user = User.query.filter_by(id=id).first()
            userschema.load(userdata,instance=user,session=db_session)
            db_session.commit()
            response = userschema.dump(user)
            return userdata
        except ValidationError as e:
            return {'message': json.dumps(e.messages)}
    def delete(self,id):
        User.query.filter_by(id = id).delete()
        db_session.commit()
        return {"status":"Deleted"}

             

userRoute.add_resource(UserClass,"/", "/<id>")




