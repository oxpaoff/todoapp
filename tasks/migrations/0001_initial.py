# Generated by Django 3.1.7 on 2021-12-13 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=50)),
                ('created', models.DateField(auto_now_add=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
