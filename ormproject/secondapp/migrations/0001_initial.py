# Generated by Django 5.0.3 on 2024-04-15 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='zaid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('password', models.CharField(default='', max_length=20)),
            ],
            options={
                'db_table': 'za',
            },
        ),
    ]