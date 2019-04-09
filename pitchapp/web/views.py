from django.shortcuts import render

from pitchapp.web.forms import UploadFileForm
from pitchapp.web.parser import parse_pitch_file

RESULT_PAGE_TEMPLATE = 'views/result.html'
HOME_PAGE_TEMPLATE = 'views/home.html'


def _render_result_page(request, context):
    return render(request, RESULT_PAGE_TEMPLATE, context)


def home(request):
    """
    Main logic handler.
    GET: Renders the page with the form
    POST: Handles file upload, verifies form is valid and
        renders result template with results or errors
    """
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                parsed_dict = parse_pitch_file(request.FILES['file'])
                return _render_result_page(request, {'parsed_dict': parsed_dict})
            except Exception as e:
                # Just get the error message
                str_error = str(e).split(':')[0]
                return _render_result_page(request, {'parse_error': str_error})
    else:
        form = UploadFileForm()

    return render(request, HOME_PAGE_TEMPLATE, {'form': form})


def result(request):
    return _render_result_page(request, {'parse_error': 'No data uploaded!'})
