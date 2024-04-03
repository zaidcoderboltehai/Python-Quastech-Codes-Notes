from django.shortcuts import HttpResponse  #yeh webpage pai response bhejne ke liye kaam aata hai 

def firstView(request): #django mai jitne bhi views hote hai unmey ek parameter dena compulsory hai jiska naam hai'request'(yaha pai oops waale concept ki baat nahi hori hai)
    return HttpResponse("welcome to first url") #HttpResponse ismey hamesha string he pass hota hai