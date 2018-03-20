from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from UserInfo.models import *
# Create your views here.

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

    ids = aruco.detect_ArUco(cv2.imread(login_attempt.id_proof.url))
    userid = ids[0][0]
    voter = Voter.objects.get(ArUcoID=userid)


    return render(request, 'some.html', {'context': voter})

