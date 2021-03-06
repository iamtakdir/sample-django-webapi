# Generated by Django 2.1 on 2020-07-18 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.RemoveField(
            model_name='member',
            name='title',
        ),
        migrations.AlterField(
            model_name='member',
            name='designation',
            field=models.CharField(max_length=250),
        ),
        migrations.DeleteModel(
            name='Designation',
        ),
        migrations.AddField(
            model_name='member',
            name='name',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='members.Name'),
            preserve_default=False,
        ),
    ]
