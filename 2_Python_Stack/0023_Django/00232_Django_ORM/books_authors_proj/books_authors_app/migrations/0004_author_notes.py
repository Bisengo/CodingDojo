# Generated by Django 2.2.4 on 2020-04-20 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0003_auto_20200420_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(null=True),
        ),
    ]
