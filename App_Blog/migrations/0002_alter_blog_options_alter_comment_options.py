# Generated by Django 5.1 on 2025-06-28 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('-publish_date',)},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-comment_date',)},
        ),
    ]
