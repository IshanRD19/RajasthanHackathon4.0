############## Task1.1 - ArUco Detection ##############

import numpy as np
import cv2
import cv2.aruco as aruco
import sys
import math
import time

def detect_ArUco(img):

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	parameters = aruco.DetectorParameters_create()
	aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)
	corners, ids, _ = aruco.detectMarkers(gray, aruco_dict, parameters= parameters)
	return ids
	## function to detect ArUco markers in the image using ArUco library
	## argument: img is the test image
	## return: dictionary named Detected_ArUco_markers of the format {ArUco_id_no : corners}, where ArUco_id_no indicates ArUco id and corners indicates the four corner position of the aruco(numpy array)
	## 		   for instance, if there is an ArUco(0) in some orientation then, ArUco_list can be like
	## 				{0: array([[315, 163],
	#							[319, 263],
	#							[219, 267],
	#							[215,167]], dtype=float32)}

	# Detected_ArUco_markers = {}
    # ## enter your code here ##
    #
	# # print ids
	# for i in range(len(ids)):
	# 	for j in corners[i][0]:
	# 		j[0] = int(j[0])
	# 		j[1] = int(j[1])
	# 	Detected_ArUco_markers[ids[i][0]] = corners[i]


	# return Detected_ArUco_markers


def Calculate_orientation_in_degree(Detected_ArUco_markers):
	## function to calculate orientation of ArUco with respective to the scale mentioned in Problem_Statement.pdf
	## argument: Detected_ArUco_markers  is the dictionary returned by the function detect_ArUco(img)
	## return : Dictionary named ArUco_marker_angles in which keys are ArUco ids and the values are angles (angles have to be calculated as mentioned in the ProblemStatement.pdf)
	##			for instance, if there are two ArUco markers with id 1 and 2 with angles 120 and 164 respectively, the 
	##			function should return: {1: 120 , 2: 164}
	ArUco_marker_angles = {}
	## enter your code here ##
	for key, value in Detected_ArUco_markers.items():
		x_c = 0
		y_c = 0
		for j in value[0]:
			x_c += j[0]
			y_c += j[1]
		x_c = x_c/4
		y_c = y_c/4
		edge_center = [(value[0][0][0]+value[0][1][0])/2, (value[0][0][1]+value[0][1][1])/2]
		dx = edge_center[0] - x_c
		dy = y_c - edge_center[1]
		# print dy, dx
		deg = abs(int(math.degrees(math.atan(dy/dx))))

		if dx < 0 and dy > 0:
			deg += 90
		if dx < 0 and dy < 0:
			deg += 180
		if dx > 0 and dy < 0:
			deg += 270
		ArUco_marker_angles[key] = deg 


	return ArUco_marker_angles	## returning the angles of the ArUco markers in degrees as a dictionary


def mark_ArUco(img,Detected_ArUco_markers,ArUco_marker_angles):
	## function to mark ArUco in the test image as per the instructions given in problem_statement.pdf 
	## arguments: img is the test image 
	##			  Detected_ArUco_markers is the dictionary returned by function detect_ArUco(img)
	##			  ArUco_marker_angles is the return value of Calculate_orientation_in_degree(Detected_ArUco_markers)
	## return: image namely img after marking the aruco as per the instruction given in Problem_statement.pdf

    ## enter your code here ##
	font = asdswdxcv2.FONT_HERSHEY_SIMPLEX
	colors = [(125,125,125),(0,255,0),(180,105,255),(255,255,255)]
	centre = {}
	
	for key, value in Detected_ArUco_markers.items():
		count = 0
		x_c = 0
		y_c = 0
		for i in value[0]:
			cv2.circle(img, (int(i[0]), int(i[1])), 5, colors[count], -1)
			x_c += i[0]
			y_c += i[1]
			count+=1
		x_c = x_c/4
		y_c = y_c/4
		centre[key] = [x_c, y_c]

		cv2.circle(img, (int(x_c), int(y_c)), 5, (0, 0, 255), -1)
		edge_center = [(value[0][0][0]+value[0][1][0])/2, (value[0][0][1]+value[0][1][1])/2]
		cv2.line(img, (int(x_c), int(y_c)), (int(edge_center[0]), int(edge_center[1])), (255, 0, 0), 3)

	for key, value in ArUco_marker_angles.items():
		cv2.putText(img, str(value), (int(centre[key][0])-70, int(centre[key][1])), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
		cv2.putText(img, str(key), (int(centre[key][0])+30, int(centre[key][1])), font, 0.8, (0, 0, 255), 2, cv2.LINE_AA)    	

	return img


