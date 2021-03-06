# Generated by Django 3.2 on 2021-05-03 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210503_0436'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solvestatus',
            old_name='last_code_path',
            new_name='last_code',
        ),
        migrations.AddField(
            model_name='challenge',
            name='description',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='challenge',
            name='result',
            field=models.CharField(default='Null', max_length=50),
            preserve_default=False,
        ),
    ]
