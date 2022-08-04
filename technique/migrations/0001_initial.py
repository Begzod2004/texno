# Generated by Django 4.0.5 on 2022-07-09 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
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
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Condition', models.CharField(max_length=50)),
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
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Size', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('img', models.ImageField(upload_to='')),
            ],
            options={
                'ordering': ['-username'],
            },
        ),
        migrations.CreateModel(
            name='Technique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('abaut', models.CharField(max_length=500)),
                ('img', models.ImageField(upload_to='static/images')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='technique.brand')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='technique.color')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='technique.company')),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='technique.condition')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='technique.country')),
                ('features', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='technique.features')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='technique.size')),
            ],
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
    ]
