# Generated by Django 3.2.15 on 2022-08-31 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin_url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_link', models.URLField()),
                ('is_deleted', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email_id', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('is_admin', models.BooleanField()),
                ('is_deleted', models.BooleanField()),
            ],
        ),
    ]