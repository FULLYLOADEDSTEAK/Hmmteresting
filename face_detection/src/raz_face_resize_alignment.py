import sys
import cv2
import dlib
import os

if len(sys.argv) != 2:
    
    print("Error1 : More input need")
    exit()

predictor_path = '/home/kyungwook/kyungwook/Hmmteresting/face_detection/src/face_alignment.dat'
path = '/home/kyungwook/kyungwook/aligned_img'
face_file_path = sys.argv[1]
filename = os.path.basename(face_file_path)

# Load all the models we need: a detector to find the faces, a shape predictor
# to find face landmarks so we can precisely localize the face
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(predictor_path)

# Load the image using Dlib
img = dlib.load_rgb_image(face_file_path)

# Ask the detector to find the bounding boxes of each face. The 1 in the
# second argument indicates that we should upsample the image 1 time. This
# will make everything bigger and allow us to detect more faces.
# dets = detector(resize_img, 1)
dets = detector(img, 1)

num_faces = len(dets)
if num_faces == 0:
    print("Error2 : No Face Found")
    #print("Sorry, there were no faces found in '{}'".format(face_file_path))
    exit()

elif num_faces != 1 and num_faces != 0:
    print("Error3 : Too Many Faces")
    #print("Sorry, there were no faces found in '{}'".format(face_file_path))
    exit()

# Find the 5 face landmarks we need to do the alignment.
faces = dlib.full_object_detections()
for detection in dets:
    
    # faces.append(sp(resize_img, detection))
    faces.append(sp(img, detection))    

window = dlib.image_window()

# Get the aligned face images
# Optionally: 
# images = dlib.get_face_chips(resize_img, faces, size=112, padding=0.12)
images = dlib.get_face_chips(img, faces, size=112, padding=0.12)
for image in images: 

    bgr_img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(os.path.join(path , filename), bgr_img)
    print (path + "/" + filename)
