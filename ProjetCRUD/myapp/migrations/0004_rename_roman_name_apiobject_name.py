# Generated by Django 5.0.3 on 2024-03-28 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_name_apiobject_roman_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apiobject',
            old_name='roman_name',
            new_name='name',
        ),
    ]
