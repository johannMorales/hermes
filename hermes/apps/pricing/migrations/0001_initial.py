# Generated by Django 2.1.7 on 2019-03-16 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('includes_igv', models.BooleanField()),
                ('series', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
                ('date', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm.Contact')),
                ('payment_condition', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='store.PaymentCondition')),
            ],
            options={
                'db_table': 'cotizacion',
            },
        ),
        migrations.CreateModel(
            name='CotizacionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=10)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cotizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricing.Cotizacion')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.Product')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.MeasureUnit')),
            ],
            options={
                'db_table': 'cotizacion_item',
            },
        ),
    ]