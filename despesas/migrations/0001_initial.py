# Generated by Django 4.1 on 2022-08-11 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DespesasModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=255)),
                ('valor', models.FloatField()),
                ('data', models.DateTimeField()),
            ],
            options={
                'db_table': 'despesas',
            },
        ),
    ]
