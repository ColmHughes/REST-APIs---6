from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):      #This is equivalent of user.password == password,
        return user                                         #it just works on all python versions and different systems.
        
def identity(payload):      #identity function is unique to FlaskJWT (which we installed). The payload is the contents of the JWT token.
    user_id = payload['identity'] 
    return UserModel.find_by_id(user_id)
        