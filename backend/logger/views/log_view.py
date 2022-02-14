# Django Imports:
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import View
from django.shortcuts import render

# Models Imports:
from logger.models.log_details_model import LogDetails
from logger.models.log_model import Log

# Application Import:
from logger.logger import Logger

class Test(View, PermissionRequiredMixin):


    permission_required = 'log.read_write'

    def get(self, request, *args, **kwargs):

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

        # Return valid page with provided or default data:
        return render(request, 'test.html', data)
