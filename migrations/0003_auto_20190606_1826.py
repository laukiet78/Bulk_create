# Generated by Django 2.2.2 on 2019-06-06 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppl_order_tracking', '0002_auto_20190606_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='po_number',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]