from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from .forms import ClientForm
from .serializers import ClientSerializer
from django.db.models import Count
import plotly.express as px
from rest_framework import generics

# HTML Views
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients/client_list.html', {'clients': clients})

def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'clients/client_form.html', {'form': form, 'title': 'Добавить клиента'})

def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/client_form.html', {'form': form, 'title': 'Редактировать клиента'})

# Plotly Report View (по городам)
def client_report(request):
    data = Client.objects.values('city').annotate(count=Count('id')).order_by('city')
    cities = [entry['city'] for entry in data]
    counts = [entry['count'] for entry in data]

    fig = px.bar(
        x=cities,
        y=counts,
        labels={'x': 'Город', 'y': 'Количество клиентов'},
        title='Клиенты по городам'
    )
    chart = fig.to_html(full_html=False)
    return render(request, 'clients/client_report.html', {'chart': chart})

# API Views
class ClientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
