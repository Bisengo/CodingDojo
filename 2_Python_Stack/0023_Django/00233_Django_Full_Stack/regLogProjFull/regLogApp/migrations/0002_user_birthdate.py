# Generated by Django 2.2.4 on 2020-05-23 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regLogApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.DateField(null=True),
        ),
    ]