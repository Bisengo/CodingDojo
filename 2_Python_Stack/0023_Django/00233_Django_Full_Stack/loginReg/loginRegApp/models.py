from django.db import models
import re, bcrypt

# Create your models here.
class UserManager(models.Manager):
    
    def registrationValidator(self, forminfo):
        validationErrors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        print('printing forminfo in validator function')
        print(forminfo)
        if len(forminfo['fname']) < 2:
            validationErrors['firstName'] = "First name must be at least 2 characters"
        if len(forminfo['lname']) < 2:
            validationErrors['lastname'] = "Last name must be at least 2 characters"
        if len(forminfo['email']) < 1:
            validationErrors['email'] = "Email is required"
        elif not EMAIL_REGEX.match(forminfo['email']):
            validationErrors['emailformat'] = "Email is invalid"
        else:
            usersWithEmail = User.objects.filter(email = forminfo['email'])
            print("printing users with email now")
            print(usersWithEmail)
            # usersWithEmail looks like : <QuerySet [<User: User object (1)>]>
            if len(usersWithEmail)>0:
                validationErrors['emailTaken'] = "Email is already taken, please try another email address."
        if len(forminfo['pw']) < 8:
            validationErrors['password'] = "Password must be at least 8 characters"
        if forminfo['pw'] != forminfo['cpw']:
            validationErrors['confirm'] = "Password and confirm password must match"
        
        #email address should be valid
        return validationErrors

    def loginValidator(self, forminfo):
        errors = {}
        #email is requried to log in
        if len(forminfo['email']) < 1:
            errors['email'] = "Email is required"
        
        #email must be found in the database, in order to log in
        emailsExist = User.objects.filter(email = forminfo['email'])
        print(emailsExist)
        if len(emailsExist)== 0:
            errors['emailNotFound'] = "This email was not found. Please register first."
        else:
            user = emailsExist[0]
            #if email submitted in form is found in db, then password must match for that user with that email

            if not bcrypt.checkpw(forminfo['pw'].encode(), user.password.encode()):
                errors['pw'] = "Password does not match"

        return errors



class ItemManager(models.Manager):
    def validateItem(self, forminfo):
        errors = {}
        #some validation code here
        if len(forminfo['itemName'])<1:
            errors['itemNameRequired']= "Item name is required"
        elif len(forminfo['itemName'])<4:
            errors['itemNameShort']= "Item name needs to be at least 4 characters"
        print(errors)
        return errors


class User(models.Model):
    firstName = models.CharField(max_length = 255)
    lastName = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
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
