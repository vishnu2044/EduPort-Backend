from django.core.management.base import BaseCommand
from metacontent.models.qualification import Qualification
from metacontent.resources.qualification_list import qualifications

class Command(BaseCommand):
    help = 'Add qualifications in bulk'

    def handle(self, *args, **kwargs):

        qualification_objects = [Qualification(**qualification) for qualification in qualifications]
        Qualification.objects.bulk_create(qualification_objects)

        self.stdout.write(self.style.SUCCESS('Successfully added Qualifications in bulk'))


# import_qualifications