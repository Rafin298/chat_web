# Generated by Django 4.0.1 on 2024-03-19 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_message_file_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='file_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]