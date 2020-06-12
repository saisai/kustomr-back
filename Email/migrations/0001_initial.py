# Generated by Django 3.0.6 on 2020-06-11 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Customer', '0005_auto_20200609_2042'),
        ('Vendor', '0003_auto_20200608_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailCampaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sendgrid_id', models.PositiveIntegerField(blank=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('subject', models.TextField()),
                ('content', models.TextField()),
                ('template', models.CharField(max_length=255)),
                ('send_at', models.DateTimeField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('to', models.ManyToManyField(related_name='mail_campaigns', to='Customer.Customer')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mail_campaigns', to='Vendor.Vendor')),
            ],
        ),
    ]