# Generated by Django 2.1.7 on 2019-05-11 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudAPI', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='titie',
            new_name='title',
        ),
    ]
