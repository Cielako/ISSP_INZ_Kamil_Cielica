# Generated by Django 4.1 on 2022-12-10 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='region',
            field=models.CharField(choices=[('DŚ', 'Dolnośląskie'), ('KP', 'Kujawsko-pomorskie'), ('LB', 'Lubelskie'), ('LS', 'Lubuskie'), ('ŁD', 'Łódzkie'), ('MP', 'Małopolskie'), ('MZ', 'Mazowieckie'), ('OP', 'Opolskie'), ('PK', 'Podkarpackie'), ('PL', 'Podlaskie'), ('PM', 'Pomorskie'), ('ŚL', 'Śląskie'), ('ŚK', 'Świętokrzyskie'), ('WP', 'Wielkopolskie'), ('WM', 'Warmińsko-mazurskie'), ('ZP', 'Zachodnio-pomorskie')], default=1, max_length=19, verbose_name='Województwo'),
            preserve_default=False,
        ),
    ]
