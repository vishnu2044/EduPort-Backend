# your_app/management/commands/bulk_add_data.py

from django.core.management.base import BaseCommand
from metacontent.models.country import Country
from metacontent.models.state import State
from metacontent.resources.country_list import countries
from metacontent.resources.state_list import states

class Command(BaseCommand):
    help = 'Add countries and states in bulk'

    def handle(self, *args, **kwargs):


        country_objects = [Country(name=country["name"]) for country in countries]
        Country.objects.bulk_create(country_objects)

        country_name_to_instance = {country.name: country for country in Country.objects.all()}
 
        state_objects = [
            State(name=state["name"], country=country_name_to_instance[state["country_name"]])
            for state in states
        ]
        State.objects.bulk_create(state_objects)

        self.stdout.write(self.style.SUCCESS('Successfully added countries and states in bulk'))


#  import_state_and_countries