# Generated by Django 3.0.5 on 2020-04-14 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200414_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='discount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='mallId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Mall'),
        ),
    ]
