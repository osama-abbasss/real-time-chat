from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Message(models.Model):
    author = models.ForeignKey(User, related_name='user_message', on_delete= models.CASCADE)
    content = models.TextField()
    timestemp = models.DateTimeField(auto_now_add = True)

    def __Str__(self):
        return self.auther.username

    def last_15_message():
        return Message.objects.order_by('-timestemp').all()[:15]
