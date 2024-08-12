from django.db import models


# Create your models here.
class UserInfo(models.Model):
    user_id = models.IntegerField()
    fullname = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='images')

    def __str__(self):
        return self.fullname


class Photos_to_check(models.Model):
    user_id = models.IntegerField()
    photo = models.ImageField(upload_to='images_tocheck')

    def __str__(self):
        return str(self.user_id)