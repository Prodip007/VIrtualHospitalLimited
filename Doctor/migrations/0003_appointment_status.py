# Generated by Django 2.2.3 on 2019-08-10 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0002_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed')], default='Pending', max_length=20, null=True),
        ),
    ]
