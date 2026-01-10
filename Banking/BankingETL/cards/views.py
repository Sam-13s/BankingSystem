from django.shortcuts import render, redirect, get_object_or_404
from .models import Card
from .forms import CardForm
from django.contrib import messages

def card_list(request):
    cards = Card.objects.all()
    return render(request, 'cards/card_list.html', {'cards': cards})

def card_create(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Card created successfully.')
            return redirect('card_list')
    else:
        form = CardForm()
    return render(request, 'cards/card_form.html', {'form': form})

def card_update(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            messages.success(request, 'Card updated successfully.')
            return redirect('card_list')
    else:
        form = CardForm(instance=card)
    return render(request, 'cards/card_form.html', {'form': form, 'card': card})

def card_delete(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == 'POST':
        card.delete()
        messages.success(request, 'Card deleted successfully.')
        return redirect('card_list')
    return render(request, 'cards/card_delete.html', {'card': card})

def issue_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Card issued successfully.')
            return redirect('card_list')
    else:
        form = CardForm()
    return render(request, 'cards/issue_card.html', {'form': form})

def block_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    card.status = 'blocked'
    card.save()
    messages.success(request, 'Card blocked successfully.')
    return redirect('card_list')

def renew_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    # Assuming renewal extends expiry by 5 years, adjust as needed
    from datetime import timedelta
    card.expiry_date = card.expiry_date + timedelta(days=365*5)
    card.save()
    messages.success(request, 'Card renewed successfully.')
    return redirect('card_list')

