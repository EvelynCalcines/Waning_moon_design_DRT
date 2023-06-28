# Generated by Django 3.2.19 on 2023-06-28 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phone_case', '0005_auto_20230614_1901'),
        ('authentication', '0003_auto_20230628_2128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='phone_case',
            new_name='phonecase',
        ),
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together={('user', 'phonecase', 'text')},
        ),
    ]
