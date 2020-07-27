from django.http import HttpResponse
 
def hello(request):
    return HttpResponse("Hello world ! ")


from django.shortcuts import render
 
def index(request):
    context          = {}
    context['hello'] = 'Hello World!'
    context['zz']='affdf'
    return render(request, 'index.html', {'context':context})

def login(request):
    print(request.POST)
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    res = {"user": None, "msg": None}
    if(pwd!='zzzz'):
        res['msg']="error"
    else:
        res['msg']='yes'

    import json
    return HttpResponse(json.dumps(res))

def getpicture(request):
    return render(request,'getpicture.html')

def getp(request):
    name = request.POST.get("name")
    shop = request.POST.get("shop")
    sid = request.POST.get("sid")
    startdate = request.POST.get("startdate")
    enddate = request.POST.get("enddate")
    givedate = request.POST.get("givedate")
    pic=createpicture(name,shop,sid,startdate,enddate,givedate)
    return HttpResponse(pic)

    


import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

def createpicture(name,shop,sid,startdate,enddate,givedate):
    f = open('C:\\Users\\yxp\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\django\\bin\\helloworld\\statics\\picture\\count.txt','r+')
    count=f.read()
    font = ImageFont.truetype("C:\\Windows\\Fonts\\simsun.ttc",80)    #现在是宋体

    #打开底版图片
    imageFile = "C:\\Users\\yxp\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\django\\bin\\helloworld\\statics\\picture\\index.jpg"
    im1=Image.open(imageFile)
    start=startdate.split('-')
    end=enddate.split('-')
    give=givedate.split('-')
    # 在图片上添加文字 1
    draw = ImageDraw.Draw(im1)
    draw.text((1430, 1460),name,(0,0,0),font=font)
    draw.text((1430, 1570),shop,(0,0,0),font=font)
    draw.text((1350, 1680),sid,(0,0,0),font=font)
    draw.text((430,3247),str(int(start[0])),(0,0,0),font=font)
    draw.text((675,3247),str(int(start[1])),(0,0,0),font=font)
    draw.text((815,3247),str(int(start[2])),(0,0,0),font=font)
    draw.text((1060,3247),str(int(end[0])),(0,0,0),font=font)
    draw.text((1305,3247),str(int(end[1])),(0,0,0),font=font)
    draw.text((1460,3247),str(int(end[2])),(0,0,0),font=font)
    draw.text((430,3397),str(int(give[0])),(0,0,0),font=font)
    draw.text((675,3397),str(int(give[1])),(0,0,0),font=font)
    draw.text((815,3397),str(int(give[2])),(0,0,0),font=font)
    draw = ImageDraw.Draw(im1)
    # 保存
    name='/static/picture/index{}.jpg'.format(count)
    im1.save("C:\\Users\\yxp\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\django\\bin\\helloworld\\statics\\picture\\index{}.jpg".format(count))
    f = open('C:\\Users\\yxp\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\django\\bin\\helloworld\\statics\\picture\\count.txt','w+')
    count=int(count)+1
    f.write(str(count))
    f.close()
    return name

