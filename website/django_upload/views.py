
# Create your views here.

# Create your views here.
from django.shortcuts import render
from django.template import loader
from django_upload.models import Theory_Assignment, Lab_Assignment, Theory_Lectures, Lab_Lectures, theory_a, lab_a, \
    theory_l, lab_l
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


# Create your views here.
def home(request):
    if request.method == "POST":
        row1_1 = theory_a(request.POST, request.FILES)
        row1_2 = lab_a(request.POST, request.FILESdjango)
        row2_1 = theory_l(request.POST, request.FILES)
        row2_2 = lab_l(request.POST, request.FILES)
        if row1_1.is_valid():
            row1_1.save()
            return HttpResponseRedirect(reverse('imageupload'))
    else:
        row1_1 = theory_a()
        row1_2 = lab_a()
        row2_1 = theory_l()
        row2_2 = lab_l()
    images1 = Theory_Assignment.objects.all()
    images2 = Lab_Assignment.objects.all()
    images3 = Theory_Lectures.objects.all()
    images4 = Lab_Lectures.objects.all()
    return render(request, 'profile.html',
                  {'form': row1_1, 'form': row1_2, 'form': row2_1, 'form': row2_2, 'images1': images1,
                   'images2': images2, 'images3': images3, 'images4': images4})


def about(request):
    template = loader.get_template('About_me.html')
    return HttpResponse(template.render())
