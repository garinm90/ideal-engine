from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from orders.models import Controller


class ControllerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ControllerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'

        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Controller
        fields = ['controller_number', 'order', 'T8000', 'T4000', 'T1000', 'F16V3', 'F4V3', 'F2_Raspberry_Pi', 'Raspberry_Pi',
                'Two_Forty_24_Volt', 'Three_Twenty_24_Volt', 'TP_Link', 'Buck_Converter_24v_to_5v', 'Buck_Converter_24v_to_12v']

        
