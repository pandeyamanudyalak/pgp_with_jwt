from django.db import models
from datetime import date, time
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password


# Create your models here.
class CustomUserManager(BaseUserManager):
    """
    Custom user model where the email address is the unique identifier
    and has an is_admin field to allow access to the admin app 
    """
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError(_("The email must be set"))
        if not password:
            raise ValueError(_("The password must be set"))
        email = self.normalize_email(email)

        user = self.model(email=self.normalize_email(email),name=name)
      #   user.is_staff=True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email,  name, password=None):
      user = self.create_user(email=self.normalize_email(email),name=name,password=password)
      user.is_admin=True
      user.is_active=True
      user.is_staff=True
      user.is_superadmin=True
      user.save(using=self._db)
      
      
      return user






# Create your models here.

class CustomUser(AbstractBaseUser,PermissionsMixin):
   name = models.CharField(max_length=200, blank=True, null=True)
   email = models.EmailField(max_length=200, blank=True, null=True,unique=True)
   # password = models.CharField(max_length=200)
   is_staff=models.BooleanField(default=True)
   is_active=models.BooleanField(default=True)
   is_admin=models.BooleanField(default=False)
   is_superadmin=models.BooleanField(default=False)
  
   objects = CustomUserManager()

   USERNAME_FIELD='email'
   REQUIRED_FIELDS=['password','name']

   
   def __str__(self):
      return self.email

   def has_perm(self,perm,obj=None):
      return self.is_admin

   def has_module_perms(self,add_label):
      return True
   
   
class UserToken(models.Model):
   user_id=models.IntegerField()
   token=models.CharField(max_length=235)
   created_at=models.DateTimeField(auto_now_add=True)
   expired_at=models.DateTimeField()


class userLocation(models.Model):
   location = models.CharField(max_length=200, blank=True, null=True)
   def __str__(self):
      return self.location

class userRole(models.Model):
   roleName = models.CharField(max_length=200, blank=True, null=True)
   def __str__(self):
      return self.roleName

class userDetails(models.Model):
   userName = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
   userLocation = models.ForeignKey(userLocation, on_delete=models.CASCADE, blank=True, null=True)
   userRole = models.ForeignKey(userRole, on_delete=models.CASCADE, blank=True, null=True)
   def __str__(self):
      return str(self.userName)

class issueAgency(models.Model):
   agencyName = models.CharField(max_length=200, blank=True, null=True)
   def __str__(self):
      return str(self.agencyName)

class formData(models.Model):
   loggedPerson = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
   date = models.DateField()
   typeOfWork=models.CharField(max_length=500,blank=True, null=True)
   numberOfPerson = models.IntegerField()
   startTime = models.TimeField()
   endTime= models.TimeField()
   location = models.ForeignKey(userLocation, on_delete=models.CASCADE)
   equipment = models.CharField(max_length=200, blank=True, null=True)
   toolRequired = models.CharField(max_length=200, blank=True, null=True)
   workingAgency=models.ForeignKey(issueAgency, on_delete=models.CASCADE)
   workDescription = models.CharField(max_length=500, blank=True, null=True)
   ppeRequired = models.CharField(max_length=200, blank=True, null=True)
   person1 = models.ForeignKey(CustomUser, related_name="person1", on_delete=models.CASCADE)
   person2 = models.ForeignKey(CustomUser, related_name="person2", on_delete=models.CASCADE)
   verified_by_person1 = models.BooleanField(default=False, null=True)
   verified_by_person2 = models.BooleanField(default=False, null=True)
   newFlag = models.BooleanField(default=True, null=True)
   oldFlag = models.BooleanField(default=False, null=True)
   tocloseFlag = models.BooleanField(default=False, null=True)
   closedByLoggedUser = models.BooleanField(default=False,null=True)
   closedByPerson1 = models.BooleanField(default=False,null=True)
   
   completedFlag = models.BooleanField(default=False, null=True)
   created_at = models.DateField(auto_now_add=True)

   def __str__(self): 
      return str(self.pk)

class person(models.Model):
   person = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
   form = models.ForeignKey(formData, on_delete=models.CASCADE)
   new_notification = models.BooleanField(default=False)


