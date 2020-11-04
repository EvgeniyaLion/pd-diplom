# Generated by Django 2.2.10 on 2020-08-27 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Параметр')),
            ],
            options={
                'verbose_name': 'Название параметр',
                'verbose_name_plural': 'Названия параметров',
                'ordering': ('-name',),
            },
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.AlterField(
            model_name='shop',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на прайс для импорта товаров'),
        ),
        migrations.CreateModel(
            name='ProductParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50, verbose_name='Значение')),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_parameters', to='shop.Parameter', verbose_name='Параметр')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_parameters', to='shop.Product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Параметр товара',
                'verbose_name_plural': 'Параметры товаров',
            },
        ),
        migrations.AddConstraint(
            model_name='productparameter',
            constraint=models.UniqueConstraint(fields=('product', 'parameter'), name='unique_product_parameter'),
        ),
    ]