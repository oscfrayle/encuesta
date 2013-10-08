from django.http import HttpResponseRedirect, HttpResponse
#from django.template.loader import get_template
#from django.template import Context
from django.shortcuts import render,render_to_response,get_object_or_404
from django.core.urlresolvers import reverse
from polls.models import Choice, Poll
from django.http import Http404

def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]

    context = ({
        'latest_poll_list': latest_poll_list,
    })
    return render_to_response('index.html', context)


def edit(request):
    return  HttpResponse("Bien Oscar")

def consultar(request):
    return HttpResponse("Bien Oscar")

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'result.html', {'poll': poll})
    #return render_to_response('index.html', context)

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = ({
                'poll': p,
                'error_message': "You didn't select a choice.",
        })
        return render_to_response('view.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def detail(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render(request, 'detail.html', {'poll': poll})