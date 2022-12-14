# Generated by Django 3.1.5 on 2021-06-13 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0022_traderlink_report_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traderlink',
            name='purchase_contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_contract_link', to='contracts.contractproduct'),
        ),
        migrations.AlterField(
            model_name='traderlink',
            name='sale_contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_contract_link', to='contracts.contractproduct'),
        ),
    ]
