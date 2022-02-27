# Django Import:
from django.db.models import QuerySet

# Base Import:
from .base import Base

# Filtration class:
class Filtration(Base):

    filter_by = None
    list_filter = None
    text_filter = None
    boolean_filter = None
    queryset = None

    def _get_filter_template(self):
        """ Xxx. """

        def create_form(list_name, form_type, options = None):
            for filter_name in list_name:
                filter_attribute = self.collect_specific_model_attribute(filter_name)
                filters_template_form.append({
                    'name': filter_attribute.name,
                    'verbose_name': filter_attribute.verbose_name,
                    'help_text': filter_attribute.help_text,
                    'type': form_type,
                    'options': options
                })

        # Check if attributes are valid:
        self._attributes_check()

        # Template form list:
        filters_template_form = []

        # Complate template form values:
        if self.list_filter is not None:
            create_form(self.list_filter, 'list', ['Test 1', 'Test 2'])
        if self.text_filter is not None:
            create_form(self.text_filter, 'text')
        if self.boolean_filter is not None:
            create_form(self.boolean_filter, 'bool')

        self.page_data['filters'] = filters_template_form

    def _attributes_check(self):
        # Collect data to fill filter_by attribute:
        if self.list_filter is not None:
            if isinstance(self.list_filter, list):
                self.filter_by = []
            else:
                raise TypeError('Attribute list_filter must be a list.')
        if self.text_filter is not None:
            if isinstance(self.text_filter, list):
                self.filter_by = []
            else:
                raise TypeError('Attribute text_filter must be a list.')
        if self.boolean_filter is not None:
            if isinstance(self.boolean_filter, list):
                self.filter_by = []
            else:
                raise TypeError('Attribute boolean_filter must be a list.')

    def _get_filtered_objects(self, request):
        """ 
            Reterns all filtered object, in provided order.
            Based on provided request URL.
        """

        # Check if attributes are valid:
        self._attributes_check()

        # Collect data to fill filter_by attribute:
        if self.list_filter is not None:
            self.filter_by.extend(self.list_filter)
        if self.text_filter is not None:
            self.filter_by.extend(self.text_filter)
        if self.boolean_filter is not None:
            self.filter_by.extend(self.boolean_filter)

        # Collect all model attributes names:
        model_attributes_names = self.collect_model_attributes_names()
        # Check if filter_by list values are valid:
        if self.filter_by is not None:
            for value in self.filter_by:
                if value not in model_attributes_names:
                    # Raise error in case of value that is not valid model attribute:
                    raise TypeError('Attribute filter_by contains value that is not a valid model attribute.')

        # Check if filter_by value is None:
        if self.filter_by is None:

            # If filter_by value is None return all object or queryset if provided:
            if self.queryset is None:
                # Return all objects if queryset was not provided:
                return self.model.objects.all()
            else:
                # Return queryset object:
                if isinstance(self.queryset, QuerySet):
                    return self.queryset.all()
                else:
                    # Return all objects if queryset is incorrect:
                    return self.model.objects.all()

        else:

            # Collect GET request parameters:
            parameters = self.collect_get_parameters(request)

            # Valid all collected parameters:
            valid_parametars = all_valid_filter_parameters(parameters, self.filter_by, model_attributes_names)

            # Order parameters:
            order_list = valid_order_parameter(parameters, model_attributes_names)

            if len(order_list) > 0:

                # Return all filtered object in provided order:
                return self.model.objects.filter(**valid_parametars).order_by(*order_list)

            else:

                # Return all filtered object:
                return self.model.objects.filter(**valid_parametars)


def valid_order_parameter(parameters, model_attributes) -> list:
    """ Returns all valid order parameters in list format. """

    # All order parameters list:
    order_list = []

    # Loop thru all provided parametars:
    for parameter in parameters:
        # Find all order parameters:
        if parameter == 'order':
            # Parameter value:
            value = parameters[parameter]
            # Add provided order if valid:
            if value in model_attributes:
                # Add parameter to all parameter list:
                order_list.append(value)

    # Return all parameters list:
    return order_list

def all_valid_filter_parameters(parameters, filter_by, model_attributes) -> dict:
    """ 
        Returns all valid filter parameters in dictionary format.
            {'attribute name': 'filter value'}
    """

    def check_key_parameter(key_parameter: str) -> bool:
        """ Check if key parameter is valid. """

        # List of valid key parameters:
        valid_key_paramaters = ['contains', 'icontains']

        # Check if key parameter is valid:
        if key_parameter in valid_key_paramaters:
            # Return false if key is valid:
            return True
        else:        
            # Return false if key is invalid:
            return False

    # Return dictionary:
    valid_parametars = {}

    # Loop thru all provided parametars:
    for parameter in parameters:

        split = parameter.split('__')
        key_name = split[0]

        # If filter_by is not None, check if filter_by contain key_nave:
        if filter_by is not None:
            # Check if filter_by contain key_nave value:
            if key_name not in filter_by:
                continue

        # Check if parameter is in model attributes names list:
        if key_name in model_attributes:

            # Check key parameter if provided:
            if len(split) == 2:
                key_parameter = split[1]
                response = check_key_parameter(key_parameter)
                # Pass if response is not True:
                if response is not True:
                    # Add parameter to return dictionary but without key parameter, only key name:
                    valid_parametars[key_name] = parameters[parameter]
                    continue

            # Add parameter to return dictionary:
            valid_parametars[parameter] = parameters[parameter]
    
    # Return valid parametars dictionary:
    return valid_parametars
