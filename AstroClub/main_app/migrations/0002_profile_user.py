# Generated by Django 4.0.2 on 2022-02-15 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horoscope', models.CharField(choices=[('CA', 'Capricorn'), ('TA', 'Taurus'), ('GE', 'Gemini'), ('CA', 'Cancer'), ('LE', 'Leo'), ('VI', 'Virgo'), ('LI', 'Libra'), ('SC', 'Scorpio'), ('SA', 'Sagittarius'), ('AQ', 'Aquarius'), ('PI', 'Pisces')], default='CAPRICORN', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]