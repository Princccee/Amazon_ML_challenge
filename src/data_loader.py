import pandas as pd
import os
from PIL import Image
import requests
from io import BytesIO

def load_image_from_url(url):
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img
    except Exception as e:
        print(f"Error loading image from URL {url}: {e}")
        return None

def load_test_data(dataset_folder, filename='test.csv'):
    return pd.read_csv(os.path.join(dataset_folder, filename))