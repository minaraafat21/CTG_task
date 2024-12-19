import pandas as pd
import numpy as np

# Function to add noise to the data
def add_noise(fhr_noise_std=1, uc_noise_std=1):
    data = pd.read_csv('CTG_task/1001.csv')
    data["fhr"] += np.random.normal(0, fhr_noise_std, size=len(data["fhr"]))
    data["uc"] += np.random.normal(0, uc_noise_std, size=len(data["uc"]))
    return data

# Function to save the noisy data to a CSV file
def save_noisy_data(df, file_name="CTG_task/noisy_data.csv"):
    df.to_csv(file_name, index=False)
    print(f"Noisy data saved to {file_name}")

# Generate noisy data
noisy_data = add_noise()

# Save the noisy data to a CSV file
save_noisy_data(noisy_data)