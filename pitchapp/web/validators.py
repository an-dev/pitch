import magic

from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _


@deconstructible
class FileValidator(object):
    """
    Validator for files, checking the size, extension and mimetype.
    Initialization parameters:
        allowed_mimetypes: iterable with allowed mimetypes
        max_size: maximum number of bytes allowed
    Usage example::
        MyModel(models.Model):
            myfile = FileField(validators=[FileValidator(max_size=24*1024*1024), ...)]
    """

    mime_message = _(
        "Allowed mime types are: %(allowed_mimetypes)s.")
    max_size_message = _(
        'The maximum file size is %(allowed_size)s.')

    def __init__(self, *args, **kwargs):
        self.allowed_mimetypes = kwargs.pop('allowed_mimetypes', None)
        self.max_size = kwargs.pop('max_size', None)

    def __call__(self, value):
        """
        Check content type and file size.
        """
        # Check the content type
        handler = magic.Magic(mime=True, uncompress=True)
        mimetype = handler.from_file(value.file.name)
        if self.allowed_mimetypes and mimetype not in self.allowed_mimetypes:
            message = self.mime_message % {
                'mimetype': mimetype,
                'allowed_mimetypes': ', '.join(self.allowed_mimetypes)
            }

            raise ValidationError(message)

        # Check the file size
        filesize = len(value)
        if self.max_size and filesize > self.max_size:
            message = self.max_size_message % {
                'size': filesizeformat(filesize),
                'allowed_size': filesizeformat(self.max_size)
            }

            raise ValidationError(message)
