from django.contrib.auth.backends import ModelBackend
from principal.models import PrincipalUser

class PrincipalBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = PrincipalUser.objects.get(username=username)
            if user.check_password(password):
                return user
        except PrincipalUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return PrincipalUser.objects.get(pk=user_id)
        except PrincipalUser.DoesNotExist:
            return None
