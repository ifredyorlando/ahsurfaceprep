# Generated by Django 3.0.4 on 2020-03-21 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0010_auto_20200321_0622'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='subtitle_paragrap',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aboutusimage',
            name='aboutus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.Aboutus'),
        ),
        migrations.AlterField(
            model_name='aboutusparagrap',
            name='aboutus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.Aboutus'),
        ),
        migrations.AlterField(
            model_name='backgroundimage',
            name='home',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.Home'),
        ),
        migrations.AlterField(
            model_name='galleryprojects',
            name='projects',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.Projects'),
        ),
        migrations.AlterField(
            model_name='homecard',
            name='home',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.Home'),
        ),
        migrations.AlterField(
            model_name='infocontactus',
            name='contactus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.Contactus'),
        ),
        migrations.AlterField(
            model_name='mapcontactus',
            name='contactus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.Contactus'),
        ),
        migrations.AlterField(
            model_name='navbarhome',
            name='home',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.Home'),
        ),
        migrations.AlterField(
            model_name='services',
            name='paragrap',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='servicesnavbar',
            name='services',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.Services'),
        ),
    ]
