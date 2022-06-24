# Generated by Django 4.0.5 on 2022-06-24 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OldFormsDataBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=25)),
                ('dayoff', models.IntegerField()),
                ('personelid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.personeldatabase')),
            ],
        ),
    ]