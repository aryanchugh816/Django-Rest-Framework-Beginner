from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


# Custom User model for using email as primary key instead of username
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # We will create a custom user profile manager to handle our custom user model
    objects = UserProfileManager()


    # This 'username_field' specifies that we are using email instead of username as default in django and is required by defaullt 
    USERNAME_FIELD = 'email'

    # More required fields
    REQUIRED_FIELDS = ['name']

    # Now we will define some methods for this class

    def get_full_name(self):
        """Retrieve full name for user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name for user"""
        return self.name

    # This is just a string representation of our user, is a good practice to implement
    def __str__(self):
        """Return string representation of user"""
        return self.email
