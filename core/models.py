from django.db import models
from django.contrib.auth import get_user_model




class Notification(models.Model) :
    user = models.ForeignKey(get_user_model(),related_name = 'notification',on_delete = models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add = True)

    class Meta() :
        ordering = ['-date']


class NewsLaterSubscriber(models.Model) :
    email = models.EmailField(blank = False)  

    def __str__(self)  :
        return self.email
