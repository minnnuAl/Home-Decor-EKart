# Generated by Django 4.2.3 on 2023-10-17 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_customer_login_productbuy_delete_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('amount', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=90)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=100)),
                ('oid', models.CharField(blank=True, max_length=150)),
                ('amountpaid', models.CharField(blank=True, max_length=500, null=True)),
                ('paymentstatus', models.CharField(blank=True, max_length=20)),
                ('phone', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
