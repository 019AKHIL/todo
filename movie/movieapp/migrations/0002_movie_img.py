# Generated by Django 4.2.2 on 2023-07-02 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='sds', upload_to='pics'),
            preserve_default=False,
        ),
    ]
