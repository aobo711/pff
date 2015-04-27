from django.db import models

class Feedback(models.Model):
    desc = models.TextField(max_length=500, blank=False, null= False)
    udid = models.CharField(max_length=100, blank=True)
    contact = models.CharField(max_length=100, blank=True)
    os_version = models.CharField(max_length=100, blank=True)

    api_level = models.CharField(max_length=100, blank=True)
    device = models.CharField(max_length=100, blank=True)

    model = models.CharField(max_length=100, blank=True)
    
    @classmethod
    def create(cls, desc):
        feedback = cls(desc=desc)
        return feedback
        
    def __unicode__(self):
        return self.udid