from profiles.models import Profile, Country
import csv
from datetime import datetime

from django.db import IntegrityError
from django.core.exceptions import ValidationError

incorrect_countries = {}
incorrect_structures = {}
incorrect_domains = {}
incorrect_modalities = {}
incorrect_methods = {}

structures_transl = {
    'Neuron': 'N',
    'Layer': 'L',
    'Column': 'C',
    'Region': 'R',
    'Whole brain': 'W',
}

domains_transl = {
    'Cognition (general)': 'CG',
    'Sleep': 'SL',
    'Consciousness': 'CN',
    'Memory': 'MM',
    'Sensory': 'SS',
    'Language': 'LG',
    'Emotion': 'EM',
    'Pain': 'PN',
    'Learning': 'LE',
    'Developmental': 'DV',
    'Clinical (general)': 'CL',
    'Dementia': 'DM',
    'Parkinson': 'PK',
    'Psychiatry': 'PS',
    'Addiction': 'AD',
    'Oncology': 'ON',
    'Degenerative diseases': 'DD',
}
modalities_transl = {
    'Electrophysiology (EEG': 'EP',
    'MRI': 'MR',
    'PET': 'PE',
    'DTI': 'DT',
    'Behavioural': 'BH',
    'Eye Tracking': 'ET',
    'Brain Stimulation': 'BS',
    'Genetics': 'GT',
    'fNIRS': 'FN',
}
methods_transl = {
    'Univariate': 'UV',
    'Multivariate': 'MV',
    'Predictive Models': 'PM',
    'Predictive models': 'PM',
    'DCM': 'DC',
    'Connectivity': 'CT',
    'Computational Modeling': 'CM',
    'Computational modelling': 'CM',
}

with open('scripts/win.tsv', newline='', encoding="utf8") as csvfile:
    spamreader = list(csv.reader(csvfile, delimiter='\t', quotechar='|'))[1:]
    for row in spamreader:
        pd = datetime.strptime(row[0]+' UTC', '%d/%m/%Y %H:%M:%S %Z')
        countryResults = Country.objects.filter(name=row[3])

        kw = row[12]
        grad_date = row[7].split('/')
        gm = ""
        gy = ""
        if len(grad_date) > 2:
            gm = grad_date[1]
            gy = grad_date[2]

        # brainStructure = '['
        brainStructure = []
        bs = row[8].split(',')
        for sstruct in bs:
            struct = sstruct.strip()
            if struct in structures_transl:
                # brainStructure += "'%s', " % structures_transl[struct]
                brainStructure.append(structures_transl[struct])
            else:
                if struct not in (""):
                    # print('  Warning - %s: unknown Brain Structure: %s' % (row[1], struct))
                    if kw != "":
                        kw += ", %s" % struct
                    else:
                        kw = struct

                    if struct in incorrect_structures:
                        incorrect_structures[struct] += 1
                    else:
                        incorrect_structures[struct] = 1
        # if len(brainStructure) > 2:
        #     brainStructure = brainStructure[:-2] + ']'
        # else:
        #     brainStructure = '[]'

        # domains = '['
        domains = []
        dom = row[9].split(',')
        for dd in dom:
            d = dd.strip()
            if d in domains_transl:
                # domains += "'%s', " % domains_transl[d]
                domains.append(domains_transl[d])
            else:
                if d not in (""):
                    # print('  Warning - %s: unknown Domain: %s' % (row[1], d))
                    if kw != "":
                        kw += ", %s" % d
                    else:
                        kw = d

                    if d in incorrect_domains:
                        incorrect_domains[d] += 1
                    else:
                        incorrect_domains[d] = 1
        # if len(domains) > 2:
        #     domains = domains[:-2] + ']'
        # else:
        #     domains = "[]"

        # modalities = '['
        modalities = []
        mod = row[10].split(',')
        for mm in mod:
            m = mm.strip()
            if m in modalities_transl:
                # modalities += "'%s', " % modalities_transl[m]
                modalities.append(modalities_transl[m])
            else:
                if m not in ('MEG', 'ECoG)', ""):
                    # print('  Warning - %s: unknown Modality: %s' % (row[1], m))
                    if kw != "":
                        kw += ", %s" % m
                    else:
                        kw = m

                    if m in incorrect_modalities:
                        incorrect_modalities[m] += 1
                    else:
                        incorrect_modalities[m] = 1
        # modalities = modalities[:-2] + ']'

        # methods = '['
        methods = []
        met = row[11].split(',')
        for mmtt in met:
            mt = mmtt.strip()
            if mt in methods_transl:
                # methods += "'%s', " % methods_transl[mt]
                methods.append(methods_transl[mt])
            else:
                if mt not in (""):
                    # print('  Warning - %s: unknown Method: %s' % (row[1], mt))
                    if kw != "":
                        kw += ", %s" % mt
                    else:
                        kw = mt

                    if mt in incorrect_methods:
                        incorrect_methods[mt] += 1
                    else:
                        incorrect_methods[mt] = 1
        # methods = methods[:-2] + ']'
        
        if countryResults:
            p = Profile(
                    name = row[1],
                    institution = row[2],
                    country = countryResults[0],
                    email = row[4],
                    position = row[5],
                    webpage = row[6],
                    grad_month = gm,
                    grad_year = gy,
                    brain_structure = brainStructure,
                    domains = domains,
                    modalities = modalities,
                    methods = methods,
                    keywords = kw,
                    publish_date = pd.strftime('%Y-%m-%d %H:%M:%S'),
                    # last_updated = pd.strftime('%Y-%m-%d %H:%M:%S'),
            )

            if row[7]:
                gd = row[7].split('/')
                p.grad_date = '%s-%s-%s' % (gd[2], gd[1], gd[0])


            try:
                p.save()
            except IntegrityError as ie:
                print('%s - integrity error: %s' % (row[1], ie))
            except ValidationError as ve:
                print('%s - validation error: %s' % (row[1], ve))
    
        else:
            if row[3] in incorrect_countries:
                incorrect_countries[row[3]] += 1
            else:
                incorrect_countries[row[3]] = 1
                
print('========= Incorrect countries ==========')
for key in incorrect_countries:
    print('%s: (%s occurrences)' % (key, incorrect_countries[key]))
