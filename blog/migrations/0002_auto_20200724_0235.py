# Generated by Django 3.0.8 on 2020-07-24 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='poststatus',
            options={'ordering': ['-post__created']},
        ),
    ]
