from django.db import models

class Send(models.Model):
    """"""
    phone = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    turn = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Send sms to {self.phone} in {self.city} at {self.created}"