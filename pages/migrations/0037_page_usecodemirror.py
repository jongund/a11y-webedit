# Generated by Django 2.1.7 on 2019-09-29 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0036_remove_page_togglecodehighlight'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='useCodeMirror',
            field=models.BooleanField(default=False),
        ),
    ]
