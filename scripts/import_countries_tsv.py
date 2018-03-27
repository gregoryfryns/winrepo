import csv

from django import forms

from profiles.models import Profile, Country

class ImportProfilesForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name',
            'email',
            'webpage',
            'institution',
            'country',
            'position',
            'grad_date',
            'brain_structure',
            'modalities',
            'methods',
            'domain',
            'keywords',
            'publish_date',
        ]

    def clean_country(self):
        country = self.cleaned_data['country']
        try:
            Country.objects.get(name=country)
        except Country.DoesNotExist:
            msg = '%s does not exist in the DB' % country
            raise forms.ValidationError(msg)

        return country

def import_profiles(path):
    records_added = 0
    errors = []
    with open(path, newline='', encoding="utf8") as rows:
        # Generate a dict per row, with the first CSV row being the keys.
        for row in csv.DictReader(rows, delimiter='\t', quotechar='|'):
            # Bind the row data to the PurchaseForm.
            form = ImportProfilesForm(row)
            # Check to see if the row data is valid.
            if form.is_valid():
                # Row data is valid so save the record.
                form.save()
                records_added += 1
            else:
                errors.append(form.errors)

    return records_added, errors
