from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from .forms import QuestionForm
from .models import Kscholar
from rest_framework.views import APIView
from .serializers import ScholarSerializer
from rest_framework.response import Response





def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('capstone:detail', question_id=question.id)


def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('capstone/index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'capstone/question_form.html', context)


def scholar_list(request):
    scholars = Kscholar.objects.all()
    context = {'scholars':scholars}
    """
    for obj in scholars:
        print(obj.date)
    """
    return render(request,'capstone/index.html',context)
    
def scholar_content(request,scholars_id):
    scholars = get_object_or_404(Kscholar, pk = scholars_id)
    context = {'scholars': scholars}
    return render(request, 'capstone/content.html', context)


class Kscholarlistapi(APIView):
    def get (self, request):
        queryset = Kscholar.objects.all()
        print(queryset)
        serializer = ScholarSerializer(queryset,many = True)
        return Response(serializer.data)


def index(request):
    question_list = Question.objects.order_by('-id')
    context = {'question_list': question_list}
    return render(request, 'capstone/question_list.html', context)


def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}

    return render(request, 'capstone/question_detail.html', context)





