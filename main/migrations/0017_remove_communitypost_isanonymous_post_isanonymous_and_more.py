# Generated by Django 4.0 on 2022-12-12 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_rename_schedule_calender_content_alter_calender_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='communitypost',
            name='isAnonymous',
        ),
        migrations.AddField(
            model_name='post',
            name='isAnonymous',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='complaints',
        ),
    ]
