# Generated by Django 4.0.6 on 2022-08-10 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0007_space_id_alter_space_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='space',
            old_name='slug',
            new_name='spaceslug',
        ),
    ]
