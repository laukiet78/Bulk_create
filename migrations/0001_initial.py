# Generated by Django 2.2.2 on 2019-06-06 18:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vender_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('po_number', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('items_ordered', models.IntegerField(default=1)),
                ('vender', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ppl_order_tracking.Vender')),
            ],
        ),
        migrations.CreateModel(
            name='ItemsArrived',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_recieved', models.DateField()),
                ('items_received', models.IntegerField(default=0)),
                ('po_number', models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='ppl_order_tracking.PurchaseOrder')),
            ],
            options={
                'verbose_name_plural': 'Items Arrived',
            },
        ),
    ]
