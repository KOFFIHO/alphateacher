# Generated by Django 3.1 on 2021-02-26 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Defile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='stock')),
                ('description', models.TextField()),
                ('image2', models.ImageField(upload_to='stock')),
                ('description1', models.TextField()),
                ('image3', models.ImageField(upload_to='stock')),
                ('description2', models.TextField()),
                ('telephone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Formulaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('ville', models.CharField(max_length=100)),
                ('prix', models.IntegerField(blank=True, default=0, null=True)),
                ('quartier', models.CharField(max_length=100)),
                ('matiere', models.CharField(max_length=500)),
                ('commune', models.CharField(blank=True, max_length=100, null=True)),
                ('cv', models.FileField(blank=True, upload_to='photoform')),
                ('experience', models.CharField(max_length=50)),
                ('niveau', models.CharField(max_length=200)),
                ('niveauEnsei', models.CharField(max_length=1000)),
                ('telephone', models.CharField(max_length=50)),
                ('photopi', models.FileField(blank=True, upload_to='photoform')),
                ('phOto', models.ImageField(blank=True, upload_to='photoform')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='note')),
                ('nom', models.CharField(max_length=100)),
                ('matiere', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Offre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Repetiteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('ville', models.CharField(max_length=100)),
                ('prix', models.IntegerField(blank=True, null=True)),
                ('commune', models.CharField(blank=True, max_length=100, null=True)),
                ('quartier', models.CharField(max_length=100)),
                ('matiere', models.CharField(max_length=500)),
                ('cv', models.FileField(blank=True, null=True, upload_to='stokRepetiteur')),
                ('experience', models.IntegerField()),
                ('niveau', models.CharField(max_length=200)),
                ('niveauEnsei', models.CharField(max_length=1000)),
                ('telephone', models.IntegerField()),
                ('photopi', models.FileField(upload_to='stokRepetiteur')),
                ('phOto', models.ImageField(upload_to='stokRepetiteur')),
            ],
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
    ]
