# Generated by Django 5.0.7 on 2024-08-20 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_remove_instructorprofile_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='otp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
