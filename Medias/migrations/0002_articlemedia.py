# Generated by Django 3.0.6 on 2020-06-05 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='vendors/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
