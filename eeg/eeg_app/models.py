from django.db import models

# Create your models here.

class Facility(models.Model):
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    postalCode = models.CharField(max_length=10)

class Subject(models.Model):
    identifier = models.TextField()
    facilityId = models.ForeignKey(Facility, null=True, on_delete=models.DO_NOTHING)
    diagnosis = models.TextField()

class File(models.Model):
    subjectId = models.ForeignKey(Subject, on_delete=models.CASCADE)
    fileName = models.TextField()

class Channel(models.Model):
    name = models.CharField(max_length=20)
    unique = models.BooleanField()
    fileNameId = models.ForeignKey(File, null=True, on_delete=models.DO_NOTHING)

class Signal(models.Model):
    fileId = models.ForeignKey(File, on_delete=models.CASCADE)
    channelId = models.ForeignKey(Channel, on_delete=models.CASCADE)
    time = models.FloatField()
    voltage = models.FloatField()

class Downsample(models.Model):
    fileId = models.ForeignKey(File, on_delete=models.CASCADE)
    channelId = models.ForeignKey(Channel, on_delete=models.CASCADE)
    downSampledTrace= models.BinaryField()



