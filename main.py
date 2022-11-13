from flask import Flask

app = Flask(__name__)

with app.app_context():
    from config.dbConnection import Base,engine,db_session
    from model.posts import Posts
    from model.user_details import UserSchema
    Base.metadata.create_all(bind=engine)

@app.before_request
def closeConnection():
    db_session.remove()

@app.route("/")
def home():
    return "welcome flask"


if __name__=="__main__":
    app.run(port=4541)



