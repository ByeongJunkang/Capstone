from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from .forms import QuestionForm
from .models import Kscholar,Interscholar
from rest_framework.views import APIView
from .serializers import ScholarSerializer,InterestSerializer
from rest_framework.response import Response
from .utils import login_decorator
from django.views import View
import json
from django.http  import JsonResponse





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





def index(request):
    scholars = Kscholar.objects.all()
    context = {'scholars':scholars}
    """
    for obj in scholars:
        print(obj.date)
    """
    return render(request,'capstone/index.html',context)


def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}

    return render(request, 'capstone/question_detail.html', context)



class Kscholarlistapi(APIView):
    def get (self, request):
        queryset = Kscholar.objects.all()
        print(queryset)
        serializer = ScholarSerializer(queryset,many = True)
        print(serializer.data)
        return Response(serializer.data)


class CartView(View):
    def post (self, request):
        data = json.loads(request.body)
        print(data)
        user = request.user
        product_option_id = data["product_option_id"]
        print(user)
        print(product_option_id)

        
        if Interscholar.objects.filter(user=user, product_option_id=product_option_id).exists():
            scholar = Interscholar.objects.filter(user=user).get(product_option_id=product_option_id)
            
            scholar.save()
            return JsonResponse({"message": "PRODUCT_QUANTITY_UPDATED"}, status=201)

        Interscholar.objects.create(
            user              = user,
            product_option_id = product_option_id,
        
            )
        return JsonResponse({"message": "CART_CREATED"}, status=201)

  