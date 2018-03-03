from viewlist.models import Profile, Country
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from datetime import datetime
import csv

countryResults = Country.objects.filter(code='BE')

with open('scripts/win.tsv', newline='') as csvfile:
    spamreader = list(csv.reader(csvfile, delimiter='\t', quotechar='|'))[1:]
    for row in spamreader:

        pd = datetime.strptime(row[0]+' UTC', '%d/%m/%Y %H:%M:%S %Z')
        p = Profile(
                name = row[1],
                institution = row[2],
                # country = row[3],
                country = countryResults[0],
                email = row[4],
                position = row[5],
                webpage = row[6],
                brain_structure = row[8],
                domain = row[9],
                modalities = row[10],
                methods = row[11],
                keywords = row[12],
                publish_date = pd.strftime('%Y-%m-%d %H:%M:%S'),
                last_updated = pd.strftime('%Y-%m-%d %H:%M:%S'),
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
