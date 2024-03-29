# Generated by Django 2.2.6 on 2019-10-15 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductServiceBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productservicebase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.ProductServiceBase')),
                ('size', models.CharField(max_length=100)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Type1'), (2, 'Type2'), (3, 'Type3')])),
                ('existence', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
            bases=('api.productservicebase',),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('productservicebase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.ProductServiceBase')),
                ('approximate_duration', models.IntegerField()),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Type1'), (2, 'Type2'), (3, 'Type3')])),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
            bases=('api.productservicebase',),
        ),
    ]
