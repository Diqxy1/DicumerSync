# Generated by Django 3.0.8 on 2020-07-25 16:52

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='Nome')),
                ('last_name', models.CharField(max_length=150, verbose_name='Sobrenome')),
                ('customer_address', models.CharField(max_length=350, verbose_name='Endedreço')),
                ('customer_district', models.CharField(max_length=150, verbose_name='Bairro')),
                ('reference_address', models.CharField(max_length=150, verbose_name='Referência')),
                ('customer_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Telefone')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clientes',
                'ordering': ['first_name'],
            },
        ),
    ]