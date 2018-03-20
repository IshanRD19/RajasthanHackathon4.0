from django.shortcuts import render, redirect
from django.http import HttpResponse, StreamingHttpResponse
from UserInfo.models import *
# Create your views here.
import ArUco_library as aruco

import cv2
import Elections.ArUco_library as aruco
import base64
import re
from django.core.files.base import ContentFile
from UserInfo.models import *
from PIL import Image
import numpy as np
import cStringIO

def index(request):
    return render(request, 'home_2.html')


def submitAruco(request):

    if request.method == 'POST':
        image_b64 = request.POST['theImageData']

        # image_data = base64.b64decode(image_b64)
        #d = 'eawf'
        image_data = re.sub('^data:image/.+;base64,', '', image_b64).decode('base64')
        #return HttpResponse(image_data+d)
        # image_PIL = Image.open(cStringIO.StringIO(image_data))

        # image_np = np.array(image_PIL)

        # print 'Image received: {}'.format(image_np.shape)
        # return ''
        # image = request.FILES['aruco']
        login_attempt = IdDetectionAttempt()
        login_attempt.id_proof = ContentFile(image_data, 'whatup.png')
        login_attempt.save()

    # return HttpResponse(str(login_attempt.id_proof.url)[1:])
    img = cv2.imread(str(login_attempt.id_proof.url)[1:])

    # img = cv2.imread(image_PIL)

    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    ids = aruco.detect_ArUco(img)
    try:
        userid = ids[0][0]
        voter = Voter.objects.get(ArUcoID=userid)
    except:
        return redirect('/')

    return render(request, 'some.html', {'context': voter})

