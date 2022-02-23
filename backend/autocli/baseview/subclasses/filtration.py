# Django Import:
from django.db.models import QuerySet

# Base Import:
from .base import Base

# Filtration class:
class Filtration(Base):

    filter_by = None
    queryset = None

    def _get_filter_template(self):
        """ Xxx. """

        self.page_data['filter'] = {
            'hostname': {
                'name': 'Hostname',
                'type': 'input',
                'input_type': 'search'
            }
        }

    def _get_filtered_object(self, request):
        """ 
            Reterns all filtered object, in provided order.
            Based on provided request URL.
        """

        # Check if filter_by list is valid:
        if not isinstance(self.filter_by, list):
            if self.filter_by != 'all':
                # Raise error in case of wrong filter_by type value:
                raise TypeError('Provided filter_by value must by list type.')

        # Collect all model attributes names:
        model_attributes_names = self._collect_model_attributes_names()
        # Check if filter_by list values are valid:
        if self.filter_by != 'all':
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
            parameters = self._collect_get_parameters(request)
            valid_parametars = self._all_valid_filter_parameters(parameters)

            # Order parameters:
            order_list = self._valid_order_parameter(parameters)

            if len(order_list) > 0:

                # Return all filtered object in provided order:
                return self.model.objects.filter(**valid_parametars).order_by(*order_list)

            else:

                # Return all filtered object:
                return self.model.objects.filter(**valid_parametars)

    def _valid_order_parameter(self, parameters) -> list:
        """ Returns all valid order parameters in list format. """

        # All order parameters list:
        order_list = []
        # Collect all model attributes names:
        model_attributes = self._collect_model_attributes_names()

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

    def _all_valid_filter_parameters(self, parameters) -> dict:
        """ 
            Returns all valid filter parameters in dictionary format.
                {'attribute name': 'filter value'}
        """

        def check_key_parameter(key_name, key_parameter: str) -> bool:
            """ Check if key parameter is valid. """

            # List of valid key parameters:
            valid_key_paramaters = [
                ('contains', 'all'),
                ('icontains', 'all'),
                ('has_key', ['JSONField'])
            ]

            # Collect model attribute:
            model_attribute = self._collect_specific_model_attribute(key_name)

            # Check if key parameter is valid:
            for valid_key_paramater in valid_key_paramaters:

                # Choose only matching parameter:
                if valid_key_paramater[0] == key_parameter:
                    # Check if model_attribute type valid:
                    if valid_key_paramater[1] != 'all':
                        attribute_typ = model_attribute.__class__.__name__
                        if attribute_typ in valid_key_paramater[1]:
                            return True
                    else:
                        return True
                        
            # Return false if key is invalid:
            return False

        # Return dictionary:
        valid_parametars = {}

        # Collect all model attributes names:
        model_attributes = self._collect_model_attributes_names()

        # Loop thru all provided parametars:
        for parameter in parameters:

            split = parameter.split('__')
            key_name = split[0]

            # Check if all value in filter_by is not used:
            if self.filter_by != 'all':
                # Check if parameter is not in filter_by list:
                if key_name not in self.filter_by:
                    continue

            # Check if parameter is in model attributes names list:
            if key_name in model_attributes:

                # Check key parameter if provided:
                if len(split) == 2:
                    key_parameter = split[1]
                    response = check_key_parameter(key_name, key_parameter)
                    # Pass if response is not True:
                    if response is not True:
                        # Add parameter to return dictionary but without key parameter, only key name:
                        valid_parametars[key_name] = parameters[parameter]
                        continue

                # Add parameter to return dictionary:
                valid_parametars[parameter] = parameters[parameter]
        
        # Return valid parametars dictionary:
        return valid_parametars
