import numpy as np

def compute(ptA, ptB):
    dist = np.linalg.norm(ptA - ptB)
    return dist

def blinked(a, b, c, d, e, f):
    up = compute(b, d) + compute(c, e)
    down = compute(a, f)
    ratio = up / (2.0 * down)
    if ratio > 0.25:
        return 2
    elif 0.21 < ratio <= 0.25:
        return 1
    else:
        return 0

def get_face_descriptor(frame, face, predictor, face_rec_model):
    shape = predictor(frame, face)
    face_descriptor = face_rec_model.compute_face_descriptor(frame, shape)
    return np.array(face_descriptor)

def is_new_face(face_descriptor, known_descriptors, threshold=0.6):
    for known_descriptor in known_descriptors:
        distance = np.linalg.norm(face_descriptor - known_descriptor)
        if distance < threshold:
            return False
    return True
