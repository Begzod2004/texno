# Generated by Django 4.0.4 on 2022-06-30 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('technique', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aksiya_Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Color', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Features', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Material', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Region', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='condition',
            old_name='condition',
            new_name='Condition',
        ),
        migrations.RenameField(
            model_name='size',
            old_name='size',
            new_name='Size',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technique', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='technique.technique')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='technique.user')),
            ],
        ),
        migrations.CreateModel(
            name='Aksiya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('old_price', models.FloatField()),
                ('new_price', models.FloatField()),
                ('abaut', models.CharField(max_length=500)),
                ('img', models.ImageField(upload_to='static/images')),
                ('chegirma', models.IntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='technique.brand')),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='technique.aksiya_code')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='technique.color')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='technique.company')),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='technique.condition')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='technique.country')),
                ('features', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='technique.features')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='technique.size')),
            ],
        ),
        migrations.AddField(
            model_name='technique',
            name='features',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='technique.features'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='technique',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='technique.color'),
        ),
        migrations.AlterField(
            model_name='technique',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='technique.country'),
        ),
    ]
