import os
from pydub import AudioSegment

def mp3_to_wav(mp3_file, wav_file):
    # Load MP3 file
    audio = AudioSegment.from_mp3(mp3_file)
    
    # Export as WAV file
    audio.export(wav_file, format="wav")

# Path to the directory containing MP3 files
mp3_folder = 'path_to_your_mp3_folder'

# Path to the directory where you want to save the converted WAV files
wav_folder = 'path_to_your_wav_folder'

# Create the WAV folder if it doesn't exist
os.makedirs(wav_folder, exist_ok=True)

# Iterate through MP3 files in the folder
for filename in os.listdir(mp3_folder):
    if filename.endswith('.mp3'):
        # Construct paths for MP3 and WAV files
        mp3_path = os.path.join(mp3_folder, filename)
        wav_filename = os.path.splitext(filename)[0] + '.wav'
        wav_path = os.path.join(wav_folder, wav_filename)
        
        # Convert MP3 to WAV
        mp3_to_wav(mp3_path, wav_path)

        print(f"Converted: {mp3_path} -> {wav_path}")
