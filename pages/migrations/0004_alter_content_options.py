# Generated by Django 3.2.3 on 2021-05-29 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_rename_links_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'verbose_name_plural': 'Contents'},
        ),
    ]
