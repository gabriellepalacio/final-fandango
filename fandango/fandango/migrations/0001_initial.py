# Generated by Django 2.0 on 2018-04-24 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('poster', models.URLField()),
                ('rating', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Showtime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=10)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fandango.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Theater', max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('lat', models.DecimalField(decimal_places=4, max_digits=15, null=True)),
                ('long', models.DecimalField(decimal_places=4, max_digits=15, null=True)),
                ('theater_id', models.CharField(max_length=10, unique=True)),
                ('city', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='showtime',
            name='theater',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='fandango.Theater'),
        ),
    ]