# Generated by Django 4.0.3 on 2022-04-24 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_list_phone_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='List',
        ),
        migrations.AddField(
            model_name='todo',
            name='address',
            field=models.CharField(default='nill', max_length=150),
        ),
        migrations.AddField(
            model_name='todo',
            name='phone_number',
            field=models.IntegerField(default='1234456776'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
