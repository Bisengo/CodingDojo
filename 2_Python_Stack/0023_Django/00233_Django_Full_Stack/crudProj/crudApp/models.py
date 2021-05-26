from django.db import models

# Create your models here.
class Birthday(models.Model):
    value=models.DateField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __repr__ (self):
        return f"<Show object: {self.value} ({self.id})>"