from flask.ext.script import Manager
from lineageAPi import *
manager = Manager(app)
@manager.command
def builddb():
    if not os.path.exists('db.sqlite'):
        db.create_all()

    print "SQL lite db was created"

@manager.command
def createsuperuser(user, password):
    user =  new_user(user,password)
    print "Token: " + user.generate_auth_token()

# def createusertoken():

def get_new_token(username):
    user = User.query.filter_by(username=username).first()
    user.get
    if user is not None:
        token = user.generate_auth_token()
        print "Token: " + token
    else:
        abort(400)    # existing user

if __name__ == "__main__":
    manager.run()



