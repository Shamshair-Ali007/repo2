# Generated by Django 5.1 on 2024-08-29 14:43

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='welcome',
            name='age',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
    ]
