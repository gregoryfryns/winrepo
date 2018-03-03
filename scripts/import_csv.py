from viewlist.models import Profile, Country
import csv

rejected_values = {}
with open('scripts/win.tsv', newline='') as csvfile:
    spamreader = list(csv.reader(csvfile, delimiter='\t', quotechar='|'))
    for row in spamreader:
        # name = row[1]
        # email = row[2]
        # webpage = row[3]
        # institution = row[4]
        # country = row[5]
        # position = row[6]
        # grad_date = row[7]
        # brain_structure = row[8]
        # modalities = row[9]
        # methods = row[10]
        # domain = row[11]
        # keywords = row[12]
        # publish_date = row[13]
        # last_updated = row[14]

        name = row[1]
        institution = row[2]
        country = row[3]
        email = row[4]
        position = row[5]
        webpage = row[6]
        grad_date = row[7]
        brain_structure = row[8]
        domain = row[9]
        modalities = row[10]
        methods = row[11]
        keywords = row[12]
        publish_date = row[0]
        last_updated = row[0]

        countryResults = Country.objects.filter(name=country)
        
        if len(countryResults) <= 0:
            if country in rejected_values:
                rejected_values[country] += 1
            else:
                rejected_values[country] = 1

for entry in rejected_values:
    print('%s (%s occurrences)' % (entry, rejected_values[entry]))


# for country in countries_list:
# 	c = Country(
# 			code = country[0],
# 			name = country[1],
# 			is_under_represented = False,
# 		)
# 	c.save()