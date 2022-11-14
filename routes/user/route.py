from flask import Blueprint,request
from flask_restful import Api,Resource
from model.user_details import User,UserSchema
from marshmallow.exceptions import ValidationError
from config.dbConnection import db_session
import json
userBlueprint = Blueprint("userBlueprint",__name__,url_prefix='/users')
userRoute = Api(userBlueprint)

class UserFunction(Resource):
    def get(self,id=None):
        if id is None:
            return "all users"
        else:

            return f"its user {id}"
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
             

userRoute.add_resource(UserFunction,"/", "/<id>")




