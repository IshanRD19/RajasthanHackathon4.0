from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from UserInfo.models import *
# Create your views here.
import ArUco_library as aruco

import cv2
#import ArUco_library as aruco
import base64
import re
from django.core.files.base import ContentFile
from UserInfo.models import *

def index(request):
    return render(request, 'home.html')


def submitAruco(request):

    if request.method == 'POST':
        image = request.FILES['aruco']
        login_attempt = IdDetectionAttempt()
        login_attempt.id_proof = image
        login_attempt.save()

    # return HttpResponse(str(login_attempt.id_proof.url)[1:])
    img = cv2.imread(str(login_attempt.id_proof.url)[1:])
    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    ids = aruco.detect_ArUco(img)
    userid = ids[0][0]
    voter = Voter.objects.get(ArUcoID=userid)


    return render(request, 'some.html', {'context': voter})

