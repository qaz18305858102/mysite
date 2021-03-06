# Generated by Django 4.0.4 on 2022-05-12 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('permission', models.CharField(default='员工', max_length=30)),
                ('USER_MMID', models.CharField(default='', max_length=30)),
                ('creat_time', models.DateTimeField(auto_now_add=True)),
                ('updtae_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('firstname', models.CharField(blank=True, max_length=30)),
                ('lastname', models.CharField(blank=True, max_length=30)),
                ('Email', models.CharField(max_length=30)),
                ('question', models.CharField(max_length=30)),
                ('answer', models.CharField(max_length=30)),
                ('creat_time', models.DateTimeField(auto_now_add=True)),
                ('updtae_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
