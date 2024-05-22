import os
import pickle
import face_recognition

# Define the directories
data_dir = './data'
db_dir = './db'

# Create the database directory if it doesn't exist
if not os.path.exists(db_dir):
    os.makedirs(db_dir)

# Iterate over each image in the data directory
for image_name in os.listdir(data_dir):
    if image_name.endswith(('jpg', 'jpeg', 'png')):  # Ensure only image files are processed
        # Extract the person's name from the image filename
        person_name = os.path.splitext(image_name)[0]
        
        # Load the image file
        image_path = os.path.join(data_dir, image_name)
        image = face_recognition.load_image_file(image_path)
        
        # Find face encodings
        face_encodings = face_recognition.face_encodings(image)
        
        if face_encodings:
            # Assuming only one face per image, take the first face encoding
            encoding = face_encodings[0]
            
            # Save the face encoding to a pickle file
            file_path = os.path.join(db_dir, f'{person_name}.pickle')
            with open(file_path, 'wb') as file:
                pickle.dump(encoding, file)
            
            print(f'Successfully saved encoding for {person_name}')
        else:
            print(f'No faces found in {image_name}')

print('Processing complete.')
