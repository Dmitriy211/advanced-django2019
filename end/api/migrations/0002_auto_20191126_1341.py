# Generated by Django 2.2.6 on 2019-11-26 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='color',
            field=models.PositiveSmallIntegerField(choices=[(1, 'red'), (2, 'green'), (3, 'blue')], default=1),
        ),
    ]