# Generated by Django 4.1.2 on 2022-10-31 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0006_alter_business_job_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='job_image',
        ),
    ]
