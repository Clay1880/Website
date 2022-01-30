import email
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from home.models import Contact, PistolOrder, RiflesOrder, ShotgunOrder, SniperOrder, SubMachineOrder
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        'variable1':'Hello world'
    }
    
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is About Page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')

def buy_pistol(request):
    if request.method == "POST":
        global mode
        global gun_name
        global username
        global buyer_email
        global address
        username = request.POST.get('username')
        buyer_email = request.POST.get('buyer_email')
        mode = request.POST.get('paymentMethod')
        gun_name = request.POST.get('selectedPistol')
        address = request.POST.get('address')
        messages.success(request, 'Order Confirmed! Click on Proceed')
        
    
    return render(request, 'pistol.html')

def payment(request):
    if gun_name=="Desert Eagle":
        # global img
        img = "pic1.jpg"
        cost = "₹48,000"
        link = "https://en.wikipedia.org/wiki/Desert_Eagle"

    elif gun_name=="Hand Canon":
        # global img
        img = "pic2.png"
        cost = "₹25,000"
        link = "https://en.wikipedia.org/wiki/Hand_cannon"

    elif gun_name=="M1873":
        # global img
        img = "pic3.jfif"
        cost = "₹30,000"
        link = "https://garenafreefire.fandom.com/wiki/M1873"

    elif gun_name=="M1917":
        # global img
        img = "pic5.png"
        cost = "₹25,000"
        link = "https://en.wikipedia.org/wiki/M1917_Revolver"

    elif gun_name=="M500":
        # global img
        img = "pic4.png"
        cost = "₹32,000"
        link = "https://garenafreefire.fandom.com/wiki/M500"


    if mode=="PayPal":
        suffix = "Enter your PayPal E-Mail"

    elif mode=="UPI":
        suffix = "Enter your UPI ID"

    elif mode=="Paytm":
        suffix = "Enter your Paytm Number"

    elif mode=="Bitcoin":
        suffix = "Enter you Bitcoin Address"


    variables = {
        "mode": mode,
        "gun_name": gun_name,
        "image":img,
        "cost":cost,
        "name":username,
        "suffix":suffix,
        "link":link
    }

    if request.method=="POST":
        a = request.POST.get('mode_info')
        order = PistolOrder(user=username, email=buyer_email, address=address, gun_name=gun_name, mode=mode, mode_info=a, date=datetime.today())
        order.save()
        messages.success(request, 'Thanks for Shopping. Order will be delivered as soon as possible.')
    
    

    return render(request, 'payment.html',variables)
    
def buy_rifle(request):
    if request.method == "POST":
        global mode1
        global gun_name1
        global username1
        global buyer_email1
        global address1
        username1 = request.POST.get('username')
        buyer_email1 = request.POST.get('buyer_email')
        mode1 = request.POST.get('paymentMethod')
        gun_name1 = request.POST.get('selectedPistol')
        address1 = request.POST.get('address')
        messages.success(request, 'Order Confirmed! Click on Proceed')
    return render(request,'rifles.html')

def payment_rifle(request):
    if gun_name1=="SCAR":
        # global img
        img1 = "pic1.png"
        cost1 = "₹1,00,000"
        link1 = "https://en.wikipedia.org/wiki/FN_SCAR"

    elif gun_name1=="AK47":
        # global img
        img1 = "pic2.png"
        cost1 = "₹60,000"
        link1 = "https://en.wikipedia.org/wiki/AK-47"

    elif gun_name1=="Famas":
        # global img
        img1 = "pic3.png"
        cost1 = "₹50,000"
        link1 = "https://en.wikipedia.org/wiki/FAMAS"

    elif gun_name1=="Groza":
        # global img
        img1 = "pic4.png"
        cost1 = "₹90,000"
        link1 = "https://en.wikipedia.org/wiki/OTs-14_Groza"

    elif gun_name1=="M4A1":
        # global img
        img1 = "pic5.png"
        cost1 = "₹52,000"
        link1 = "https://en.wikipedia.org/wiki/M4_carbine"


    if mode1=="PayPal":
        suffix = "Enter your PayPal E-Mail"

    elif mode1=="UPI":
        suffix = "Enter your UPI ID"

    elif mode1=="Paytm":
        suffix = "Enter your Paytm Number"

    elif mode1=="Bitcoin":
        suffix = "Enter you Bitcoin Address"


    variables = {
        "mode": mode1,
        "gun_name": gun_name1,
        "image":img1,
        "cost":cost1,
        "name":username1,
        "suffix":suffix,
        "link":link1
    }

    if request.method=="POST":
        a = request.POST.get('mode_info')
        order = RiflesOrder(user=username1, email=buyer_email1, address=address1, gun_name=gun_name1, mode=mode1, mode_info=a,cost=cost1, date=datetime.today())
        order.save()
        messages.success(request, 'Thanks for Shopping. Order will be delivered as soon as possible.')
    return render(request,'payment_rifle.html',variables)

def buy_shotgun(request):
    if request.method == "POST":
        global mode2
        global gun_name2
        global username2
        global buyer_email2
        global address2
        username2 = request.POST.get('username')
        buyer_email2 = request.POST.get('buyer_email')
        mode2 = request.POST.get('paymentMethod')
        gun_name2 = request.POST.get('selectedPistol')
        address2 = request.POST.get('address')
        messages.success(request, 'Order Confirmed! Click on Proceed')
    return render(request, 'shotgun.html')

def payment_shotgun(request):
    if gun_name2=="M1887":
        # global img
        img2 = "pic1.png"
        cost2 = "₹6,000"
        link2 = "https://en.wikipedia.org/wiki/File:M1887_RH.JPG"

    elif gun_name2=="MAG-7":
        # global img
        img2 = "pic2.png"
        cost2 = "₹15,000"
        link2 = "https://en.wikipedia.org/wiki/MAG-7"

    elif gun_name2=="M1014":
        # global img
        img2 = "pic3.png"
        cost2 = "₹30,000"
        link2 = "https://en.wikipedia.org/wiki/Benelli_M4"

    elif gun_name2=="Kel-Tec KSG":
        # global img
        img2 = "pic4.jpg"
        cost2 = "₹90,000"
        link2 = "https://en.wikipedia.org/wiki/Kel-Tec_KSG"

    if mode2=="PayPal":
        suffix = "Enter your PayPal E-Mail"

    elif mode2=="UPI":
        suffix = "Enter your UPI ID"

    elif mode2=="Paytm":
        suffix = "Enter your Paytm Number"

    elif mode2=="Bitcoin":
        suffix = "Enter you Bitcoin Address"


    variables = {
        "mode": mode2,
        "gun_name": gun_name2,
        "image":img2,
        "cost":cost2,
        "name":username2,
        "suffix":suffix,
        "link":link2
    }

    if request.method=="POST":
        a = request.POST.get('mode_info')
        order = ShotgunOrder(user=username2, email=buyer_email2, address=address2, gun_name=gun_name2, mode=mode2, mode_info=a,cost=cost2, date=datetime.today())
        order.save()
        messages.success(request, 'Thanks for Shopping. Order will be delivered as soon as possible.')
    return render(request, 'payment_shotgun.html', variables)

def buy_snipers(request):
    if request.method == "POST":
        global mode3
        global gun_name3
        global username3
        global buyer_email3
        global address3
        username3 = request.POST.get('username')
        buyer_email3 = request.POST.get('buyer_email')
        mode3 = request.POST.get('paymentMethod')
        gun_name3 = request.POST.get('selectedPistol')
        address3 = request.POST.get('address')
        messages.success(request, 'Order Confirmed! Click on Proceed')
    return render(request, 'sniper.html')
    
def payment_sniper(request):
    if gun_name3=="AWM":
        # global img
        img3 = "pic1.png"
        cost3 = "₹6,50,000"
        link3 = "https://en.wikipedia.org/wiki/Accuracy_International_AWM"

    elif gun_name3=="KAR98K":
        # global img
        img3 = "pic2.png"
        cost3 = "₹5,00,000"
        link3 = "https://en.wikipedia.org/wiki/Karabiner_98k"

    elif gun_name3=="M82B":
        # global img
        img3 = "pic3.png"
        cost3 = "₹8,00,000"
        link3 = "https://en.wikipedia.org/wiki/Barrett_M82"

    if mode3=="PayPal":
        suffix = "Enter your PayPal E-Mail"

    elif mode3=="UPI":
        suffix = "Enter your UPI ID"

    elif mode3=="Paytm":
        suffix = "Enter your Paytm Number"

    elif mode3=="Bitcoin":
        suffix = "Enter you Bitcoin Address"


    variables = {
        "mode": mode3,
        "gun_name": gun_name3,
        "image":img3,
        "cost":cost3,
        "name":username3,
        "suffix":suffix,
        "link":link3
    }

    if request.method=="POST":
        a = request.POST.get('mode_info')
        order = SniperOrder(user=username3, email=buyer_email3, address=address3, gun_name=gun_name3, mode=mode3, mode_info=a,cost=cost3, date=datetime.today())
        order.save()
        messages.success(request, 'Thanks for Shopping. Order will be delivered as soon as possible.')
    return render(request, 'payment_sniper.html', variables)


def buy_submachinegun(request):
    if request.method == "POST":
        global mode4
        global gun_name4
        global username4
        global buyer_email4
        global address4
        username4 = request.POST.get('username')
        buyer_email4 = request.POST.get('buyer_email')
        mode4 = request.POST.get('paymentMethod')
        gun_name4 = request.POST.get('selectedPistol')
        address4 = request.POST.get('address')
        messages.success(request, 'Order Confirmed! Click on Proceed')
    return render(request, 'submachine.html')

def payment_smg(request):
    if gun_name4=="MAC10":
        # global img
        img4 = "pic1.png"
        cost4 = "₹25,000"
        link4 = "https://en.wikipedia.org/wiki/MAC-10"

    elif gun_name4=="VECTOR":
        # global img
        img4 = "pic2.png"
        cost4 = "₹1,14,000"
        link4 = "https://en.wikipedia.org/wiki/KRISS_Vector"

    elif gun_name4=="THOMPSON":
        # global img
        img4 = "pic3.png"
        cost4 = "₹40,000"
        link4 = "https://en.wikipedia.org/wiki/Thompson_submachine_gun"
    
    elif gun_name4=="VSS":
        # global img
        img4 = "pic4.png"
        cost4 = "₹1,00,000"
        link4 = "https://en.wikipedia.org/wiki/VSS_Vintorez"

    elif gun_name4=="MP5":
        # global img
        img4 = "pic5.png"
        cost4 = "₹50,000"
        link4 = "https://en.wikipedia.org/wiki/Heckler_%26_Koch_MP5"
    
    elif gun_name4=="UMP":
        # global img
        img4 = "pic6.png"
        cost4 = "₹90,000"
        link4 = "https://en.wikipedia.org/wiki/Heckler_%26_Koch_UMP"

    elif gun_name4=="MP40":
        # global img
        img4 = "pic7.png"
        cost4 = "₹40,000"
        link4 = "https://en.wikipedia.org/wiki/MP_40"

    elif gun_name4=="P90":
        # global img
        img4 = "pic8.png"
        cost4 = "₹80,000"
        link4 = "https://en.wikipedia.org/wiki/FN_P90"

    if mode4=="PayPal":
        suffix = "Enter your PayPal E-Mail"

    elif mode4=="UPI":
        suffix = "Enter your UPI ID"

    elif mode4=="Paytm":
        suffix = "Enter your Paytm Number"

    elif mode4=="Bitcoin":
        suffix = "Enter you Bitcoin Address"


    variables = {
        "mode": mode4,
        "gun_name": gun_name4,
        "image":img4,
        "cost":cost4,
        "name":username4,
        "suffix":suffix,
        "link":link4
    }

    if request.method=="POST":
        a = request.POST.get('mode_info')
        order = SubMachineOrder(user=username4, email=buyer_email4, address=address4, gun_name=gun_name4, mode=mode4, mode_info=a,cost=cost4, date=datetime.today())
        order.save()
        messages.success(request, 'Thanks for Shopping. Order will be delivered as soon as possible.')
    return render(request, 'payment_smg.html', variables)