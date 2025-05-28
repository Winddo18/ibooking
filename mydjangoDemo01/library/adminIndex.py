from django.shortcuts import render,redirect,HttpResponse
# djangp=2.1
from .models import *
from .utils import *

def startend2mask(start,end):
    mask=""
    for i in range(24):
        if i >=start and i <end:
            mask=mask+"1"
        else:
            mask=mask+"0"
    #print("=> 开放时间为：",mask," .. mask的长度为:",len(mask))
    return mask
def mask2startend(mask):
    start=0
    end=0
    start=mask.find("1")
    end=mask.rfind("1")
    if start==-1 or end==-1:
        start=0
        end=0
    return start,end

def addSeat(request):
    #从前端表单中获取数据
    Campus=request.GET.get("campus",None)
    Classroom_1=request.GET.get("classroom_1",None)
    Classroom_2=request.GET.get("classroom_2",None)
    Classroom=str(Classroom_1)+str(Classroom_2)
    Index_1=request.GET.get("index_1",None)
    Index_2=request.GET.get("index_2",None)
    Index=str(Index_1).zfill(3)+str(Index_2).zfill(3)
    Electricity=(request.GET.get("electricity",None)=="Powered") #Powered->1  Unpowered->0
    Start=request.GET.get("start",None)
    End=request.GET.get("end",None)
    Maxtime=request.GET.get("maxtime",None)
    State=request.GET.get("state",None)
    if State=="不可用":
        State=-1
    elif State=="空闲":
        State=0
    elif State=="被占用":
        State=1
    else:
        State=None
    #在 SeatInfo 表中添加记录
    SeatInfo.objects.create(
        Campus=Campus,
        Classroom=Classroom,
        Index=Index,
        Electricity=Electricity,
        Mask=startend2mask(int(Start),int(End)),
        MaxTime=Maxtime,
    )
    #return redirect("/page/adminIndex.html")
    return render(request,"adminIndex.html")