# Generated by Django 3.2.4 on 2021-06-13 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('happyd1g1t', '0002_happiness'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='happiness',
            unique_together={('user', 'date')},
        ),
    ]