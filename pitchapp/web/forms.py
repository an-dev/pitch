from django import forms

from pitchapp.web.validators import FileValidator


class UploadFileForm(forms.Form):
    file = forms.FileField(label='',
                           validators=[FileValidator(
                               max_size=5 * 1024 * 1024,
                               allowed_mimetypes=['text/plain'])],
                           widget=forms.FileInput(
                               attrs={'class': 'form-control'})
                           )
