# Generated by Django 2.2.5 on 2019-09-21 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Course', models.CharField(max_length=50)),
                ('Admission_No', models.IntegerField()),
            ],
        ),
    ]