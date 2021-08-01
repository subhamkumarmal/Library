# Generated by Django 3.2.5 on 2021-08-01 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taker_name', models.CharField(max_length=40)),
                ('taker_add', models.CharField(max_length=100)),
                ('labrary_member', models.CharField(max_length=40)),
                ('book_id', models.IntegerField()),
                ('book_name', models.CharField(max_length=50)),
                ('book_issue_data', models.DateTimeField()),
            ],
            options={
                'db_table': 'Library',
            },
        ),
    ]
