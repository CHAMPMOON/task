import json

from data.models import Data
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):

        with open('data.json', 'rb') as data_json:
            data = json.load(data_json)

            for elem in data:
                sensor_type = elem.get('Sensor_type')
                del elem['Sensor_type']

                Data.objects.create(**elem, sensor_type=sensor_type)
