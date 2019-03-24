# Generated by Django 2.1.7 on 2019-03-18 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='type',
            field=models.CharField(choices=[('TYPE_JURIDICA', 'Persona Juridica'), ('TYPE_NATURAL', 'Persona Natural')], default='TYPE_JURIDICA', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='juridica',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.PersonaJuridica'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='natural',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.PersonaNatural'),
        ),
        migrations.AlterField(
            model_name='personajuridica',
            name='web',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]