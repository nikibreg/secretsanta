# Generated by Django 2.1.4 on 2019-01-07 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('want', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('group', models.IntegerField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
