# Generated by Django 4.1.2 on 2022-11-01 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0010_alter_business_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employers',
            options={'ordering': ['-applied_date']},
        ),
    ]
