

# Create View class:
class BaseView:

    singular_panel = None
    plural_panel = None
    list_box_view = None

    def _collect_panel_data(self):
        """ Genetate panel data. """

        # 
        collected_panel_data = {
            'action_objects': [],
            'list_box_view': False
        }

        

        model_name = self.model._meta.object_name.lower() + '-create'

        if self.plural_panel is True:
            data = {
                'ico': 'create',
                'link': model_name
            }
            collected_panel_data['action_objects'].append(data)

        return collected_panel_data
