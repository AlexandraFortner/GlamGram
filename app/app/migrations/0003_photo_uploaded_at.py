# Generated by Django 2.0 on 2017-12-21 15:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20171218_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
