import pandas as pd
import numpy as np

# Function to add noise to the data
def add_noise(fhr_noise_std=0.5):
    data = pd.read_csv('CTG_task\originalData\modifiedbacy_file.csv')
    noise = np.random.normal(0, fhr_noise_std, size=len(data["fhr"]))
    data["fhr"] += noise
    data["uc"] += noise
    return data

# Function to save the noisy data to a CSV file
def save_noisy_data(df, file_name="CTG_task/originalData/noisy_modifiedbacy_file.csv"):
    df.to_csv(file_name, index=False)
    print(f"Noisy data saved to {file_name}")

# Generate noisy data
noisy_data = add_noise()

# Save the noisy data to a CSV file
save_noisy_data(noisy_data)