from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):  #this is equivalent of user.password == password, it just works on all python versions and different systems
        return user
        
def identity(payload):  #identity function is unique to FlaskJWT (which we installed). payload is the contents of the JWT token.
    user_id = payload['identity'] 
    return UserModel.find_by_id(user_id)
        