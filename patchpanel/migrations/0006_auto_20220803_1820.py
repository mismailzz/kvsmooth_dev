# Generated by Django 2.2 on 2022-08-03 18:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patchpanel', '0005_auto_20220803_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadvmpatchdb',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='uploadvmpatchdb',
            name='script',
            field=models.FileField(upload_to='documents/'),
        ),
    ]
