from django.core.management.base import BaseCommand
import json
from articles.models import Article


class Command(BaseCommand):
    help = u'Внесение данных из json-файла в БД'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help=u'Путь к json-файлу')

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for item in data:
            if item['model'] == 'articles.article':
                instance = Article(id=item['pk'],
                                title=item['fields']['title'],
                                text=item['fields']['text'],
                                published_at=item['fields']['published_at'],
                                image=item['fields']['image'])
                instance.save()






