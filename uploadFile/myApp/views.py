from django.shortcuts import render, redirect
from django.conf import settings
from .models import UploadFile
from .forms import DocumentForm


def list(request):
    # handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = UploadFile(docfile=request.FILES['docfile'])
            if request.FILES['docfile'].size > settings.MAX_UPLOAD_SIZE:
                return render(request, 'list.html', {'message': 'Maxi file size is 2.5MB.'})
            newdoc.save()
            return redirect('list')
    else:
        # empty unbound form
        form = UploadFile()
    # load documents for the list page
    documents = UploadFile.objects.all()
    return render(request, 'list.html', {'documents': documents, 'form': form})
