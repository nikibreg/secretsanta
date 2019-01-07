from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from .send import send

def index(request):
    return render(request, 'index.html')

class newgroup(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'newgroup.html')

    def post(self, request, *args, **kwargs):
        data, players = request.POST, []
        for i in range(int((len(data)-2)/3)):
            i = str(i)
            players.append({"name":data["name"+i], "email":data["email"+i], "want":data["want"+i]})
        names=[]
        for player in players:
            names.append(player['name'])
        sendEmails(match(names), players)
        return redirect('index')



def sendEmails(matches, players):
    for match in matches:
        for player in players:
            if player["name"] is match[0]:
                santa = player
            if player["name"] is match[1]:
                addressee = player
        msg = "Your Secret Santa match is " + addressee["name"] + ".\nEvery participant's time is limited for fulfiling their match's Christmas wish. This is what your addressee wrote as theirs\n" + addressee["want"] + "\nGood luck, Santa!"
        print(msg)
        
        send(msg, santa["email"])

def match (gifters):
    import random   
    i = 0
    results = list()        
    while i == 0:
            giftees = list(gifters) 
            results = list()        
            while len(gifters) > 0 and len(giftees) > 0:
                    random.shuffle(gifters)        
                    random.shuffle(giftees)
                    if not gifters[-1] == giftees[-1]:
                            gen = (gifters[-1], giftees[-1])       
                            results.append(gen)                    
                            gifters.pop()
                            giftees.pop()
                    else:
                            if len(gifters) == 1 and len(giftees) == 1:
                                    break
            if len(gifters) == 0 and len(giftees) == 0:
                    status = 1               
                    for result in results:
                            gifter1, giftee1 = result       
                            for gifter2, giftee2 in results:
                                    if (giftee1, gifter1) == (gifter2, giftee2):
                                            status = 0
                                            break
                    i = status      
    return results