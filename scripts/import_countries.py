import csv

from profiles.models import Country
from django.db import IntegrityError

with open('scripts/countries_list.tsv', newline='', encoding="utf8") as csvfile:
    spamreader = list(csv.reader(csvfile, delimiter='\t', quotechar='|'))[1:]
    for row in spamreader:
        c = Country(
            code=row[0],
            name=row[1],
            is_under_represented=(row[2]=='1')
        )
        c.save()    
