import os

from django.core.files.uploadedfile import TemporaryUploadedFile
from django.test import TestCase

from pitchapp.web.forms import UploadFileForm


class TestUpload(TestCase):

    def test_upload_form_valid(self):
        """tests a valid upload"""
        upload_file = open(os.path.join(os.path.dirname(os.path.abspath(__name__)), 'test_out'),
                           'r')
        _file = TemporaryUploadedFile(
            '%s.txt' % upload_file.name, "text/plain",
            len(upload_file.read()), None)

        with open(_file.name, 'w'):
            _file.write(b'Hello world')

        import pdb; pdb.set_trace()
        form = UploadFileForm(
            files={
                'file': _file})
        self.assertTrue(form.is_valid())

    def test_upload_form_invalid(self):
        """tests an invalid upload"""
        pitch_file = TemporaryUploadedFile("Lorem Ipsum", "test_out", "application/octet-stream",
                                           0,
                                           )
        form = UploadFileForm(data={'file': pitch_file})
        self.assertFalse(form.is_valid())

    def test_upload_form_empy(self):
        """tests an empty upload (not allowed)"""
        form = UploadFileForm(data={})
        self.assertFalse(form.is_valid())
