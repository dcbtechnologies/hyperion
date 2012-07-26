# Create your views here.
from models import Graph
from django.http import HttpResponse
from django.shortcuts import render_to_response
from pyes.es import ES
from pyes.query import TermQuery

def parse(query):
    q = TermQuery()
    for term in query.split(' '):
        key, value = term.split('=')
        q.add(key, value)
    return q

def index(request):
    es = ES()
    graphs = Graph.objects.all()
    for graph in graphs:
        graph.count = es.count(parse(graph.query))['count']
    return render_to_response('dashboard/index.html', {'graphs': graphs})

def count(request):
    es = ES()
    field = request.GET['field']
    value = request.GET['value']
    return HttpResponse(str(es.count(TermQuery(field, value), 'my_index', 'my_type')['count']))

