# Django Imports:
from django.views.generic import View

# Base view Import:
from .subclasses.pagination import Pagination
from .subclasses.filtration import Filtration


# Base view class: subclasses 
class BaseView(View, Pagination, Filtration):
    """
        Base View.
    """

    # Class attributes:
    template = None
    page_name = None
    panel = None

    # GET request response page:
    def get(self, request, *args, **kwargs):

        self.page_data = {
            'page_name': self._get_page_name()
        }

    def _collect_object(self, request):
        """ Collect all object using filter and pagination classes. """

        return self._get_filtered_object(request)

    def _get_page_name(self, text_to_display: str=None, plural: bool=False) -> str:
        """ Return given page name if provided, or generate standard page name. """

        # Check if page name is provided, if not generate newone:
        if self.page_name is None:

            # Collect model name:
            if plural is True:
                model_name = str(self.model._meta.verbose_name_plural)
            else:
                model_name = str(self.model._meta.verbose_name)

            # Generate a new page name:
            if text_to_display is None:
                return model_name
            else:
                return text_to_display + ' ' + model_name

    def _get_attribute(self, attribute, default):
        """ Return given attribute value if provided or default one if not provided. """

        # Value to return:
        output_template = None

        # Check if given attribute is provided, if not return newone:
        if attribute is None: 
            output_template = default
        else:
            output_template = attribute

        # Return value:
        return output_template

