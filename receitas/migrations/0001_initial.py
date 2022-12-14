# Generated by Django 4.1 on 2022-08-11 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receitas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.TextField()),
                ('valor', models.FloatField()),
                ('data', models.DateTimeField()),
            ],
            options={
                'ordering': ['id', 'descricao', 'valor', 'data'],
            },
        ),
    ]
