# Generated by Django 3.0.2 on 2020-02-22 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200221_1708'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='userpersonaldb',
            name='no_double',
        ),
    ]
