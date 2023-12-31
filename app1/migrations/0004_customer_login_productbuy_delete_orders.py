# Generated by Django 4.2.3 on 2023-10-17 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_orders_orderupdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_login',
            fields=[
                ('Customer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=20)),
                ('email', models.CharField(default='', max_length=20)),
                ('password', models.CharField(default='', max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('current_location', models.CharField(max_length=20)),
                ('phone_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductBuy',
            fields=[
                ('Buy_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Product_id', models.IntegerField()),
                ('ProductName', models.CharField(max_length=20)),
                ('Quantity', models.IntegerField()),
                ('Price', models.IntegerField()),
                ('Customer_id', models.IntegerField()),
                ('name', models.CharField(default='', max_length=20)),
                ('email', models.CharField(default='', max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('Status', models.CharField(default='', max_length=20)),
                ('payment_type', models.CharField(default='', max_length=20)),
                ('Transportor_id', models.IntegerField(default=0)),
                ('Transport_name', models.CharField(default='Not Taken Yet', max_length=20)),
                ('Transportor_phone', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
    ]
