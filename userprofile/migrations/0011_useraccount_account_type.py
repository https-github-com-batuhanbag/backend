# Generated by Django 2.1.5 on 2021-08-18 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0010_delete_editoraccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='account_type',
            field=models.CharField(choices=[('accType1', 'User'), ('accType2', 'Editor')], default='accType1', max_length=10),
        ),
    ]