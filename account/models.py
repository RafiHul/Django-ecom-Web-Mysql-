from django.db import models
from django.contrib.auth.models import User as AuthUser


class UserProfile(models.Model):
    username_acc = models.ForeignKey(AuthUser, on_delete=models.CASCADE, db_column='username_acc', to_field='username')
    gambar = models.ImageField(upload_to="profile_pic", default='profile_pic/default_pic.jpg')
    saldo = models.IntegerField(default=0, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'user_profile'

    def __str__(self):
        return str(self.username_acc)  