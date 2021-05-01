# Generated by Django 2.2.3 on 2019-08-09 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('others', 'others')], max_length=50)),
                ('number', models.CharField(max_length=11)),
                ('description_of_illness', models.CharField(max_length=2000)),
                ('first_time_visit', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20)),
                ('preferred_doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Doctor.DoctorDetails')),
            ],
        ),
    ]