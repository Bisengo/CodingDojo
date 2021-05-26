from django.db import models
from datetime import datetime

# Create your models here.

class ShowManager(models.Manager):
    def showValidator(self, forminfo):
        validationErrors = {}
        # title required and must be at least 2 characters
        if len(forminfo['ftitle']) == 0:
            validationErrors['title_blank'] = "please enter a title"      
        elif len(forminfo['ftitle']) < 2:
            validationErrors['title_short'] = "title must be at least 2 characters"
        showsWithtitle = Show.objects.filter(title = forminfo['ftitle'])
        print("printing shows with the title now")
        print(showsWithtitle)
            # usersWithEmail looks like : <QuerySet [<User: User object (1)>]>
        if len(showsWithtitle)>0:
            validationErrors['titleTaken'] = "this title is already taken, please choose another one."
        
        # network required and must be at least 3 characters
        if len(forminfo['fnetwork']) == 0:
            validationErrors['network_blank'] = "please enter the network"
        elif len(forminfo['fnetwork']) < 3:
            validationErrors['network_short'] = "network must be at least 3 characters"

        # release date should be in the past
        date_str = forminfo['frelease']
        today = datetime.today().strftime('%Y-%m-%d')
        if date_str > today:
            validationErrors['release'] = "release date should be in past"

        # description is optional but if present must be at least 10 characters
        if len(forminfo['fdesc']) > 0 and len(forminfo['fdesc']) < 10:
            validationErrors['fdesc'] = "description must be at least 10 characters"
        
        return validationErrors



class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
    
    def __repr__ (self):
        return f"<Show object: {self.title} ({self.id})>"
