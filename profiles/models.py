from django.db import models
from django.utils import timezone

from multiselectfield import MultiSelectField

class Country(models.Model):
    code = models.CharField(max_length=3, blank=False, unique=True)
    name = models.CharField(max_length=60, blank=False)
    is_under_represented = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'countries'
        ordering = ['name']

    def __str__(self):
        return self.name
        

class Profile(models.Model):
    PHD = 'PhD student'
    MDR = 'Medical Doctor'
    PDR = 'Post-doctoral researcher'
    JRE = 'Researcher/ scientist'
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
        (JRE, 'Researcher/ scientist'),
        (SRE, 'Senior researcher/ scientist'),
        (LEC, 'Lecturer'),
        (ATP, 'Assistant Professor'),
        (ACP, 'Associate Professor'),
        (PRF, 'Professor'),
        (DIR, 'Group leader/ Director/ Head of Department')
    )

    MONTHS_CHOICES = (
        ('01', 'January'),
        ('02', 'February'),
        ('03', 'March'),
        ('04', 'April'),
        ('05', 'May'),
        ('06', 'June'),
        ('07', 'July'),
        ('08', 'August'),
        ('09', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December')
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
        ('OE', 'Other electrophysiology'),
        ('MR', 'MRI'),
        ('PE', 'PET'),
        ('DT', 'DTI'),
        ('BH', 'Behavioural'),
        ('ET', 'Eye Tracking'),
        ('BS', 'Brain Stimulation'),
        ('GT', 'Genetics'),
        ('FN', 'fNIRS'),
        ('LE','Lesions and Inactivations'),
    )

    METHODS_CHOICES = (
        ('UV', 'Univariate'),
        ('MV', 'Multivariate'),
        ('PM', 'Predictive Models'),
        ('DC', 'DCM'),
        ('CT', 'Connectivity'),
        ('CM', 'Computational Modeling'),
        ('AM', 'Animal Models')
    )

    DOMAINS_CHOICES = (
        ('CG', 'Cognition (general)'),
        ('MM', 'Memory'),
        ('SS', 'Sensory systems'),
        ('MO', 'Motor Systems'),
        ('LG', 'Language'),
        ('EM', 'Emotion'),
        ('PN', 'Pain'),
        ('LE', 'Learning'),
        ('AT', 'Attention'),
        ('DE', 'Decision Making'),
        ('DV', 'Developmental'),
        ('SL', 'Sleep'),
        ('CN', 'Consciousness'),
        ('CL', 'Clinical (general)'),
        ('DM', 'Dementia'),
        ('PK', 'Parkinson'),
        ('DD', 'Other degenerative diseases'),
        ('PS', 'Psychiatry'),
        ('AD', 'Addiction'),
        ('ON', 'Oncology'),
        ('EV', 'Evolutionary'),
        ('CM', 'Cellular and Molecular'),
        ('BI', 'Bioinformatics'),
        ('NC', 'Neuropharmacology'),
        ('ET', 'Ethics')
    )

    @classmethod
    def get_position_choices(cls):
        return cls.POSITION_CHOICES

    @classmethod
    def get_structure_choices(cls):
        return cls.STRUCTURE_CHOICES

    @classmethod
    def get_modalities_choices(cls):
        return cls.MODALITIES_CHOICES

    @classmethod
    def get_methods_choices(cls):
        return cls.METHODS_CHOICES

    @classmethod
    def get_domains_choices(cls):
        return cls.DOMAINS_CHOICES

    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=True)
    webpage = models.URLField(blank=True)
    institution = models.CharField(max_length=100, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES, blank=True)
    grad_month = models.CharField(max_length=2, choices=MONTHS_CHOICES, blank=True)
    grad_year = models.CharField(max_length=4, blank=True)
    brain_structure = MultiSelectField(choices=STRUCTURE_CHOICES, blank=True)
    modalities = MultiSelectField(choices=MODALITIES_CHOICES, blank=True)
    methods = MultiSelectField(choices=METHODS_CHOICES, blank=True)
    domains = MultiSelectField(choices=DOMAINS_CHOICES, blank=True)
    keywords = models.CharField(max_length=250, blank=True)
    publish_date = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name', 'institution', 'last_updated']

    def __str__(self):
        return f'{self.name}, {self.institution}'

    # @property
    # def is_senior(self):
    #     senior_keywords = ('Senior', 'Lecturer', 'Professor', 'Director', 'Principal')
    #     return any(keyword in self.position for keyword in senior_keywords)

    def brain_structure_labels(self):
        return [dict(self.STRUCTURE_CHOICES).get(item, item) for item in self.brain_structure]

    def modalities_labels(self):
        return [dict(self.MODALITIES_CHOICES).get(item, item) for item in self.modalities]

    def methods_labels(self):
        return [dict(self.METHODS_CHOICES).get(item, item) for item in self.methods]

    def domains_labels(self):
        return [dict(self.DOMAINS_CHOICES).get(item, item) for item in self.domains]

    def grad_month_labels(self):
        return dict(self.MONTHS_CHOICES).get(self.grad_month)


class Recommendation(models.Model):
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

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100, blank=False)
    reviewer_email = models.EmailField(blank=False)
    reviewer_position = models.CharField(max_length=50, choices=POSITION_CHOICES, blank=True)
    reviewer_institution = models.CharField(max_length=100, blank=False)
    seen_at_conf = models.BooleanField()
    comment = models.TextField(blank=False)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-last_updated']

    def __str__(self):
        return self.comment[:50]
