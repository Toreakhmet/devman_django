# Generated by Django 3.2 on 2024-04-02 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.ImageField(upload_to='Images'),
        ),
    ]
