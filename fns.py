import face_recognition as fr
import os
from PIL import Image
import time

def FaceDistance(known_img_path, unknown_img_path):

    # Load some images to compare against
    known_img_load = fr.load_image_file(known_img_path)
    
    # Get the face encodings for the known images
    known_img_enc = fr.face_encodings(known_img_load)[0]
    
    known_img_encs = [
        known_img_enc,
    ]
    
    # Load a test image and get encondings for it
    unknown_img_load = fr.load_image_file(unknown_img_path)
    unknown_img_enc = fr.face_encodings(unknown_img_load)[0]
    
    # See how far apart the test image is from the known faces
    face_distances = fr.face_distance(known_img_encs, unknown_img_enc)
    
    for i, face_distance in enumerate(face_distances):
        print("Unknown image has a distance of {:.2} from known image #{}".format(face_distance, i))
        print("- For Normal cutoff of 0.6 - Does unknown image match the known? {}".format(face_distance < 0.6))
        print("- For Strict cutoff of 0.5 - Does unknown image match the known? {}".format(face_distance < 0.5))
        print()
        
        return round(face_distance, 2)
    
def faceScanner(input_path, output_path):
    
    dirlist = os.listdir(input_path)
    itr = 0

    for file in dirlist:
        
        # set stopwatch
        t = time.time()
        
        fullfile = input_path + file
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
            pil_image.save("{}{}face-{}.jpg".format(output_path,str(file),i))
            
            i = i + 1