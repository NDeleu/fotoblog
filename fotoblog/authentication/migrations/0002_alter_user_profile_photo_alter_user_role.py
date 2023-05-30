# Generated by Django 4.2.1 on 2023-05-30 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(upload_to='', verbose_name='photo de profil'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('CREATOR', 'Créateur'), ('SUBSCRIBER', 'Abonné')], max_length=30, verbose_name='rôle'),
        ),
    ]
