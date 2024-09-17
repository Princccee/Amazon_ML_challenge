import os
from src.data_loader import load_test_data
from src.data_loader import load_image_from_url
from src.ocr_extractor import extract_text_from_image
from src.regex import filter_relevant_info

def predictor(image_link, category_id, entity_name):
    print(f"Processing {entity_name} from image {image_link}")

    image = load_image_from_url(image_link)
    if image is None:
        print(f"Failed to load image from {image_link}")
        return ""

    extracted_text = extract_text_from_image(image)
    print(f"Extracted text: {extracted_text}")

    filtered_value = filter_relevant_info(entity_name, extracted_text)
    print(f"Filtered value: {filtered_value}")

    return filtered_value if filtered_value != '' else ""


if __name__ == "__main__":
    DATASET_FOLDER = '/Users/princekumar/Machine Learning/Pyhton Programming/Amazon_ML/Dataset' # Replace with the test.csv file path.
    # DATASET_FOLDER = './Dataset/test.csv'  # Replace with the test.csv file path.

    test = load_test_data(DATASET_FOLDER)

    test['prediction'] = test.apply(
        lambda row: predictor(row['image_link'], row['group_id'], row['entity_name']), axis=1)

    output_filename = os.path.join(DATASET_FOLDER, 'test_out.csv')
    test[['index', 'prediction']].to_csv(output_filename, index=False)