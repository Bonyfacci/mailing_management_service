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
