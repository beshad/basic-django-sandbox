# Generated by Django 2.2.19 on 2021-05-29 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_content_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]