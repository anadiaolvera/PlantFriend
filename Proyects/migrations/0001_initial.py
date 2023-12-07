# Generated by Django 4.2.7 on 2023-11-23 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModeloPrueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('proyecto_id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_finalizacion', models.DateField(blank=True, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='Proyects/static/Images')),
                ('PcreationDate', models.DateTimeField(auto_now_add=True)),
                ('PupdateDate', models.DateTimeField(auto_now=True)),
                ('estado_proyecto', models.CharField(choices=[('activo', 'Activo'), ('finalizado', 'Finalizado')], default='activo', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SocialCause',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('socialCauseTitle', models.CharField(max_length=100)),
                ('socialCauseDescription', models.TextField()),
                ('socialCauseImg', models.ImageField(blank=True, null=True, upload_to='Proyects/static/Images/SocialCause')),
                ('startingDate', models.DateField()),
                ('dueDate', models.DateField()),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.EmailField(help_text='Required. Enter a valid email address.', max_length=254, unique=True)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
    ]
