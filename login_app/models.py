from django.db import models


class users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_id = models.EmailField(max_length = 254,unique=True)
    password = models.CharField(max_length=30,unique=True)
    is_admin = models.BooleanField()
    is_deleted = models.BooleanField()
    class Meta:
        managed = False
        db_table = 'public\".\"login_app_users'

class admin_url(models.Model):
    url_link = models.URLField(max_length = 200)
    is_deleted = models.BooleanField()
    class Meta:
        managed = False
        db_table = 'public\".\"login_app_admin_url'