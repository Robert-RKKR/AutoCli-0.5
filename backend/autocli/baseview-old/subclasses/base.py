# Base class:
class Base:

    model = None
    page_data = {}

    def collect_get_parameters(self, request) -> dict:
        """ Collect all GET request parameters. """

        # Return dictionary:
        all_parameters = {}

        # Request dictionary:
        req = request.GET

        # Collect all parameters:
        for parameter_key in req:
            all_parameters[parameter_key] = req[parameter_key]

        # Return dictionary:
        return all_parameters

    def collect_specific_model_attribute(self, attribute_name: str) -> object:
        """ Collect specific model attribute. """

        # Collect attributes names:
        attributes = self._collect_model_attributes()
        
        for attribute in attributes:

            # Collect only one specific model attribute:
            if attribute.name == attribute_name:
                return attribute

        # Return False if provided attribute name is not exist in provided model:
        return False

    def collect_model_attributes_names(self) -> list:
        """ Collect all model attributes names. """

        # Attributes names list:
        attributes_names = []

        # Collect attributes names:
        for attribute in self._collect_model_attributes():
            attributes_names.append(attribute.name)

        # Return all model attributes names:
        return attributes_names
    
    def _collect_model_attributes(self) -> tuple:
        """ Collect all model attributes. """

        # Return all model attributes:
        return self.model._meta.get_fields()
