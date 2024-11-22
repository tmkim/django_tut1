from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    # template = loader.get_template("polls/index.html")
    # return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)
    
def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
    # return HttpResponse("Question %s." % question_id)

def results(request, q_id):
    response = "Results for %s."
    return HttpResponse(response % q_id)

def vote(request, q_id):
    return HttpResponse("Voting question %s." % q_id)