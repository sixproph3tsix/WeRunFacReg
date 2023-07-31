from fns import FaceDistance
from fns import FaceScanner

# GET FACE DISTANCE
known = "C:\\Users\\prsnl\\Documents\\temp\\ingest_sample_comp\\2023 Cheha X Tri final-14271.jpg"
unknown = "C:\\Users\\prsnl\\Documents\\temp\\ingest_sample_comp\\2023 Cheha X Tri final-14190.jpg"
distance = FaceDistance(known,unknown)


# SCAN FOR FACES
input = "C:\\Users\\prsnl\\Documents\\temp\\ingest_sample_comp\\"
output = "C:\\Users\\prsnl\\Documents\\temp\\found_faces\\"
FaceScanner(input, output)

