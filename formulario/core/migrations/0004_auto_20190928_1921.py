# Generated by Django 2.2.5 on 2019-09-28 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190928_1921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='datacadastro',
            new_name='dataCadastro',
        ),
    ]