from typing import List
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from .forms import QuestionForm
from .models import Kscholar,Interscholar,Berta,Favorscholar
from rest_framework.views import APIView
from .serializers import ScholarSerializer,InterestSerializer,BertSerializer,BertSerializer1,FavorSerializer
from rest_framework.response import Response
from .utils import login_decorator
from django.views import View
import json
from django.http  import JsonResponse
from rest_framework import status
import jwt
from datetime import datetime
from common.serializers import UserSerializer
from common.models import User
import re


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
        serializer = ScholarSerializer(queryset,many = True)
        print(request)
        return Response(serializer.data)

class Kscholarlistapi1(APIView):
    def get (self, request,pk):
        queryset = Kscholar.objects.filter(id = pk)
        serializer = ScholarSerializer(queryset,many = True)
        print(request)
        return Response(serializer.data)        

class BertCompareApi(APIView):
    def get (self, request):   
        access = request.COOKIES['access']
        payload = jwt.decode(access, 'django-insecure-e!mjafckg!d4-7sn424q2w188$-&ie-+qs+=petrmp)r)0@b+v', algorithms=['HS256'])
        pk = payload.get('user_id')
        user = User.objects.get(id = pk)
        queryset = Berta.objects.all()
        abs = []
        line =[]
        show = []
        a = (user.semester)
        semester_number = re.sub(r'[^0-9]', '', a)
        b= (user.lastgpa)
       
        c= float(user.fullgpa)
        
        d= (user.income)
        income_number =re.sub(r'[^0-9]', '', d)
       
        e =(user.departments)
        f= str(datetime.now())
        line.append(semester_number)
        line.append(b)
        line.append(c)
        line.append(income_number)
        line.append(e)
        line.append(f)
           
        for obj in queryset:
            lin =[]
            a =(obj.con_age)
            b =(obj.con_bef_score)
            c=(obj.con_total_score)
            d =(obj.con_income)
            e = (obj.con_major)
            g = (obj.con_end_date)
            if(a == 'None'):
                lin.append(a)
         
            else:
                numbers = re.findall(r'\d+', a)
                lin.append(numbers)
            lin.append(b)
            lin.append(c)
            if(d == 'None'):
                lin.append(d)
         
            else:
                numbers = re.findall(r'\d+', d)
                lin.append(numbers)
            lin.append(e)
            lin.append(g)

            abs.append(lin)

        result1=[]
        result2=[]
        result3 =[]
        result4 =[]
        result5=[]

        for i in range(len(abs)):
            result = 0
           
            a=b=c=d=e=0
            
            
            
            count = 0
            
            if(abs[i][0]!= 'None'):
                if(abs[i][0][0]<=line[0]<=abs[i][0][1]):
                    print("hi")
                else:
                    result +=1
                    a = 1
                   
            else:
                count+=1
            
        
            if(abs[i][1]!= 'None'):
                if(float(line[1])<float(abs[i][1])):
                    result +=1
                    b = 1
            else:
                count+=1
        
        
            if(abs[i][2] != 'None'):
                if(line[2]<(float(abs[i][2]))):
                    result +=1
                    c=1
            else:
                count+=1
        
            if(abs[i][3]!= 'None'):
                if(abs[i][3][0]<=line[3]<=abs[i][3][1]):
                    print("hi")
                else:
                    result +=1
                    d=1
            else:
                count +=1
        
            if(abs[i][4]!='None'):
                if(abs[i][4].find(line[4]) == -1):
                    result +=1
                    e=1
            else:
                count+=1
        
            print(i,result,count)
            if (result == 0):
                show.append(i+1)  
            result1.append(a)          
            result2.append(b)
            result3.append(c)
            result4.append(d)
            result5.append(e)
        data = Berta.objects.filter(id__in = show)
        
        serializer = BertSerializer1(data,many = True)
        
        
        return Response({"data":serializer.data,"result1": result1,"result2": result2, "result3":result3,"result4": result4,"result5":result5})

class Bertlistapi1(APIView):
    def get (self, request,pk):
        queryset = Berta.objects.filter(id = pk)
        serializer = BertSerializer(queryset,many = True)
        print(request)
        return Response(serializer.data)      
class Bertlistapi(APIView):
    def get (self, request):
        queryset = Berta.objects.all()
        serializer = BertSerializer(queryset,many = True)
        print(request)
        return Response(serializer.data)                     


class FavorView(APIView):
    def post(self, request):
        serializer = FavorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data , status.HTTP_201_CREATED)

    def get(self, request):
            access = request.COOKIES['access']
            payload = jwt.decode(access, 'django-insecure-e!mjafckg!d4-7sn424q2w188$-&ie-+qs+=petrmp)r)0@b+v', algorithms=['HS256'])
            pk = payload.get('user_id')
            data = Favorscholar.objects.filter(user_id = pk)
            abs = []
            for obj in data:
                a =(obj.product_option_id)
                abs.append(a)
            data = Berta.objects.filter(id__in = abs)
            serializer = BertSerializer(data,many = True)
            return Response(serializer.data)




class CartView(APIView):
    def post(self, request):
        serializer = InterestSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save() 
        return Response(serializer.data, status.HTTP_201_CREATED) 
    
    
    def get(self,request):
            access = request.COOKIES['access']
            payload = jwt.decode(access, 'django-insecure-e!mjafckg!d4-7sn424q2w188$-&ie-+qs+=petrmp)r)0@b+v', algorithms=['HS256'])
            pk = payload.get('user_id')
            
            data = Interscholar.objects.filter(user_id = pk)
            abs = []
            for obj in data:
                a =(obj.product_option_id)
                abs.append(a)
            data = Kscholar.objects.filter(id__in = abs)
            serializer = ScholarSerializer(data,many = True)
            return Response(serializer.data)



    def delete(self, request):        
        user = request.data.get('user_id')
        product = request.data.get('product_option_id')
        item = Interscholar.objects.filter(user_id = user,product_option_id = product)
        item.delete()
        return Response(status.HTTP_201_CREATED) 



class CartView1(View):
    def post (self, request):
        data = json.loads(request.body)
        print(data)
        user = request.user
        product_option_id = data["kscholar_id"]
        print(user)
        print(product_option_id)

        
        if Interscholar.objects.filter(user=user, product_option_id=product_option_id).exists():
            scholar = Interscholar.objects.filter(user=user).get(product_option_id=product_option_id)
            scholar.save()
            return JsonResponse({"message": "interested_UPDATED"}, status=201)

        Interscholar.objects.create(
            user              = user,
            product_option_id = product_option_id,
        
            )
        return JsonResponse({"message": "interested_CREATED"}, status=201)

  