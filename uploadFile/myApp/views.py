from django.shortcuts import render, redirect
# from django.template import RequestContext
# from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import UploadFile
from .forms import DocumentForm


def list(request):
    # handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = UploadFile(docfile=request.FILES['docfile'])
            newdoc.save()
            return redirect(reverse('list'))
    else:
        # empty unbound form
        form = UploadFile()
    # load documents for the list page
    documents = UploadFile.objects.all()
    return render(request, 'list.html', {'documents': documents, 'form': form})
