# Generated by Django 5.0.1 on 2024-05-15 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]