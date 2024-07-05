from django import forms

def dynamic_form_class(headers):
    class DynamicForm(forms.Form):
        pass

    for header in headers:
        field_name = header.lower().replace(' ', '_')
        print(field_name)
        setattr(DynamicForm, field_name, forms.CharField(label=header))

    return DynamicForm


