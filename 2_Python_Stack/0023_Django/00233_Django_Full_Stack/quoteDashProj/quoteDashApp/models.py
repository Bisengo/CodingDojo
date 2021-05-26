from django.db import models
import re, bcrypt

# Create your models here.
class UserManager(models.Manager):

    def registrationValidator(self, forminfo):
        regValidationErrors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        print('printing forminfo in validator function')
        print(forminfo)

	# Validation criteria given below

	# first name must be at least 2 characters
	# last name must be at least 2 characters
        if len(forminfo['fname']) < 2:
            regValidationErrors['firstName'] = "First name must be at least 2 characters"
        if len(forminfo['lname']) < 2:
            regValidationErrors['lastname'] = "Last name must be at least 2 characters"

	# email address is needed
	# email address must be valid
	# chosen email address must be already in use
        if len(forminfo['email']) < 1:
            regValidationErrors['email'] = "Email is required"
        elif not EMAIL_REGEX.match(forminfo['email']):  regValidationErrors['emailformat'] = "Email is invalid"
        else:
            usersWithEmail = User.objects.filter(email = forminfo['email'])
            print("printing users with email now")
            print(usersWithEmail)
            # usersWithEmail looks like : <QuerySet [<User: User object (1)>]>
            if len(usersWithEmail)>0:
                regValidationErrors['emailTaken'] = "Email is already taken, please try another email address."

	# password must be at least 8 characters
	# passwords must match
        if len(forminfo['pw']) < 8:
            regValidationErrors['password'] = "Password must be at least 8 characters"
        if forminfo['pw'] != forminfo['cpw']:
            regValidationErrors['confirm'] = "Password and confirm password must match"
        
        return regValidationErrors

    def loginValidator(self, forminfo):
        loginValidationErrors = {}

        #email is requried to log in
        if len(forminfo['email']) < 1:
            loginValidationErrors['email'] = "Email is required"
        
        #email must be found in the database in order to log in
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

class QuoteManager(models.Manager):
    def quoteValidator(self, forminfo ):
        quoteValidationErrors = {}
        #some validation code here
        if len(forminfo['authorFromHtml'])<1:
            quoteValidationErrors['authorNameRequired']= "author name is required"
        elif len(forminfo['authorFromHtml'])<3:
            quoteValidationErrors['authorNameShort']= "author name needs to be at least 3 characters"
        
        if len(forminfo['contentFromHtml'])<1:
            quoteValidationErrors['contentRequired']= "quote content is required"
        elif len(forminfo['contentFromHtml'])<10:
            quoteValidationErrors['contentShort']= "quote content needs to be at least 10 characters"
        print(quoteValidationErrors)
        return quoteValidationErrors

class User(models.Model):
    firstName = models.CharField(max_length = 255)
    lastName = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

    def __rep__(self):
        return f"<User object:{self.firstName} ({self.id})>"



class Quote(models.Model):
    content = models.TextField()
    author = models.CharField(max_length = 255)
    uploader = models.ForeignKey(User, related_name = 'quote_uploaded', on_delete = models.CASCADE)
    favoritor = models.ManyToManyField(User, related_name ='quote_favored')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()

    def __rep__(self):
        return f"<User object:{self.author} ({self.id})>"