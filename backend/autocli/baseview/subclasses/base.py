# Base class:
class Base:

    model = None

    def _collect_get_parameters(self, request) -> dict:
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

    def _collect_model_attributes(self):
        """ Collect all model attributes. """

        # Return all model attributes:
        return self.model._meta.get_fields()

    def _collect_specific_model_attribute(self, attribute_name: str):
        """ Collect specific model attribute. """

        # Collect attributes names:
        attributes = self._collect_model_attributes()
        for attribute in attributes:

            # Collect only one specific model attribute:
            if attribute == attribute_name:
                return attributes[attribute]

    def _collect_model_attributes_names(self):
        """ Collect all model attributes names. """

        # Attributes names list:
        attributes_names = []

        # Collect attributes names:
        for attribute in self._collect_model_attributes():
            attributes_names.append(attribute.name)

        # Return all model attributes names:
        return attributes_names
