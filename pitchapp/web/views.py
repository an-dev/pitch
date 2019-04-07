from django.shortcuts import render

from pitchapp.web.forms import UploadFileForm
from pitchapp.web.parser import parse_pitch_file


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
                return render(request, 'views/result.html', {'parsed_dict': parsed_dict})
            except Exception as e:
                # Just get the error message
                str_error = str(e).split(':')[0]
                return render(request, 'views/result.html', {'parse_error': str_error})
    else:
        form = UploadFileForm()

    return render(request, 'views/home.html', {'form': form})


def result(request):
    return render(request, 'views/result.html', {'parse_error': 'No data uploaded!'})
