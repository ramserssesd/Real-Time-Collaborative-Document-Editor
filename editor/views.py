from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Document
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse

@login_required
def document_list(request):
    documents = Document.objects.all()
    return render(request, 'editor/list.html', {'documents': documents})

@login_required
def editor_view(request, doc_id):
    doc = get_object_or_404(Document, id=doc_id)
    return render(request, 'editor/editor.html', {'doc': doc})

@csrf_exempt
@login_required
def save_document(request, doc_id):
    if request.method == 'POST':
        doc = get_object_or_404(Document, id=doc_id)
        doc.content = request.POST.get('content', '')
        doc.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'error': 'Invalid method'}, status=400)

def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/documents/')
    else:
        form = AuthenticationForm()
    return render(request, 'editor/login.html', {'form': form})



