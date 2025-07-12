from django.forms import formset_factory
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .forms import ParticipantForm

def register(request):
    ParticipantFormSet = formset_factory(ParticipantForm, extra=1)
    
    if request.method == 'POST':
        formset = ParticipantFormSet(request.POST)

        if formset.is_valid():
            saved_count = 0
            for form in formset:
                if form.cleaned_data:
                    participant = form.save()
                    saved_count += 1

            # Redirect to success page instead of showing message on same page
            return redirect('success')
    else:
        formset = ParticipantFormSet()

    return render(request, 'registry/register.html', {
        'formset': formset,
    })

def success(request):
    return render(request, 'registry/success.html')