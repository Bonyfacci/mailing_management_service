from django import forms

from app_send_mail.models import Client, Newsletter, Message


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientsCreateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ('owner',)


class MessageCreateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        exclude = ('owner',)


class NewsletterCreateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
        exclude = ('owner',)
        widgets = {
            'message': forms.Select,
            'client_id': forms.CheckboxSelectMultiple,
        }

    def clean_finish(self):
        finish = self.cleaned_data['finish']
        start = self.cleaned_data['start']
        if start > finish:
            raise forms.ValidationError('Внимание! Конец времени не может быть меньше старта')
        if start == finish:
            raise forms.ValidationError('Внимание! Конец времени должен быть отличным от старта времени')

        return finish
