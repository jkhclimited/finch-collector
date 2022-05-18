# Generated by Django 4.0.4 on 2022-05-18 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_rename_copy_owned_card'),
    ]

    operations = [
        migrations.CreateModel(
            name='EffectType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='effect_type',
            field=models.ManyToManyField(to='main_app.effecttype'),
        ),
    ]
