from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'draw/index.html', {})

# def room(request, room_name):
#     return render(request, 'draw/room.html', {
#         'room_name_json': mark_safe(json.dumps(room_name))
#     }) 
 
def voteLarge(request):
   return render(request, "draw/voteLarge.html")
  
def voteSmall(request):
   return render(request, "draw/voteSmall.html")

def voteSmallTEST(request):
   return render(request, "draw/voteSmallTEST.html")
  
def voteWinner(request):
   return render(request, "draw/voteWinner.html")
  
def voteSmallConfirmation(request):
   return render(request, "draw/voteSmallConfirmation.html")
                 
def wst(request):
   return render(request, "draw/wst.html")
