from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Message(models.Model):
    author = models.ForeignKey(User, related_name='user_message', on_delete= models.CASCADE)
    room_name = models.CharField(max_length = 25)
    content = models.TextField()
    timestemp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.author.username

    def last_15_messages():
        return Message.objects.order_by('-timestemp').all()[:15]
