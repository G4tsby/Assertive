# Generated by Django 4.1.4 on 2022-12-11 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_rename_security_todo_securitytodo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='car',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
