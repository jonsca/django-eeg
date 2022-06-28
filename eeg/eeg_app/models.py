from django.db import models

# Create your models here.

class Facility(models.Model):
    name = models.CharField()
    country = models.CharField()
    postalCode = models.CharField()

class Subject(models.Model):
    identifier = models.CharField()
    facilityId = models.ForeignKey(Facility, null=True)
    diagnosis = models.CharField()

class File(models.Model):
    subjectId = models.ForeignKey(Subject, on_delete=models.CASCADE)
    fileName = models.CharField()

class Channel(models.Model):
    name = models.CharField()
    unique = models.BooleanField()
    fileNameId = models.ForeignKey(File, null=True)

class Signal(models.Model):
    fileId = models.ForeignKey(File, on_delete=models.CASCADE)
    channelId = models.ForeignKey(Channel, on_delete=models.CASCADE)
    time = models.FloatField()
    voltage = models.FloatField()

class Downsample(models.Model):
    fileId = models.ForeignKey(File, on_delete=models.CASCADE)
    channelId = models.ForeignKey(Channel, on_delete=models.CASCADE)
    downSampledTrace= models.BinaryField()



