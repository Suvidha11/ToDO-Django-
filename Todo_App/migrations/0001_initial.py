# Generated by Django 4.1.3 on 2023-03-02 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('Task', models.CharField(max_length=50)),
            ],
        ),
    ]