from profiles.models import Profile, Country
import csv
from datetime import datetime

from django.db import IntegrityError
from django.core.exceptions import ValidationError

incorrect_countries = {}
with open('scripts/win.tsv', newline='', encoding="utf8") as csvfile:
    spamreader = list(csv.reader(csvfile, delimiter='\t', quotechar='|'))[1:]
    for row in spamreader:

        pd = datetime.strptime(row[0]+' UTC', '%d/%m/%Y %H:%M:%S %Z')
        countryResults = Country.objects.filter(name=row[3])
        
        if countryResults:
            p = Profile(
                    name = row[1],
                    institution = row[2],
                    country = countryResults[0],
                    email = row[4],
                    position = row[5],
                    webpage = row[6],
                    brain_structure = row[8],
                    domains = row[9],
                    modalities = row[10],
                    methods = row[11],
                    keywords = row[12],
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