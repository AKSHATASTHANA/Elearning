# Generated by Django 4.1.6 on 2023-02-25 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Contact', models.CharField(max_length=10)),
            ],
        ),
    ]
