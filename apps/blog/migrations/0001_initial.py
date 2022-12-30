# Generated by Django 4.1.4 on 2022-12-30 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='blog/')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
