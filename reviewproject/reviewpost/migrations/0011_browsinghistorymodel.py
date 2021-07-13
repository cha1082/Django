# Generated by Django 3.2.4 on 2021-07-08 05:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reviewpost', '0010_purchasehistorymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrowsingHistoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reviewpost.reviewmodel')),
            ],
        ),
    ]