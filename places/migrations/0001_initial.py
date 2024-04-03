# Generated by Django 3.2 on 2024-04-03 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Excursion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description_short', models.TextField()),
                ('description_long', models.TextField()),
                ('lng', models.FloatField()),
                ('lat', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(upload_to='Images')),
                ('count', models.IntegerField(default=0)),
                ('excursion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.excursion')),
            ],
        ),
    ]