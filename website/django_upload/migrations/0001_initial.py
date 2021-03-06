# Generated by Django 2.1.2 on 2018-10-18 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lab_Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(default='null', max_length=100)),
                ('Lab_Assignment', models.FileField(upload_to='')),
                ('Lab_Optional_Assignment', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Lab_Lectures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(default='null', max_length=100)),
                ('Lab_lectures', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Theory_Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(default='null', max_length=100)),
                ('Theory_Assignment', models.FileField(upload_to='')),
                ('submit_Date', models.CharField(default='null', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Theory_Lectures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(default='null', max_length=100)),
                ('Theory_Lectures', models.FileField(upload_to='')),
                ('Video_lectures', models.FileField(upload_to='')),
            ],
        ),
    ]
