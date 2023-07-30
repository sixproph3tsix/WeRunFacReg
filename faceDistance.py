import face_recognition as fr
import os

# Often instead of just checking if two faces match or not (True or False), it's helpful to see how similar they are.
# You can do that by using the face_distance function.

# The model was trained in a way that faces with a distance of 0.6 or less should be a match. But if you want to
# be more strict, you can look for a smaller face distance. For example, using a 0.55 cutoff would reduce false
# positive matches at the risk of more false negatives.

# Note: This isn't exactly the same as a "percent match". The scale isn't linear. But you can assume that images with a
# smaller distance are more similar to each other than ones with a larger distance.
        
# found_faces_folder = "C:\\Users\\prsnl\\Documents\\Python\\face_recognition\\found_faces\\"
# found_faces_list = os.listdir(found_faces_folder)


unknown_face = fr.load_image_file("C:\\Users\\prsnl\\Documents\\Python\\face_recognition\\found_faces\\2023 Cheha X Tri final-14201.jpgface-0.jpg")
unknown_face_enc = fr.face_encodings(unknown_face)[0]


known_faces_folder = "C:\\Users\\prsnl\\Documents\\Python\\face_recognition\\known_faces\\"
lst_known_faces = os.listdir(known_faces_folder)

dict_face_enc = {"Filename":[],"Encoding":[]}

# Load knowns to compare against
for facefile in lst_known_faces:

    image = fr.load_image_file(known_faces_folder + facefile)

    encoded_face = fr.face_encodings(image)[0]
    
    dict_face_enc["Filename"].append(facefile)
    dict_face_enc["Encoding"].append(encoded_face)

known_face = dict_face_enc["Encoding"][0]
print(dict_face_enc["Filename"][0])

results = fr.compare_faces([encoded_face], unknown_face_enc)

# See how far apart the test image is from the known faces
# face_distances = fr.face_distance(known_encodings, image_to_test_encoding)

# for i, face_distance in enumerate(face_distances):
#     print("The test image has a distance of {:.2} from known image #{}".format(face_distance, i))
#     print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
#     print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.5))
#     print()