# Generated by Django 4.2.2 on 2024-02-09 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_formdata_type_of_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdata',
            name='Type_of_members',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='aadhar_no',
            field=models.CharField(max_length=100),
        ),
    ]
