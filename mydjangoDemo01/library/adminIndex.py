from django.shortcuts import render,redirect,HttpResponse
# djangp=2.1
from .models import *
from .utils import *


"""
Seat Information
"""

def addSeatPage(request):
    return render(request,"addseat.html")

def addSeat(request):
    #从前端表单中获取数据
    Campus=request.GET.get("campus",None)
    Classroom_1=request.GET.get("classroom_1",None)
    Classroom_2=request.GET.get("classroom_2",None)
    Classroom=str(Classroom_1)+str(Classroom_2)
    Index_1=request.GET.get("index_1",None)
    Index_2=request.GET.get("index_2",None)
    Index=str(Index_1).zfill(3)+str(Index_2).zfill(3)
   
    #在 SeatInfo 表中添加记录
    SeatInfo.objects.create(
        Campus=Campus,
        Classroom=Classroom,
        Index=Index,
       
    )
    #return redirect("/page/adminIndex.html")
    return render(request,"adminIndex.html")
