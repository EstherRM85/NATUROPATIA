# Generated by Django 2.2.10 on 2020-03-27 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EntradaBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=70)),
                ('descripcion', models.TextField(null=True)),
                ('fecha', models.DateTimeField()),
                ('imagen', models.ImageField(upload_to='static/img')),
            ],
        ),
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patologia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80, null=True)),
                ('descripcion', models.TextField(null=True)),
                ('imagen', models.ImageField(upload_to='static/img')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
                ('edad', models.IntegerField(null=True)),
                ('descripcion', models.TextField(null=True)),
                ('fecha_publicacion', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80, null=True)),
                ('descripcion', models.TextField(null=True)),
                ('imagen', models.ImageField(upload_to='static/img')),
            ],
        ),
    ]
