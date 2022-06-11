from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .forms import ImageForm
from .models import Image

def add_image_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            image_obj = form.save(commit=False)
            user = request.user
            image_obj.owner_id = user.id
            image_obj.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'main/upload_image.html', {'form': form})

def success(request):
    return HttpResponse('successfully uploaded')

class ImageListView(ListView):
    model = Image
    context_object_name = 'images'