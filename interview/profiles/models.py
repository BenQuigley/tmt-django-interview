from django.contrib.auth.hashers import make_password
from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)  # hashed and salted
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    avatar = models.ImageField(null=True)

    def get_full_name(self) -> str:
        """Combine the first and last name to a full name if both exist."""
        # ref: https://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/
        return " ".join([name for name in (self.first_name, self.last_name) if name])

    def get_username(self):
        """Retrieve the record's username."""
        # FIXME Not sure why this function was requested; probably misunderstood this requirement.
        return self.username

    @property
    def is_authenticated(self):
        """Always return True.

        For distinguishing between e.g. AnonymousUser.
        Does not imply any permissions and doesn’t check if the user is active or has a valid session.

        ref: https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#django.contrib.auth.models.AbstractBaseUser.is_authenticated
        """
        return True

    @property
    def is_active(self):
        return True

    def has_module_perms(self, *args, **kwargs):
        # TODO implement me
        return self.is_staff or self.is_admin or self.is_superuser

    def has_perm(self, *args, **kwargs):
        # TODO implement me
        return self.is_staff or self.is_admin or self.is_superuser

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
