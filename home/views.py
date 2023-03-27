from django.shortcuts import render, HttpResponse
from home.models import Entry
# Create your views here.

def home(request):
    if request.method == "POST":
        
        contact_v = request.POST.get('contact_number')
        name_v = request.POST.get('name')
        spam_v = request.POST.get('spam-yes')
        risk_score_v = request.POST.get('myRange')
        mail_body = request.POST.get('mail-body')
        mail_sub = request.POST.get('subject')
        sms_v = request.POST.get('sms')

    
        if not(name_v):
            name_v=request.POST.get('company')
        

        print(contact_v, name_v, spam_v, risk_score_v)
        if (spam_v=='yes'):
            spam_value=1
        else:
            spam_value=0
            risk_score_v=0
        
        Entry.objects.filter(userid = 'Saurav', contact=contact_v).delete()

        print(contact_v, name_v, spam_v, risk_score_v, mail_body, mail_sub, sms_v)
        
        ins = Entry(contact=contact_v, source=name_v, risk_score=risk_score_v,spam=spam_value,subject=mail_sub, body=mail_body, sms=sms_v)
        ins.save()
        


    return render(request, 'page.html')

def page2(request):
    if request.method == 'POST':

        input_contact = request.POST.get('contact_number')
        print('Testing')
        print(input_contact)
        obj=Entry.objects.filter(contact=input_contact)
        risknum=0
        count=0
        for i in obj:
            risknum=(i.weight*i.risk_score)+risknum
            count=count+i.weight
        riskscore=risknum/count
        print(riskscore)
        context={'riskscore':riskscore}
        return render(request, 'page2.html', context)
        
    return render(request, 'page2.html')