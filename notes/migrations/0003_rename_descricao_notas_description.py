# Generated by Django 4.0.7 on 2024-02-16 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_rename_data_criado_notas_date_created_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notas',
            old_name='descricao',
            new_name='description',
        ),
    ]
