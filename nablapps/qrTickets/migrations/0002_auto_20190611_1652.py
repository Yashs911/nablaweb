# Generated by Django 2.1.9 on 2019-06-11 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qrTickets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QrEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='qrticket',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='qrTickets.QrEvent'),
            preserve_default=False,
        ),
    ]
