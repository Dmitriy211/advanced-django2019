# Generated by Django 2.2.5 on 2019-09-25 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190925_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskcomment',
            name='task',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Task'),
            preserve_default=False,
        ),
    ]
