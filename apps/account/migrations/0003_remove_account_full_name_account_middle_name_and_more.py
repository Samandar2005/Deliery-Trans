# Generated by Django 4.1.4 on 2022-12-30 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_account_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='full_name',
        ),
        migrations.AddField(
            model_name='account',
            name='middle_name',
            field=models.CharField(max_length=50, null=True, verbose_name='Middle name'),
        ),
        migrations.AddField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='account',
            name='surname',
            field=models.CharField(max_length=50, null=True, verbose_name='Surname'),
        ),
    ]