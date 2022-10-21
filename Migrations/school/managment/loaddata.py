from django.core.management.base import BaseCommand
import json
from school.models import Teacher, Student


class Command(BaseCommand):
    help = u'Внесение данных из json-файла в БД'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help=u'Путь к json-файлу')

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for item in data:
            if item['model'] == 'school.student':
                instance = Student(id=item['pk'],
                                   name=item['fields']['name'],
                                   teacher=item['fields']['teacher'],
                                   group=item['fields']['group'])
                instance.save()
            if item['model'] == 'school.teacher':
                instance = Student(id=item['pk'],
                                   name=item['fields']['name'],
                                   subject=item['fields']['subject'])
                instance.save()



