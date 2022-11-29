# Generated by Django 3.2.16 on 2022-11-22 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("permission", "0001_initial"),
        ("app", "0017_app_audience"),
    ]

    operations = [
        migrations.AlterField(
            model_name="app",
            name="permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this app.",
                related_name="app_set",
                related_query_name="app",
                to="permission.Permission",
            ),
        ),
        migrations.AlterField(
            model_name="appextension",
            name="permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this app extension.",
                to="permission.Permission",
            ),
        ),
        migrations.AlterField(
            model_name="appinstallation",
            name="permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions which will be assigned to app.",
                related_name="app_installation_set",
                related_query_name="app_installation",
                to="permission.Permission",
            ),
        ),
    ]
