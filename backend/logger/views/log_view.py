# Django Imports:
from django.shortcuts import render

# Models Imports:
from logger.models.log_details_model import LogDetails
from logger.models.log_model import Log

# Application Import:
from logger.logger import Logger

def test(request):
    data = {
        'output': 'RKKR'
    }

    lagdata = {
        'Test1': 'RKKR 1',
        'Test2': 'RKKR 2'
    }

    logger = Logger('Test', False)
    logger.debug('Test log', **lagdata)

    data['logs'] = Log.objects.all()

    return render(request, 'test.html', data)


# Test