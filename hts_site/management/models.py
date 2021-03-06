from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    status = models.TextField()
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    pi = models.CharField(max_length=500)
    billing_account = models.CharField(max_length=500)
    department = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Flowcell(models.Model):
    label = models.TextField()
    status = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    qc_url = models.TextField()

    def __str__(self):
        return self.label


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Kit(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Index(models.Model):
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Sample(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE)
    label = models.CharField(max_length=500)
    project_description = models.CharField(max_length=500)
    organism = models.CharField(max_length=500)
    sequencer = models.CharField(max_length=500)
    alignment_genome = models.CharField(max_length=500)
    sample_type = models.CharField(max_length=500)
    dna_conc_ul = models.FloatField()
    determined_by = models.CharField(max_length=100)
    dna_conc_ul = models.FloatField()
    avg_len_lib = models.CharField(max_length=50)
    sample_vol = models.FloatField()
    read_length = models.CharField(max_length=50)
    kit_other = models.CharField(max_length=500)
    index_type = models.TextField()  # barcodes
    comments = models.TextField()
    other_variables = models.TextField()
    sequence_url = models.TextField()
    quality_url = models.TextField()
    status = models.TextField()

    def __str__(self):
        return self.label


# Lane/Cell
class Lane(models.Model):
    flowcell = models.ForeignKey(Flowcell, on_delete=models.CASCADE)
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    # user is a convenience attribute, can be obtained by going Lane -> sample -> project -> user
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    flowcell_element_control = models.BooleanField()
    flowcell_element_concentration = models.FloatField()

    def __str__(self):
        return '<Lane>: Sample: {0}, ID: {1}'.format(self.sample, self.id)
