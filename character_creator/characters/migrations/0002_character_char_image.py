# Generated by Django 2.1 on 2018-08-07 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='char_image',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
