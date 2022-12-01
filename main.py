from flask import Flask,render_template,redirect
from routes.user import route as user
app = Flask(__name__)

with app.app_context():
    from config.dbConnection import Base,engine,db_session
    from model.posts import Posts
    from model.user_details import UserSchema
    Base.metadata.create_all(bind=engine)

from routes.posts import route as post_
from routes.comments import route as comment_


post_.postBlueprint.register_blueprint(comment_.commentBlueprint)
user.userBlueprint.register_blueprint(post_.postBlueprint)
app.register_blueprint(user.userBlueprint)


@app.before_request
def closeConnection():
    db_session.remove()

@app.errorhandler(404)
def error404(e):
    return render_template("error404.html")



if __name__=="__main__":
    app.run(port=4541)



