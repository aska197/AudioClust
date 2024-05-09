# Audio Genre Classification Project

## Overview
This project focuses on classifying audio tracks into different genres using Mel-frequency cepstral coefficients (MFCC) as features. The classification is performed using machine learning techniques applied to audio data extracted from WAV files.

## Data
The audio data used in this project consists of a collection of WAV files, each representing a music track. These files are stored in the `data` directory.

## Preprocessing
- **Audio Conversion:** Initially, MP3 audio files are converted into WAV format to ensure compatibility with the processing pipeline.
- **Feature Extraction:** Mel-frequency cepstral coefficients (MFCCs) are extracted from the audio signals using the librosa library in Python.
- **Normalization:** Audio signals are normalized to ensure consistency and improve model performance.

## Classification
- **Genre Labeling:** Each audio track is labeled with its corresponding genre (rock or indie) based on the information contained in the filename.
- **Feature Engineering:** MFCCs are used as features for training machine learning models.
- **Model Training:** Various machine learning models, such as k-nearest neighbors (kNN) and neural networks, are trained on the extracted features to classify audio tracks into their respective genres.

## Repository Structure
- **code:** Contains Python scripts for data preprocessing and feature extraction.
- **data:** Contains audio files in different formats (MP3 and WAV).
- **results:** Contains CSV files with extracted features and classification results.
- **schemes:** Contains Orange data mining tool workflows for audio clustering and model learning.
- **README.md:** This file provides an overview of the project, its goals, and the data preprocessing and classification steps.

## Usage

1. **Data Preprocessing**: 
    - Run `code/mp3_wav.py` to convert MP3 files to WAV format.
    - Run `code/wav_csv.py` to extract MFCC features from WAV files and save them to CSV format.

2. **Orange Data Mining**:
    - Import the CSV files into Orange for further analysis and visualization.
    - Use Orange workflows for clustering and classification tasks.

3. **Machine Learning**:
    - Use machine learning algorithms to build classification models based on extracted features.

Dependencies
------------
This project relies on the following Python libraries:
- librosa: For audio processing and feature extraction.
- numpy: For numerical operations and data manipulation.
- pandas: For data organization and analysis.
- os: For interacting with the file system and handling file paths.
- pydub: For audio file manipulation and conversion.

Contributors
------------
*   Anastasiia Krasevych (GitHub: aska197)

## License

This project is licensed under the MIT License. 

### Notes:

- The idea and concept of the project are owned by Anastasiia Krasevych, but some portions of the code were adapted from open-source projects. Please refer to the individual source files for details on their respective licenses.
- The code for converting WAV files to CSV files was inspired by [HadrienG2](https://github.com/HadrienG2/wav-csv-conversion) and is used under the MIT License.
- All rights to the audio files used in this project belong to their respective artists. This project solely aims to demonstrate data analysis and machine learning techniques and does not claim ownership of the audio content.

