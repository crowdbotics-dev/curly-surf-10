# Generated by Django 2.2.28 on 2023-03-17 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_text_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='text_field',
        ),
    ]