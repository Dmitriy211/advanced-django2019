# Generated by Django 2.2.5 on 2019-10-01 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_taskcomment_task'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('name', 'status')},
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'DONE'), (2, 'DOING'), (3, 'TODO')], default=3),
        ),
        migrations.AlterUniqueTogether(
            name='task',
            unique_together={('project', 'name')},
        ),
        migrations.RemoveField(
            model_name='task',
            name='block',
        ),
        migrations.DeleteModel(
            name='Block',
        ),
    ]