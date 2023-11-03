# Generated by Django 4.2.7 on 2023-11-03 12:20

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_transferlearningmodel_dataset'),
    ]

    operations = [
        migrations.CreateModel(
            name='CapstoneData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(choices=[('MobileNetV3Small', 'MobileNetV3Small'), ('ResNet50', 'ResNet50'), ('EffecientNetB3', 'EffecientNetB3'), ('VGG19', 'VGG19'), ('XceptionNet', 'XceptionNet')], max_length=255)),
                ('batch_size', models.CharField(choices=[('16', '16'), ('32', '32'), ('64', '64'), ('128', '128')], default='16', max_length=4)),
                ('epochs', models.CharField(choices=[('25', 25), ('50', 50)], default='25', max_length=4)),
                ('learning_rate', models.CharField(choices=[('0.001', '0.001'), ('0.005', '0.005')], default='0.001', max_length=6)),
                ('optimizer', models.CharField(choices=[('Adam', 'Adam'), ('Adamax', 'Adamax'), ('RMSprop', 'RMSprop')], default='Adam', max_length=10)),
                ('dropout', models.CharField(blank=True, max_length=5)),
                ('dataset', models.CharField(choices=[('Original+Smote+Image Processing', 'Original+Smote+Image Processing'), ('Original+Image Processing', 'Original+Image Processing'), ('Original+Augmentation+Image Processing', 'Original+Augmentation+Image Processing')], default='Smote+Original+Image Processing', max_length=255)),
                ('training_accuracy', models.CharField(blank=True, max_length=3)),
                ('validation_accuracy', models.CharField(blank=True, max_length=3)),
                ('testing_accuracy', models.CharField(blank=True, max_length=3)),
                ('accuracy_graph', models.ImageField(blank=True, null=True, upload_to=core.models.graph_accuracy_image_file_path)),
                ('loss_graph', models.ImageField(blank=True, null=True, upload_to=core.models.graph_loss_image_file_path)),
            ],
        ),
        migrations.DeleteModel(
            name='TransferLearningModel',
        ),
    ]
