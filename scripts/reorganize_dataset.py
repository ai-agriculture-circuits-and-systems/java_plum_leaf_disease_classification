#!/usr/bin/env python3
"""
Reorganize Java Plum Leaf Disease Classification dataset to standard structure.
"""

import os
import json
import csv
import shutil
from pathlib import Path
from PIL import Image
import random

# Mapping from old category names to new subcategory names
CATEGORY_MAPPING = {
    "Healthy": "healthy",
    "Bacterial_Spot": "bacterial_spot",
    "Brown_Blight": "brown_blight",
    "Sooty_Mold": "sooty_mold",
    "Powdery_Mildew": "powdery_mildew",
    "Dry": "dry"
}

# Category ID mapping (for labelmap.json)
CATEGORY_IDS = {
    "background": 0,
    "healthy": 1,
    "bacterial_spot": 2,
    "brown_blight": 3,
    "sooty_mold": 4,
    "powdery_mildew": 5,
    "dry": 6
}

def get_image_size(image_path):
    """Get image dimensions."""
    try:
        with Image.open(image_path) as img:
            return img.size  # (width, height)
    except Exception as e:
        print(f"Error reading image {image_path}: {e}")
        return (512, 512)  # Default size

def json_to_csv(json_path, csv_path, category_id):
    """Convert JSON annotation to CSV format."""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Get image info
        if not data.get('images') or not data.get('annotations'):
            return False
        
        image_info = data['images'][0]
        annotation = data['annotations'][0]
        
        width = image_info.get('width', 512)
        height = image_info.get('height', 512)
        bbox = annotation.get('bbox', [0, 0, width, height])
        
        # Write CSV
        with open(csv_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['#item', 'x', 'y', 'width', 'height', 'label'])
            writer.writerow([0, bbox[0], bbox[1], bbox[2], bbox[3], category_id])
        
        return True
    except Exception as e:
        print(f"Error converting {json_path} to CSV: {e}")
        return False

def reorganize_data():
    """Reorganize dataset to standard structure."""
    base_path = Path(".")
    raw_data_path = base_path / "Raw Data"
    java_plums_path = base_path / "java_plums"
    
    if not raw_data_path.exists():
        print(f"Error: {raw_data_path} does not exist")
        return
    
    # Process each category
    for old_category, new_subcategory in CATEGORY_MAPPING.items():
        old_category_path = raw_data_path / old_category
        if not old_category_path.exists():
            print(f"Warning: {old_category_path} does not exist, skipping")
            continue
        
        new_subcategory_path = java_plums_path / new_subcategory
        images_path = new_subcategory_path / "images"
        json_path = new_subcategory_path / "json"
        csv_path = new_subcategory_path / "csv"
        
        print(f"Processing {old_category} -> {new_subcategory}...")
        
        # Get all image files
        image_files = list(old_category_path.glob("*.jpg"))
        print(f"  Found {len(image_files)} images")
        
        category_id = CATEGORY_IDS[new_subcategory]
        
        # Process each image
        for img_file in image_files:
            # Get base name without extension
            base_name = img_file.stem
            
            # Copy image
            new_img_path = images_path / img_file.name
            shutil.copy2(img_file, new_img_path)
            
            # Copy and update JSON
            old_json_path = old_category_path / f"{base_name}.json"
            if old_json_path.exists():
                new_json_path = json_path / f"{base_name}.json"
                shutil.copy2(old_json_path, new_json_path)
                
                # Convert to CSV
                new_csv_path = csv_path / f"{base_name}.csv"
                json_to_csv(old_json_path, new_csv_path, category_id)
        
        print(f"  Completed {new_subcategory}")

def create_labelmap():
    """Create labelmap.json file."""
    labelmap = []
    
    # Background
    labelmap.append({
        "object_id": 0,
        "label_id": 0,
        "keyboard_shortcut": "0",
        "object_name": "background"
    })
    
    # Categories
    for subcategory, cat_id in sorted(CATEGORY_IDS.items(), key=lambda x: x[1]):
        if subcategory == "background":
            continue
        labelmap.append({
            "object_id": cat_id,
            "label_id": cat_id,
            "keyboard_shortcut": str(cat_id),
            "object_name": subcategory
        })
    
    # Save to java_plums directory
    labelmap_path = Path("java_plums") / "labelmap.json"
    with open(labelmap_path, 'w', encoding='utf-8') as f:
        json.dump(labelmap, f, indent=2, ensure_ascii=False)
    
    print(f"Created {labelmap_path}")

def create_splits():
    """Create dataset split files."""
    java_plums_path = Path("java_plums")
    
    # Collect all images from all subcategories
    all_images = []
    for subcategory in CATEGORY_MAPPING.values():
        images_path = java_plums_path / subcategory / "images"
        if images_path.exists():
            for img_file in images_path.glob("*.jpg"):
                all_images.append((subcategory, img_file.stem))
    
    # Shuffle for random split
    random.seed(42)  # For reproducibility
    random.shuffle(all_images)
    
    # Split: 70% train, 15% val, 15% test
    total = len(all_images)
    train_end = int(total * 0.7)
    val_end = train_end + int(total * 0.15)
    
    train_images = all_images[:train_end]
    val_images = all_images[train_end:val_end]
    test_images = all_images[val_end:]
    
    # Write split files for each subcategory
    for subcategory in CATEGORY_MAPPING.values():
        sets_path = java_plums_path / subcategory / "sets"
        
        # Filter images for this subcategory
        train_sub = [name for cat, name in train_images if cat == subcategory]
        val_sub = [name for cat, name in val_images if cat == subcategory]
        test_sub = [name for cat, name in test_images if cat == subcategory]
        all_sub = [name for cat, name in all_images if cat == subcategory]
        
        # Write files
        with open(sets_path / "train.txt", 'w', encoding='utf-8') as f:
            f.write('\n'.join(train_sub) + '\n')
        
        with open(sets_path / "val.txt", 'w', encoding='utf-8') as f:
            f.write('\n'.join(val_sub) + '\n')
        
        with open(sets_path / "test.txt", 'w', encoding='utf-8') as f:
            f.write('\n'.join(test_sub) + '\n')
        
        with open(sets_path / "all.txt", 'w', encoding='utf-8') as f:
            f.write('\n'.join(all_sub) + '\n')
        
        with open(sets_path / "train_val.txt", 'w', encoding='utf-8') as f:
            f.write('\n'.join(train_sub + val_sub) + '\n')
        
        print(f"Created splits for {subcategory}: train={len(train_sub)}, val={len(val_sub)}, test={len(test_sub)}")

if __name__ == "__main__":
    print("Reorganizing dataset...")
    reorganize_data()
    print("\nCreating labelmap.json...")
    create_labelmap()
    print("\nCreating dataset splits...")
    create_splits()
    print("\nDone!")

