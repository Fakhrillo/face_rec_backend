from .models import UserInfo, Photos_to_check
from rest_framework.views import APIView
from rest_framework.response import Response
from PIL import Image
import face_recognition
import numpy as np


class UserView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            user_id = int(request.data['user_id'])
            fullname = request.data['fullname']
            uploaded_file = request.FILES['photo']
            pil_image = Image.open(uploaded_file)
            test_image = np.array(pil_image)

            if not self.encodings:
                self.load_known_encodings()

            test_encoding = face_recognition.face_encodings(test_image)[0]

            # Prepare arrays for vectorized comparison
            known_encodings = np.array([self.encodings[user_id][1] for user_id in self.encodings])
            names = [self.encodings[user_id][0] for user_id in self.encodings]

            # Calculate distances between uploaded encoding and known encodings
            distances = np.linalg.norm(known_encodings - test_encoding, axis=1)

            # Find closest match
            min_distance_index = np.argmin(distances)
            min_distance = distances[min_distance_index]

            # Set threshold to determine match
            threshold = 0.6
            if min_distance < threshold:
                return Response('You are already in DB')
            else:
                UserInfo.objects.create(user_id=user_id, fullname=fullname, photo=uploaded_file)
                self.load_known_encodings()
                return Response('Successfully added')
        except Exception as e:
            return Response({'error': str(e)}, status=400)

    def load_known_encodings(self):
        try:
            for user in UserInfo.objects.all():
                known_image = face_recognition.load_image_file(user.photo.path)
                self.encodings[user.user_id] = [user.fullname]
                self.encodings[user.user_id].append(face_recognition.face_encodings(known_image)[0])
        except Exception as e:
            print(f'Failed to load known encodings: {e}')


class UserCheck(APIView):
    encodings = {}

    def post(self, request, *args, **kwargs):
        try:
            user_id = request.data.get('user_id')
            uploaded_file = request.FILES.get('photo')

            if not user_id or not uploaded_file:
                return Response({'error': 'User ID and photo are required.'}, status=400)

            user_id = int(user_id)
            pil_image = Image.open(uploaded_file)
            test_image = np.array(pil_image)

            self.load_known_encodings(user_id)

            if user_id not in self.encodings:
                return Response({'error': 'User ID not found.'}, status=404)

            test_encoding = face_recognition.face_encodings(test_image)
            if not test_encoding:
                return Response({'error': 'No face detected in the uploaded image.'}, status=400)
            test_encoding = test_encoding[0]

            known_encodings, names = self.get_known_encodings_and_names()

            distances = np.linalg.norm(known_encodings - test_encoding, axis=1)
            min_distance_index = np.argmin(distances)
            min_distance = distances[min_distance_index]

            threshold = 0.6
            if min_distance < threshold:
                name = names[min_distance_index]
                identified_user_id = [key for key, value in self.encodings.items() if value[0] == name][0]
            else:
                name = 'unknown'
                identified_user_id = -1

            Photos_to_check.objects.create(user_id=user_id, photo=uploaded_file)

            return Response({'name': name})
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    def load_known_encodings(self, user_id):
        try:
            user = UserInfo.objects.get(user_id=user_id)
            known_image = face_recognition.load_image_file(user.photo.path)
            self.encodings[user.user_id] = [user.fullname, face_recognition.face_encodings(known_image)[0]]
        except UserInfo.DoesNotExist:
            print(f'User with ID {user_id} does not exist.')
        except Exception as e:
            print(f'Failed to load known encodings: {e}')

    def get_known_encodings_and_names(self):
        known_encodings = []
        names = []
        for user_id, (name, encoding) in self.encodings.items():
            known_encodings.append(encoding)
            names.append(name)
        return np.array(known_encodings), names

    def get_known_encodings_and_names(self):
        known_encodings = []
        names = []
        for user_id, (name, encoding) in self.encodings.items():
            known_encodings.append(encoding)
            names.append(name)
        return np.array(known_encodings), names