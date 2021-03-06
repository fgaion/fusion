# Generated by Django 3.1.3 on 2021-04-30 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210429_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('recurso', models.CharField(max_length=100, verbose_name='Recurso')),
                ('descricao', models.TextField(max_length=200, verbose_name='Descrição')),
                ('icone', models.CharField(choices=[('lni-rocket', 'Foguete'), ('lni-laptop-phone', 'Laptop Phone'), ('lni-cog', 'Engrenagem'), ('lni-leaf', 'Design'), ('lni-layers', 'Templates')], max_length=16, verbose_name='Icone')),
            ],
            options={
                'verbose_name': 'Recurso',
                'verbose_name_plural': 'Recursos',
            },
        ),
    ]
