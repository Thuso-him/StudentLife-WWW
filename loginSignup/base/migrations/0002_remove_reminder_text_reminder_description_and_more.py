# Generated by Django 5.2 on 2025-04-08 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reminder',
            name='text',
        ),
        migrations.AddField(
            model_name='reminder',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='reminder',
            name='title',
            field=models.CharField(default='Untitled', max_length=200),
        ),
    ]
