from django import forms

def dynamic_form_class(headers):
    class DynamicForm(forms.Form):
        def __init__(self, *args, **kwargs):
            super(DynamicForm, self).__init__(*args, **kwargs)
            for header in headers:
                self.fields[header] = forms.CharField(max_length=255)
    return DynamicForm


