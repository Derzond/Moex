# Generated by Django 4.1 on 2022-08-26 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last', models.FloatField(null=True)),
                ('bid', models.FloatField(null=True)),
                ('ask', models.FloatField(null=True)),
                ('high', models.FloatField(null=True)),
                ('low', models.FloatField(null=True)),
                ('open', models.FloatField(null=True)),
                ('previousClose', models.FloatField(null=True)),
                ('timestamp', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Silver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last', models.FloatField(null=True)),
                ('bid', models.FloatField(null=True)),
                ('ask', models.FloatField(null=True)),
                ('high', models.FloatField(null=True)),
                ('low', models.FloatField(null=True)),
                ('open', models.FloatField(null=True)),
                ('previousClose', models.FloatField(null=True)),
                ('timestamp', models.DateTimeField(null=True)),
            ],
        ),
        migrations.AddIndex(
            model_name='silver',
            index=models.Index(fields=['timestamp'], name='exchange_si_timesta_e6e5f0_idx'),
        ),
        migrations.AddIndex(
            model_name='gold',
            index=models.Index(fields=['timestamp'], name='exchange_go_timesta_6f168d_idx'),
        ),
    ]
