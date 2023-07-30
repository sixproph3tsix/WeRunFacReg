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

known_faces_folder = "C:\\Users\\prsnl\\Documents\\Python\\face_recognition\\known_faces\\"
known_faces_list = os.listdir(known_faces_folder)

# initialize the empty list for known faces
loaded_knowns = []

i = 0

# Load knowns to compare against
for facefile in known_faces_list:

    print(known_faces_folder + facefile)
    loaded_knowns.append(fr.load_image_file(known_faces_folder + facefile))

    # Get the face encodings for the knowns
    face_encoding = fr.face_encodings(loaded_knowns[i])[0]
    i = i + 1

# face_b_encoding = fr.face_encodings(known_image_b)[0]

# known_encodings = [
#     face_a_encoding,
#     face_b_encoding
# ]

# # Load a test image and get encondings for it
# image_to_test = fr.load_image_file("C:\\Users\\prsnl\\Documents\\Python\\face_recognition\\ingest_sample_comp\\2023 Cheha X Tri final-14200")
# image_to_test_encoding = fr.face_encodings(image_to_test)[0]

# # See how far apart the test image is from the known faces
# face_distances = fr.face_distance(known_encodings, image_to_test_encoding)

# for i, face_distance in enumerate(face_distances):
#     print("The test image has a distance of {:.2} from known image #{}".format(face_distance, i))
#     print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
#     print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.5))
#     print()