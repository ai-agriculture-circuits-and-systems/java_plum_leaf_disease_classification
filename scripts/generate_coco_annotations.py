import os
import json
import random
import time
from pathlib import Path

def generate_unique_id():
    """Generate a unique 10-digit ID: 7 random digits + 3 timestamp digits"""
    random_part = random.randint(1000000, 9999999)
    timestamp_part = int(time.time() * 1000) % 1000
    return random_part * 1000 + timestamp_part

def create_coco_annotation(image_path, category_name, supercategory):
    """Create COCO format annotation for a single image"""
    
    # Generate unique IDs
    image_id = generate_unique_id()
    annotation_id = generate_unique_id()
    category_id = generate_unique_id()
    
    # Get image filename
    filename = os.path.basename(image_path)
    
    # Create COCO format JSON
    coco_data = {
        "info": {
            "description": "data",
            "version": "1.0",
            "year": 2025,
            "contributor": "search engine",
            "source": "augmented",
            "license": {
                "name": "Creative Commons Attribution 4.0 International",
                "url": "https://creativecommons.org/licenses/by/4.0/"
            }
        },
        "images": [
            {
                "id": image_id,
                "width": 512,
                "height": 512,
                "file_name": filename,
                "size": 409484,
                "format": "JPEG",
                "url": "",
                "hash": "",
                "status": "success"
            }
        ],
        "annotations": [
            {
                "id": annotation_id,
                "image_id": image_id,
                "category_id": category_id,
                "segmentation": [],
                "area": 262144,
                "bbox": [0, 0, 512, 512]
            }
        ],
        "categories": [
            {
                "id": category_id,
                "name": category_name,
                "supercategory": supercategory
            }
        ]
    }
    
    return coco_data

def process_directory():
    """Process all images in the dataset and generate COCO annotations"""
    
    base_path = Path(".")
    
    # Process both Raw Data and Compressed Data
    for data_type in ["Raw Data", "Compressed Data"]:
        data_path = base_path / data_type
        
        if not data_path.exists():
            continue
            
        # Process each category directory
        for category_dir in data_path.iterdir():
            if category_dir.is_dir():
                supercategory = data_type
                category_name = category_dir.name
                
                print(f"Processing {data_type}/{category_name}...")
                
                # Process each image in the category
                for image_file in category_dir.glob("*.jpg"):
                    # Create COCO annotation
                    coco_data = create_coco_annotation(
                        str(image_file), 
                        category_name, 
                        supercategory
                    )
                    
                    # Save JSON file with same name as image
                    json_filename = image_file.stem + ".json"
                    json_path = image_file.parent / json_filename
                    
                    with open(json_path, 'w', encoding='utf-8') as f:
                        json.dump(coco_data, f, indent=2, ensure_ascii=False)
                    
                    print(f"Generated: {json_filename}")

if __name__ == "__main__":
    process_directory()
    print("COCO annotations generation completed!") 