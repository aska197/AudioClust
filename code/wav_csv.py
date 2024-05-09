import librosa
import numpy as np
import pandas as pd
import os

# Define the directory containing WAV files (replace 'YOUR_PATH_HERE' with the actual path)
audio_dir = 'YOUR_PATH_TO_WAV_FOLDER_HERE'

# Function to normalize audio
def normalize_audio(audio, target_amplitude=0.95):
    peak_amplitude = np.max(np.abs(audio))
    gain = target_amplitude / peak_amplitude
    normalized_audio = audio * gain
    return normalized_audio

# Initialize lists to store features, filenames, and genres
features = []
filenames = []
genres = []

# Iterate over WAV files in the specified directory
for filename in os.listdir(audio_dir):
    if filename.endswith('.wav'):
        audio_path = os.path.join(audio_dir, filename)
        audio, sr = librosa.load(audio_path)
        
        # Normalize audio
        normalized_audio = normalize_audio(audio)
        
        # Extract MFCC features
        mfccs = librosa.feature.mfcc(y=normalized_audio, sr=sr)
        mfccs_mean = np.mean(mfccs, axis=1)
        
        # Append features and filename to lists
        features.append(mfccs_mean)
        filenames.append(filename)
        
        # Determine genre based on filename
        if 'rock' in filename.lower():
            genres.append('rock')
        elif 'indie' in filename.lower():
            genres.append('indie')
        else:
            genres.append('unknown')  # Handle cases where genre is not specified

# Convert features list to a numpy array
features_array = np.array(features)

# Create DataFrame with MFCC features, filenames, and genres
columns = [f'mfcc_{i}' for i in range(features_array.shape[1])]
df = pd.DataFrame(features_array, columns=columns)
df.insert(0, 'genre', genres)  # Insert 'genre' column at the beginning
df['filename'] = filenames  # Add 'filename' column

# Reorder columns with 'genre' at the beginning
df = df[['genre'] + ['filename'] + columns]

# Save DataFrame to a CSV file
output_csv_path = os.path.join(audio_dir, 'audio_dataset.csv')
df.to_csv(output_csv_path, index=False)

print(f"CSV file saved at: {output_csv_path}")


