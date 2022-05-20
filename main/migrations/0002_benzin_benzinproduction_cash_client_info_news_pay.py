# Generated by Django 3.2.9 on 2022-05-20 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Benzin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('payed', models.IntegerField()),
                ('discon_card', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='Info')),
                ('phone', models.IntegerField()),
                ('text', models.TextField(blank=True, null=True)),
                ('telegram_link', models.CharField(max_length=500)),
                ('instagram_link', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='News/')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('benzin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.benzin')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.client')),
            ],
        ),
        migrations.CreateModel(
            name='BenzinProduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('allow', models.IntegerField(choices=[(1, 'Ready'), (2, 'Accept'), (3, 'Refuse')], default=1)),
                ('day', models.DateField(auto_now_add=True)),
                ('benzin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.benzin')),
            ],
        ),
    ]
