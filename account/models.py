from django.db import models
from django.contrib.auth.models import User as AuthUser


class UserProfile(models.Model):
    username_acc = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='username_acc', to_field='username')
    gambar = models.ImageField(upload_to="profile_pic", blank=True, null=True)
    saldo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_profile'

    def __str__(self):
        return str(self.username_acc)  