from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone


from . import forms
from .models import Question, Choice


# Create your views here.

# def index(request):
#     return render(request,'basicApp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('VALIDATION SUCCESS!')
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("SOMETHING: " + form.cleaned_data['text'])

    return render(request,'basicApp/form_page.html',{'form':form})


def form_question_view(request):
    formq= forms.FormQuestion()

    if request.method == 'POST':
        formq = forms.FormQuestion(request.POST)

        if formq.is_valid():
            print('YOU ADDED NEW QUESTION SUCCESS!')
            print("QUESTION: " +formq.cleaned_data['question'])
            content = formq.cleaned_data['question']
            new_q=Question.objects.create(question_text=content, pub_date=timezone.now())

    return render(request,'basicApp/form_pageq.html',{'formq':formq})



def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'basicApp/detail.html', {'question': question})

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'basicApp/detail.html', {'question': question})

# def results(request, question_id):
#     response = "You're looking at the RESULTS of question %s."
#     return HttpResponse(response % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'basicApp/results.html', {'question': question})

# def vote(request, question_id):
#     return HttpResponse("You're VOTING on question %s." % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'basicApp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('basicApp:results', args=(question.id,)))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('basicApp/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

class IndexView(generic.ListView):
    template_name = 'basicApp/index.html'
    context_object_name = 'latest_question_list'

    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Question.objects.order_by('-pub_date')[:5]

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'basicApp/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'basicApp/results.html'

# Leave the rest of the views (detail, results, vote) unchanged

class IndexView(generic.ListView):
    template_name = 'basicApp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'basicApp/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'basicApp/results.html'
