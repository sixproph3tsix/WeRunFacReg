import face_recognition as fr

def faceDistance(known_img_path, test_img_path):

    # Load some images to compare against
    known_img_load = fr.load_image_file(known_img_path)
    
    # Get the face encodings for the known images
    known_img_enc = fr.face_encodings(known_img_load)[0]
    
    known_encs = [
        known_img_enc,
    ]
    
    # Load a test image and get encondings for it
    test_img_load = fr.load_image_file(test_img_path)
    test_img_enc = fr.face_encodings(test_img_load)[0]
    
    # See how far apart the test image is from the known faces
    face_distances = fr.face_distance(known_encs, test_img_enc)
    
    for i, face_distance in enumerate(face_distances):
        print("Test image has a distance of {:.2} from known image #{}".format(face_distance, i))
        print("- For Normal cutoff of 0.6 - Does test image match the known? {}".format(face_distance < 0.6))
        print("- For Strict cutoff of 0.5 - Does test image match the known? {}".format(face_distance < 0.5))
        print()
        
kp = "C:\\Users\\prsnl\\Documents\\Python\\face_recognition\\ingest_sample_comp\\2023 Cheha X Tri final-14271.jpg"
tp = "C:\\Users\\prsnl\\Documents\\Python\\face_recognition\\ingest_sample_comp\\2023 Cheha X Tri final-14190.jpg"
faceDist(kp,tp)