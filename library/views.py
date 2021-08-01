from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Library
from .forms import BookIssueForm,BookIssue
from .programs.calculation import getDifference,countLeapYears
from .programs.calculation import Date

# Create your views here.

def Index(request):

    if request.method=="POST":
        forms=BookIssueForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/')
    else:
        forms=BookIssueForm()

    return render(request,'library/index.html',{'forms':forms})

def ReturnBook(request):
    if request.method=="POST":
        forms = BookIssue(request.POST)
        if forms.is_valid():
            getValue = Library.objects.filter(book_id__exact=forms.cleaned_data['bookId'])
            print("The values",getValue)
            if  getValue:
                strs=str(getValue[0].book_issue_data)
                lst=list(strs.split('-'))
                lst[2]= lst[2][:2]
                lst2=lst[1:3]
                count = 1
                for i in lst2:
                    for j in i:
                        if j is '0':
                            lst[count]=i[1]
                        else:
                            pass
                    count+=1
                print(lst)

                strs=str(forms.cleaned_data['date'])
                flst=list(strs.split('-'))
                flst[2]= flst[2][:2]
                flst2=flst[1:3]
                count = 1
                for i in flst2:
                    for j in i:
                        if j is '0':
                            flst[count]=i[1]
                        else:
                            pass
                    count+=1

                print(flst)

                dt1 = Date(int(lst[2]),int(lst[1]),int(lst[0]))
                dt2 = Date(int(flst[2]),int(flst[1]),int(flst[0]))

                s = getDifference(dt1, dt2)
                print("The is here=>",s)

                if (int(s)>15):
                    amount=((int(s)-15)*50)
                else:
                    amount="You are just on time. you do not need to pay a single paniii"

                return render(request,'library/userRecipt.html',{'params':getValue,'amounts':amount})

            else:
                return HttpResponse("There is no data inside the database")
    else:
        forms=BookIssue()
    return render(request,'library/return.html',{'forms':forms})



def Delete(request,id):
    user=Library.objects.filter(book_id__exact=id)
    user.delete()
    return redirect('/')
