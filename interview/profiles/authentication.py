from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from interview.profiles.models import UserProfile


class SettingsBackend(BaseBackend):
    """
    Authenticate against the custom user's table.

    Use the login name and a hash of the password. For example:

    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'pbkdf2_sha256$30000$Vo0VlMnkR4Bk$qEvtdyZRWTcOsCnI/oQ7fVOu1XAURIZYoOZ3iq8Dr4M='
    """

    def authenticate(self, request, username=None, password=None):
        user_profile = UserProfile.objects.filter(email=username).first()
        if not user_profile:
            return None
        pwd_valid = check_password(password, user_profile.password)
        if pwd_valid:
            return user_profile
        return None

    def get_user(self, user_id):
        return UserProfile.objects.filter(pk=user_id).first()
