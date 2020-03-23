# Generated by Django 3.0.4 on 2020-03-20 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20200313_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='image',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='paragrap',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='ubication',
        ),
        migrations.RemoveField(
            model_name='home',
            name='navbaritem',
        ),
        migrations.RemoveField(
            model_name='home',
            name='paragrap',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='image',
        ),
        migrations.RemoveField(
            model_name='services',
            name='navbaritem',
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='subtitle',
            field=models.CharField(default='', editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='title',
            field=models.CharField(default='', editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='services',
            name='paragrap',
            field=models.TextField(max_length=255),
        ),
        migrations.CreateModel(
            name='ServicesNavbar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('navbaritem', models.CharField(max_length=50)),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.Services')),
            ],
        ),
        migrations.CreateModel(
            name='Navbarhome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('navbaritem', models.CharField(max_length=50)),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.Home')),
            ],
        ),
        migrations.CreateModel(
            name='MapContactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubication', models.CharField(max_length=255)),
                ('contactus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.Contactus')),
            ],
        ),
        migrations.CreateModel(
            name='InfoContactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=50)),
                ('contactus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.Contactus')),
            ],
        ),
        migrations.CreateModel(
            name='Galleryprojects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.Projects')),
            ],
        ),
        migrations.CreateModel(
            name='BackgroundImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.Home')),
            ],
        ),
        migrations.CreateModel(
            name='Aboutusparagrap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragrap', models.TextField(default='', editable=False, max_length=255)),
                ('aboutus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.Aboutus')),
            ],
        ),
        migrations.CreateModel(
            name='Aboutusimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', editable=False, upload_to='images/')),
                ('aboutus', models.ForeignKey(default='', editable=False, on_delete=django.db.models.deletion.CASCADE, to='page.Aboutus')),
            ],
        ),
    ]