import face_recognition as fr
import os
from PIL import Image
import time

path = "C:\\Users\\prsnl\\Documents\\Python\\face_recognition\\ingest_sample_comp\\JPEG\\"
output = "C:\\Users\\prsnl\\Documents\\Python\\face_recognition\\framed_faces\\"

dirlist = os.listdir(path)
itr = 0

for file in dirlist:
    
    # set stopwatch
    t = time.time()
    
    fullfile = path + file
    image = fr.load_image_file(fullfile)
    face_locations = fr.face_locations(image)
    elapsed = str(round(int(time.time() - t),5))
    
    # get the file size and covert to megabytes
    file_stats = os.stat(fullfile)
    file_stats_mb = round(int(file_stats.st_size)/1000000,2)

    # get the number of files being processed
    num_files = len(dirlist)
    num_files_rem = num_files - itr
    
    # report what's happening
    print("\n\nProcessed: "+file+"... of size "+str(file_stats_mb)+"MB... in "+elapsed+" seconds")
    print("{} face(s) found in this image.".format(len(face_locations)))
    print(str(num_files_rem)+" files remaining...")

    itr = itr + 1
    i = 0
    
    # process the faces
    for face_location in face_locations:
        
        top, right, bottom, left = face_location
        
        # compute the face's center coordinates
        ver_center = bottom - (bottom - top) / 2
        hor_center = right - (right - left) / 2       
        center = ver_center, hor_center
    
        print("A Face Located at pixel Location Top: {}, Left: {}, Bottom: {}, Right: {}, ... Center: {}".format(top,left,bottom,right,center))    
    
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.save("{}{}face-{}.jpg".format(output,str(file),i))
        
        i = i + 1
        
        
        
        
        
        
        
face_list = "C:\\Users\\prsnl\\Documents\\Python\\face_recognition\\framed_faces"
face_list = os.listdir(face_list)

# Often instead of just checking if two faces match or not (True or False), it's helpful to see how similar they are.
# You can do that by using the face_distance function.

# The model was trained in a way that faces with a distance of 0.6 or less should be a match. But if you want to
# be more strict, you can look for a smaller face distance. For example, using a 0.55 cutoff would reduce false
# positive matches at the risk of more false negatives.

# Note: This isn't exactly the same as a "percent match". The scale isn't linear. But you can assume that images with a
# smaller distance are more similar to each other than ones with a larger distance.

# Load some images to compare against
known_image_a = fr.load_image_file("C:\\Users\\prsnl\\Documents\\Python\\face_recognition\\knownA.jpg")
known_image_b = fr.load_image_file("C:\\Users\\prsnl\\Documents\\Python\\face_recognition\\knownB.jpg")

# Get the face encodings for the known images
face_a_encoding = fr.face_encodings(known_image_a)[0]
face_b_encoding = fr.face_encodings(known_image_b)[0]

known_encodings = [
    face_a_encoding,
    face_b_encoding
]

# Load a test image and get encondings for it
image_to_test = fr.load_image_file("C:\\Users\\prsnl\\Documents\\Python\\face_recognition\\ingest_sample_comp\\2023 Cheha X Tri final-14200")
image_to_test_encoding = fr.face_encodings(image_to_test)[0]

# See how far apart the test image is from the known faces
face_distances = fr.face_distance(known_encodings, image_to_test_encoding)

for i, face_distance in enumerate(face_distances):
    print("The test image has a distance of {:.2} from known image #{}".format(face_distance, i))
    print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
    print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.5))
    print()