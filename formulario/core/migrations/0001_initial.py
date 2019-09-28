# Generated by Django 2.2.5 on 2019-09-28 18:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medicos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80, verbose_name='Nome')),
                ('dataNascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('dataColeta', models.DateField(verbose_name='Data da Coleta')),
                ('dataEntrega', models.DateField(verbose_name='Data da Entrega')),
                ('statusEntrega', models.BooleanField(verbose_name='Status da Entrega')),
                ('codigoIdentificador', models.CharField(default=uuid.uuid1, max_length=100, unique=True)),
                ('cadastro', models.DateTimeField(auto_now_add=True)),
                ('CRM', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='clientes', to='medicos.Medico')),
            ],
        ),
    ]
