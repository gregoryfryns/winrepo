from django.db import models
from django.utils import timezone

from multiselectfield import MultiSelectField

class Country(models.Model):
    code = models.CharField(max_length=3, blank=False, unique=True)
    name = models.CharField(max_length=60, blank=False)
    is_under_represented = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "countries"
        
    def __str__(self):
        return self.name


class Profile(models.Model):
    PHD = 'PhD student'
    MDR = 'Medical Doctor'
    PDR = 'Post-doctoral researcher'
    SRE = 'Senior researcher/ scientist'
    LEC = 'Lecturer'
    ATP = 'Assistant Professor'
    ACP = 'Associate Professor'
    PRF = 'Professor'
    DIR = 'Group leader/ Director/ Head of Department'
    
    POSITION_CHOICES = (
        (PHD, 'PhD student'),
        (MDR, 'Medical Doctor'),
        (PDR, 'Post-doctoral researcher'),
        (SRE, 'Senior researcher/ scientist'),
        (LEC, 'Lecturer'),
        (ATP, 'Assistant Professor'),
        (ACP, 'Associate Professor'),
        (PRF, 'Professor'),
        (DIR, 'Group leader/ Director/ Head of Department')
    )

    STRUCTURE_CHOICES = (
        ('N', 'Neuron'),
        ('L', 'Layer'),
        ('C', 'Column'),
        ('R', 'Region'),
        ('W', 'Whole Brain')
    )
    
    MODALITIES_CHOICES = (
        ('EP', 'Electrophysiology (EEG, MEG, ECoG)'),
        ('MR', 'MRI'),
        ('PE', 'PET'),
        ('DT', 'DTI'),
        ('BH', 'Behavioural'),
        ('ET', 'Eye Tracking'),
        ('BS', 'Brain Simulation'),
        ('GT', 'Genetics'),
        ('FN', 'fNIRS')
    )

    METHODS_CHOICES = (
        ('UV', 'Univariate'),
        ('MV', 'Multivariate'),
        ('PM', 'Predictive Models'),
        ('DC', 'DCM'),
        ('CT', 'Connectivity'),
        ('CM', 'Computational Modeling')
    )

    DOMAIN_CHOICES = (
        ('CG', 'Cognition (general)'),
        ('SL', 'Sleep'),
        ('CN', 'Consciousness'),
        ('MM', 'Memory'),
        ('SS', 'Sensory'),
        ('LG', 'Language'),
        ('EM', 'Emotion'),
        ('PN', 'Pain'),
        ('LE', 'Learning'),
        ('DV', 'Developmental'),
        ('CL', 'Clinical (general)'),
        ('DM', 'Dementia'),
        ('PK', 'Parkinson'),
        ('PS', 'Psychiatry'),
        ('AD', 'Addiction'),
        ('ON', 'Oncology'),
        ('DD', 'Degenerative diseases'),
    )

    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=True)
    webpage = models.URLField(blank=True)
    institution = models.CharField(max_length=100, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES, blank=True)
    grad_date = models.DateField(null=True, blank=True)
    brain_structure = MultiSelectField(choices=STRUCTURE_CHOICES, blank=True)
    modalities = MultiSelectField(choices=MODALITIES_CHOICES, blank=True)
    methods = MultiSelectField(choices=METHODS_CHOICES, blank=True)
    domain = MultiSelectField(choices=DOMAIN_CHOICES, blank=True)
    keywords = models.CharField(max_length=250, blank=True)
    publish_date = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
        
    @property
    def is_senior(self):
        senior_keywords = ('Senior', 'Lecturer', 'Professor', 'Director', 'Principal')
        return any(keyword in self.position for keyword in senior_keywords)

class Recommendation(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100, blank=False)
    reviewer_email = models.EmailField(blank=False)
    reviewer_position = models.CharField(max_length=30, blank=False)
    reviewer_institution = models.CharField(max_length=100, blank=False)
    seen_at_conf = models.BooleanField()
    comment = models.TextField(blank=False)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment[:50]
