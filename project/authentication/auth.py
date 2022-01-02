from cuser.middleware import CuserMiddleware
from rest_framework.authentication import TokenAuthentication


class CustomTokenAuthentication(TokenAuthentication):

    def authenticate_credentials(self, token):
        user, token = super().authenticate_credentials(token)
        CuserMiddleware.set_user(user)
        return user, token
