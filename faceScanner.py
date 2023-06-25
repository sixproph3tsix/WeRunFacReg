import face_recognition as fr
import os
from PIL import Image
import time

path = "C:\\Users\\prsnl\\Documents\\Python\\zer\\face_recognition\\ingest_sample_comp\\"

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
    print("Processed: "+file+" of size..."+str(file_stats_mb)+"MB in... "+elapsed+" seconds")
    print("I found {} face(s) in this photograph.".format(len(face_locations)))
    print(str(num_files_rem)+" files remaining...")

    itr = itr + 1
    i = 0
    
    # process the faces
    for face_location in face_locations:
        
        top, right, bottom, left = face_location
        
        print("A Face Located at pixel Location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top,left,bottom,right))    
    
        ver_center = bottom - (bottom - top) / 2
        hor_center = right - (right - left) / 2
        
        print("Vertical Center at: " + str(ver_center))
        print("Horizontal Center at: " + str(hor_center))
    
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.save("framed_faces/"+str(file)+"face-{}.jpg".format(i))
        i = i + 1