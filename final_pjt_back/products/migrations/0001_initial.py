# Generated by Django 4.2.13 on 2024-05-17 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepositProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField(unique=True)),
                ('fin_co_no', models.IntegerField()),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('etc_note', models.TextField()),
                ('join_deny', models.IntegerField()),
                ('join_member', models.TextField()),
                ('join_way', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('mtrt_int', models.TextField()),
                ('max_limit', models.IntegerField(null=True)),
                ('dcls_strt_day', models.CharField(max_length=10, null=True)),
                ('dcls_end_day', models.CharField(max_length=10, null=True)),
                ('fin_co_subm_day', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SavingProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField(unique=True)),
                ('fin_co_no', models.IntegerField()),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('etc_note', models.TextField()),
                ('join_deny', models.IntegerField()),
                ('join_member', models.TextField()),
                ('join_way', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('mtrt_int', models.TextField()),
                ('max_limit', models.IntegerField(null=True)),
                ('dcls_strt_day', models.CharField(max_length=10, null=True)),
                ('dcls_end_day', models.CharField(max_length=10, null=True)),
                ('fin_co_subm_day', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SavingOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField()),
                ('intr_rate_type_nm', models.CharField(max_length=100)),
                ('intr_rate', models.FloatField()),
                ('intr_rate2', models.FloatField()),
                ('save_trm', models.IntegerField()),
                ('rsrv_type', models.CharField(max_length=10)),
                ('rsrv_type_nm', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.savingproduct')),
            ],
        ),
        migrations.CreateModel(
            name='DepositOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField()),
                ('intr_rate_type_nm', models.CharField(max_length=100)),
                ('intr_rate', models.FloatField()),
                ('intr_rate2', models.FloatField()),
                ('save_trm', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.depositproduct')),
            ],
        ),
    ]
