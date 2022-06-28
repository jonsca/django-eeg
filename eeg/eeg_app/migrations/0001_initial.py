# Generated by Django 4.0.5 on 2022-06-28 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('unique', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('postalCode', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileName', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.TextField()),
                ('diagnosis', models.TextField()),
                ('facilityId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='eeg_app.facility')),
            ],
        ),
        migrations.CreateModel(
            name='Signal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.FloatField()),
                ('voltage', models.FloatField()),
                ('channelId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eeg_app.channel')),
                ('fileId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eeg_app.file')),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='subjectId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eeg_app.subject'),
        ),
        migrations.CreateModel(
            name='Downsample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('downSampledTrace', models.BinaryField()),
                ('channelId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eeg_app.channel')),
                ('fileId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eeg_app.file')),
            ],
        ),
        migrations.AddField(
            model_name='channel',
            name='fileNameId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='eeg_app.file'),
        ),
    ]