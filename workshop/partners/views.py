from django.shortcuts import render, redirect, get_object_or_404
from .models import Partner
from .forms import PartnerForm
from django.utils import timezone


def partners_list(request):
    partners = Partner.objects.order_by('name')
    return render(request, 'partners/partners.html', {'partners': partners})


def partner_new(request):
    form = PartnerForm()
    if request.method == 'POST':
        form = PartnerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = timezone.now()
            post.save()
            return redirect('partners.views.partners_list')
    return render(request, 'partners/partner_edit.html', {'form': form})


def partner_edit(request, pk):
    partner = get_object_or_404(Partner, pk=pk)
    if request.method == "POST":
        form = PartnerForm(request.POST, instance=partner)
        if form.is_valid():
            partner = form.save()
            return redirect('partners.views.partners_list')
    else:
        form = PartnerForm(instance=partner)
    return render(request, 'partners/partner_edit.html', {'form': form})
