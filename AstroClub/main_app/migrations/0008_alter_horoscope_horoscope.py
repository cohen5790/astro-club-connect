# Generated by Django 4.0.2 on 2022-02-17 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_horoscope_horoscope'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horoscope',
            name='horoscope',
            field=models.CharField(choices=[('CP', 'Capricorn'), ('TA', 'Taurus'), ('GE', 'Gemini'), ('CA', 'Cancer'), ('LE', 'Leo'), ('VI', 'Virgo'), ('LI', 'Libra'), ('SC', 'Scorpio'), ('SA', 'Sagittarius'), ('AQ', 'Aquarius'), ('PI', 'Pisces'), ('AR', 'Aries')], default='Capricorn', max_length=2),
        ),
    ]