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

        # username is required
        if len(forminfo['fname']) == 0:
            regValidationErrors['uName_blank'] = "Please enter the user name"
        # username must be at least 2 characters
        elif len(forminfo['fname']) < 2:
            regValidationErrors['uName_short'] = "First name must be at least 2 characters"

        # email address is needed
        if len(forminfo['femail']) == 0:
            regValidationErrors['email_blank'] = "Please enter the email"
        # email address must be valid
        elif not EMAIL_REGEX.match(forminfo['femail']):  
            regValidationErrors['emailformat'] = "Email is invalid"
        # chosen email address must be already in use
        else:
            usersWithEmail = User.objects.filter(email = forminfo['femail'])
            print("printing users with email now")
            print(usersWithEmail)
            if len(usersWithEmail)>0:
                regValidationErrors['emailTaken'] = "Email is already taken, please try another email address."

        # password is required
        if len(forminfo['fpw']) == 0:
            regValidationErrors['password_blank'] = "Please enter the password"
        # password must be at least 8 characters
        elif len(forminfo['fpw']) < 8:
            regValidationErrors['password_short'] = "Password must be at least 8 characters"
        # passwords must match
        elif forminfo['fpw'] != forminfo['fcpw']:
            regValidationErrors['confirm'] = "Password and confirm password must match"
    
        return regValidationErrors

    def loginValidator(self, forminfo):
        loginValidationErrors = {}
        #email is requried to log in
        if len(forminfo['femail']) < 1:
            loginValidationErrors['email_short'] = "Email is required"
        
        #email must be found in the database, in order to log in
        emailsExist = User.objects.filter(email = forminfo['femail'])
        print(emailsExist)
        if len(emailsExist)== 0:
            loginValidationErrors['emailNotFound'] = "This email was not found. Please register first."
        else:
            user = emailsExist[0]
            #if email submitted in form is found in db, then password must match for that user with that email

            if not bcrypt.checkpw(forminfo['fpw'].encode(), user.password.encode()):
                loginValidationErrors['fpw'] = "Password does not match"

        return loginValidationErrors 

class QuoteManager(models.Manager):
    def quoteValidator(self, forminfo ):
        quoteValidationErrors = {}
        #some validation code here
        # author is required
        if len(forminfo['fauthor']) < 1:
            quoteValidationErrors['authorNameRequired'] = "author name is required"
        # author must be at least 3 characters
        elif len(forminfo['fauthor']) < 3:
            quoteValidationErrors['authorNameShort'] = "author name needs to be at least 3 characters"
        # quote content is needed
        if len(forminfo['fcontent']) < 1:
            quoteValidationErrors['contentRequired'] = "quote content is required"
        # quote content must be at least 10 characters
        elif len(forminfo['fcontent']) < 10:
            quoteValidationErrors['contentShort'] = "quote content needs to be at least 10 characters"
        print(quoteValidationErrors)
        return quoteValidationErrors


class User(models.Model):
    userName = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

    def __rep__(self):
        return f"<User object:{self.userName} ({self.id})>"

class Quote(models.Model):  
    content = models.TextField()
    author = models.CharField(max_length = 255)
    uploader = models.ForeignKey(User, related_name = 'quote_uploaded', on_delete = models.CASCADE)
    favoritor = models.ManyToManyField(User, related_name ='quote_favored')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()

    def __rep__(self):
        return f"<Quote object:{self.author} ({self.id})>"