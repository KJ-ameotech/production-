# Generated by Django 4.2.6 on 2023-10-27 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0003_alter_document_id_proof'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='family_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]