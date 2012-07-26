# Create your views here.
from models import Graph
from django.shortcuts import render_to_response
from pyes.es import ES
from pyes.query import TermQuery, BoolQuery, RangeQuery
from pyes.utils import ESRange

def parse(query):
    clauses = query.split(' ')
    tq = TermQuery()
    earliest = None
    for clause in clauses:
        key, value = clause.split('=')
        if key == 'earliest':
            earliest = value
            continue
        tq.add(key, value)
    q = BoolQuery(must=[tq])
    if earliest:
        q.add_must(RangeQuery(ESRange('created_at', from_value='now' + earliest)))
    return q

def index(request):
    es = ES()
    graphs = Graph.objects.all()
    for graph in graphs:
        graph.count = es.count(parse(graph.query))['count']
    return render_to_response('dashboard/index.html', {'graphs': graphs})
