# Generated by Django 2.2.2 on 2019-07-24 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_category_folder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='folder',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='main.Folder'),
        ),
    ]
