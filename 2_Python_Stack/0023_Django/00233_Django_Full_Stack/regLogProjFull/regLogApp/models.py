from django.db import models
import re, bcrypt
from datetime import datetime, date, timedelta

# Create your models here.

class UserManager(models.Manager):

    def registrationValidator(self, forminfo):
        regValidationErrors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        print('printing forminfo in validator function')
        print(forminfo)

        # Validation criteria given below

        # first name must be at least 2 characters
        if len(forminfo['fname']) == 0:
            regValidationErrors['firstName_blank'] = "Please enter the first name"
        elif len(forminfo['fname']) < 2:
            regValidationErrors['firstName_short'] = "First name must be at least 2 characters"
        # last name must be at least 2 characters
        if len(forminfo['lname']) == 0:
            regValidationErrors['lastName_blank'] = "Please enter the last name"
        elif len(forminfo['lname']) < 2:
            regValidationErrors['lastname_short'] = "Last name must be at least 2 characters"

        # email address is needed
        if len(forminfo['email']) == 0:
            regValidationErrors['email_blank'] = "Please enter the email"
        # email address must be valid
        elif not EMAIL_REGEX.match(forminfo['email']):  
            regValidationErrors['emailformat'] = "Email is invalid"
        # chosen email address must be already in use
        else:
            usersWithEmail = User.objects.filter(email = forminfo['email'])
            print("printing users with email now")
            print(usersWithEmail)
            if len(usersWithEmail)>0:
                regValidationErrors['emailTaken'] = "Email is already taken, please try another email address."

        # password must be at least 8 characters
        if len(forminfo['pw']) == 0:
            regValidationErrors['password_blank'] = "Please enter the password"
        elif len(forminfo['pw']) < 8:
            regValidationErrors['password_short'] = "Password must be at least 8 characters"
        # passwords must match
        if forminfo['pw'] != forminfo['cpw']:
            regValidationErrors['confirm'] = "Password and confirm password must match"
        
        today = datetime.today()
        valdate = today - timedelta(days = 18*365)
        date_str = forminfo['bday']
        today_str = today.strftime('%Y-%m-%d')
        vald_str = valdate.strftime('%Y-%m-%d')
        # birth date is required 
        if len(forminfo['bday']) == 0:
            regValidationErrors['bday_blak'] = "Please enter your birth date"
        # birth date should be in the past 
        elif date_str > today_str:
            regValidationErrors['bday_past'] = "birth date should be in past"
        # user must be at least 13 years old
        elif vald_str < date_str:
            regValidationErrors['bday_age'] = "You must be at least 18 to register"
        return regValidationErrors

    def loginValidator(self, forminfo):
        loginValidationErrors = {}
        #email is requried to log in
        if len(forminfo['email']) < 1:
            loginValidationErrors['email_short'] = "Email is required"
        
        #email must be found in the database, in order to log in
        emailsExist = User.objects.filter(email = forminfo['email'])
        print(emailsExist)
        if len(emailsExist)== 0:
            loginValidationErrors['emailNotFound'] = "This email was not found. Please register first."
        else:
            user = emailsExist[0]
            #if email submitted in form is found in db, then password must match for that user with that email

            if not bcrypt.checkpw(forminfo['pw'].encode(), user.password.encode()):
                loginValidationErrors['pw'] = "Password does not match"

        return loginValidationErrors    

class ItemManager(models.Manager):
    def itemValidator(self, forminfo):
        itemValidationErrors = {}
        #some validation code here
        if len(forminfo['itemName'])<1:
            itemValidationErrors['itemNameRequired']= "Item name is required"
        elif len(forminfo['itemName'])<4:
            itemValidationErrors['itemNameShort']= "Item name needs to be at least 4 characters"
        print(itemValidationErrors)
        return itemValidationErrors

class User(models.Model):
    firstName = models.CharField(max_length = 255)
    lastName = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    birthdate = models.DateField(auto_now_add = False, auto_now = False, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    
class Item(models.Model):
    name = models.CharField(max_length = 255)
    uploader = models.ForeignKey(User, related_name = 'items_uploaded', on_delete = models.CASCADE)
    favoritor = models.ManyToManyField(User, related_name ='fav_items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ItemManager()