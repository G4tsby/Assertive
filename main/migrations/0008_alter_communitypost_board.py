# Generated by Django 4.1.4 on 2022-12-10 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_board_alter_communitypost_board'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitypost',
            name='board',
            field=models.CharField(max_length=50),
        ),
    ]
