# Generated by Django 4.1.5 on 2023-01-31 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=300)),
                ('img1', models.ImageField(upload_to='pictures')),
                ('post', models.TextField()),
            ],
        ),
    ]
