from django.shortcuts import render, HttpResponse
from home.models import Entry
# Create your views here.

def home(request):
    if request.method == "POST":
        
        contact_v = request.POST.get('contact_number')
        name_v = request.POST.get('name')
        spam_v = request.POST.get('spam-yes')
        risk_score_v = request.POST.get('myRange')

        if not(name_v):
            name_v=request.POST.get('company')
        

        print(contact_v, name_v, spam_v, risk_score_v)
        if (spam_v=='yes'):
            spam_value=1
        else:
            spam_value=0
            risk_score_v=0
        
        Entry.objects.filter(userid = 'Saurav', contact=contact_v).delete()
        
        ins = Entry(contact=contact_v, source=name_v, risk_score=risk_score_v,spam=spam_value)
        ins.save()
        


    return render(request, 'page.html')