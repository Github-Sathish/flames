from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response


class GetResult(APIView):
    def post(self,request):
        data = request.data
        print(data)
        name1 = data['your_name']
        name2 = data['partner_name']
        name1.lower()
        name2.lower()
        name1 = list(name1)
        name2 = list(name2)

        flames = ['f','l','a','m','e','s']
        for i in name1:
            for j in name2:
                if i==j:
                    name1.remove(i)
                    name2.remove(j)
        name3 = name1+name2
        print(name3)
        count = len(name3)
              
        s='flames'
        while(len(flames)>1):
            print(count,len(flames))
            q = count // len(flames)
            s = s*q
            print(count,'============',s)
            letter = s[count]
            flames.remove(letter)
            s = "".join(flames)
        
        result = flames[0]
        return Response({"message" : result})