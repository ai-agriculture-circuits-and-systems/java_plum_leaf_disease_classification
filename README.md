# Java Plum Leaf Disease Classification Dataset

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/your-repo/java-plum-leaf-disease-classification)

A comprehensive dataset of Java plum (Syzygium cumini) leaf images for disease classification, collected and organized for computer vision and deep learning research in agricultural applications.

**Project page**: `https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/y6d3z6f8z9-1.zip`

## TL;DR

- **Task**: Classification, Object Detection
- **Modality**: RGB
- **Platform**: Ground/Field
- **Real/Synthetic**: Real
- **Images**: 2,400 Java plum leaf images across 6 categories (healthy, bacterial_spot, brown_blight, sooty_mold, powdery_mildew, dry)
- **Resolution**: Variable (typically 3456×4608 pixels or larger)
- **Annotations**: CSV (per-image), COCO JSON (generated)
- **License**: CC BY 4.0
- **Citation**: see below

## Table of Contents

- [Download](#download)
- [Dataset Structure](#dataset-structure)
- [Sample Images](#sample-images)
- [Annotation Schema](#annotation-schema)
- [Stats and Splits](#stats-and-splits)
- [Quick Start](#quick-start)
- [Evaluation and Baselines](#evaluation-and-baselines)
- [Datasheet (Data Card)](#datasheet-data-card)
- [Known Issues and Caveats](#known-issues-and-caveats)
- [License](#license)
- [Citation](#citation)
- [Changelog](#changelog)
- [Contact](#contact)

## Download

**Original dataset**: `https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/y6d3z6f8z9-1.zip`

This repo hosts structure and conversion scripts only; place the downloaded folders under this directory.

**Local license file**: See `LICENSE` in the root directory.

## Dataset Structure

```
java_plum_leaf_disease_classification/
├── java_plums/                          # Main category directory
│   ├── healthy/                          # Healthy subcategory
│   │   ├── csv/                          # CSV annotation files (per-image)
│   │   ├── json/                         # JSON annotation files (per-image)
│   │   ├── images/                       # Image files
│   │   └── sets/                         # Dataset split files
│   │       ├── train.txt                 # Training set image list
│   │       ├── val.txt                   # Validation set image list
│   │       ├── test.txt                  # Test set image list
│   │       ├── all.txt                   # All images list
│   │       └── train_val.txt             # Train+val images list
│   ├── bacterial_spot/                   # Bacterial spot subcategory
│   │   └── ...                          # Same structure as healthy
│   ├── brown_blight/                     # Brown blight subcategory
│   │   └── ...                          # Same structure as healthy
│   ├── sooty_mold/                       # Sooty mold subcategory
│   │   └── ...                          # Same structure as healthy
│   ├── powdery_mildew/                   # Powdery mildew subcategory
│   │   └── ...                          # Same structure as healthy
│   ├── dry/                              # Dry subcategory
│   │   └── ...                          # Same structure as healthy
│   └── labelmap.json                     # Label mapping file
│
├── annotations/                          # COCO format JSON files (generated)
│   ├── healthy_instances_train.json
│   ├── healthy_instances_val.json
│   ├── healthy_instances_test.json
│   ├── bacterial_spot_instances_*.json
│   ├── brown_blight_instances_*.json
│   ├── sooty_mold_instances_*.json
│   ├── powdery_mildew_instances_*.json
│   ├── dry_instances_*.json
│   └── combined_instances_*.json        # Combined multi-category files
│
├── scripts/                              # Utility scripts
│   ├── reorganize_dataset.py             # Reorganize dataset to standard structure
│   ├── convert_to_coco.py                # Convert CSV to COCO format
│   └── generate_coco_annotations.py     # Original COCO annotation generator
│
├── data/                                 # Data directory
│   └── origin/                           # Original data (preserved)
│       ├── Raw Data/                     # Original high-resolution images
│       │   └── ...
│       ├── Compressed Data/              # Compressed low-resolution images
│       │   └── ...
│       └── README.md                     # Original data documentation
│
├── LICENSE                               # License file
├── README.md                             # This file
└── requirements.txt                      # Python dependencies
```

**Splits**: Splits provided via `java_plums/{subcategory}/sets/*.txt`. List image basenames (no extension). If missing, all images are used.

## Sample Images

<table>
  <tr>
    <th>Category</th>
    <th>Sample</th>
  </tr>
  <tr>
    <td><strong>Healthy</strong></td>
    <td>
      <img src="java_plums/healthy/images/Healthy (100).jpg" alt="Healthy Java plum leaf" width="260"/>
      <div align="center"><code>java_plums/healthy/images/Healthy (100).jpg</code></div>
    </td>
  </tr>
  <tr>
    <td><strong>Bacterial Spot</strong></td>
    <td>
      <img src="java_plums/bacterial_spot/images/Bacterial_Spot (100).jpg" alt="Bacterial spot on Java plum leaf" width="260"/>
      <div align="center"><code>java_plums/bacterial_spot/images/Bacterial_Spot (100).jpg</code></div>
    </td>
  </tr>
  <tr>
    <td><strong>Brown Blight</strong></td>
    <td>
      <img src="java_plums/brown_blight/images/Brown_Blight (100).jpg" alt="Brown blight on Java plum leaf" width="260"/>
      <div align="center"><code>java_plums/brown_blight/images/Brown_Blight (100).jpg</code></div>
    </td>
  </tr>
  <tr>
    <td><strong>Sooty Mold</strong></td>
    <td>
      <img src="java_plums/sooty_mold/images/Sooty_Mold (100).jpg" alt="Sooty mold on Java plum leaf" width="260"/>
      <div align="center"><code>java_plums/sooty_mold/images/Sooty_Mold (100).jpg</code></div>
    </td>
  </tr>
  <tr>
    <td><strong>Powdery Mildew</strong></td>
    <td>
      <img src="java_plums/powdery_mildew/images/Powdery_Mildew (100).jpg" alt="Powdery mildew on Java plum leaf" width="260"/>
      <div align="center"><code>java_plums/powdery_mildew/images/Powdery_Mildew (100).jpg</code></div>
    </td>
  </tr>
  <tr>
    <td><strong>Dry</strong></td>
    <td>
      <img src="java_plums/dry/images/Dry (100).jpg" alt="Dry Java plum leaf" width="260"/>
      <div align="center"><code>java_plums/dry/images/Dry (100).jpg</code></div>
    </td>
  </tr>
</table>

## Annotation Schema

### CSV Format

Each image has a corresponding CSV annotation file in `java_plums/{subcategory}/csv/{image_name}.csv`:

```csv
#item,x,y,width,height,label
0,0,0,512,512,1
```

- **Coordinates**: `x, y` - top-left corner of bounding box (pixels)
- **Dimensions**: `width, height` - bounding box dimensions (pixels)
- **Label**: Category ID (1=healthy, 2=bacterial_spot, 3=brown_blight, 4=sooty_mold, 5=powdery_mildew, 6=dry)

For classification tasks, the bounding box typically covers the entire image `[0, 0, image_width, image_height]`.

### COCO Format

COCO format JSON files are generated in the `annotations/` directory. Example structure:

```json
{
  "info": {
    "year": 2025,
    "version": "1.0",
    "description": "Java Plum Leaf Disease Classification healthy train split",
    "url": "https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/y6d3z6f8z9-1.zip"
  },
  "images": [
    {
      "id": 1234567890,
      "file_name": "java_plums/healthy/images/Healthy (100).jpg",
      "width": 3456,
      "height": 4608
    }
  ],
  "annotations": [
    {
      "id": 1,
      "image_id": 1234567890,
      "category_id": 1,
      "bbox": [0, 0, 3456, 4608],
      "area": 15925248,
      "iscrowd": 0
    }
  ],
  "categories": [
    {"id": 0, "name": "background", "supercategory": "background"},
    {"id": 1, "name": "healthy", "supercategory": "java_plum_leaf"},
    {"id": 2, "name": "bacterial_spot", "supercategory": "java_plum_leaf"},
    {"id": 3, "name": "brown_blight", "supercategory": "java_plum_leaf"},
    {"id": 4, "name": "sooty_mold", "supercategory": "java_plum_leaf"},
    {"id": 5, "name": "powdery_mildew", "supercategory": "java_plum_leaf"},
    {"id": 6, "name": "dry", "supercategory": "java_plum_leaf"}
  ]
}
```

### Label Maps

Label mapping is defined in `java_plums/labelmap.json`:

```json
[
  {"object_id": 0, "label_id": 0, "keyboard_shortcut": "0", "object_name": "background"},
  {"object_id": 1, "label_id": 1, "keyboard_shortcut": "1", "object_name": "healthy"},
  {"object_id": 2, "label_id": 2, "keyboard_shortcut": "2", "object_name": "bacterial_spot"},
  {"object_id": 3, "label_id": 3, "keyboard_shortcut": "3", "object_name": "brown_blight"},
  {"object_id": 4, "label_id": 4, "keyboard_shortcut": "4", "object_name": "sooty_mold"},
  {"object_id": 5, "label_id": 5, "keyboard_shortcut": "5", "object_name": "powdery_mildew"},
  {"object_id": 6, "label_id": 6, "keyboard_shortcut": "6", "object_name": "dry"}
]
```

## Stats and Splits

### Image Statistics

| Category | Train | Val | Test | Total |
|----------|-------|-----|------|-------|
| Healthy | 286 | 45 | 69 | 400 |
| Bacterial Spot | 273 | 68 | 59 | 400 |
| Brown Blight | 265 | 64 | 71 | 400 |
| Sooty Mold | 276 | 73 | 51 | 400 |
| Powdery Mildew | 285 | 61 | 54 | 400 |
| Dry | 295 | 49 | 56 | 400 |
| **Total** | **1,680** | **360** | **360** | **2,400** |

### Split Distribution

- **Training set**: 70% (1,680 images)
- **Validation set**: 15% (360 images)
- **Test set**: 15% (360 images)

Splits provided via `java_plums/{subcategory}/sets/*.txt`. You may define your own splits by editing those files.

## Quick Start

### Load COCO Format Annotations

```python
from pycocotools.coco import COCO
import matplotlib.pyplot as plt

# Load COCO annotation file
coco = COCO('annotations/combined_instances_train.json')

# Get all image IDs
img_ids = coco.getImgIds()
print(f"Total images: {len(img_ids)}")

# Get all category IDs
cat_ids = coco.getCatIds()
print(f"Categories: {[coco.loadCats(cat_id)[0]['name'] for cat_id in cat_ids]}")

# Load a specific image and its annotations
img_id = img_ids[0]
img_info = coco.loadImgs(img_id)[0]
ann_ids = coco.getAnnIds(imgIds=img_id)
anns = coco.loadAnns(ann_ids)

print(f"Image: {img_info['file_name']}")
print(f"Annotations: {len(anns)}")
```

### Convert CSV to COCO Format

```bash
# Convert all categories to COCO format
python scripts/convert_to_coco.py --root . --out annotations --combined

# Convert specific categories
python scripts/convert_to_coco.py --root . --out annotations \
    --categories healthy bacterial_spot --splits train val test

# Generate combined files
python scripts/convert_to_coco.py --root . --out annotations --combined
```

### Dependencies

**Required**:
- Python 3.6+
- Pillow>=9.5

**Optional** (for COCO API):
- pycocotools>=2.0.7

Install dependencies:
```bash
pip install -r requirements.txt
```

## Evaluation and Baselines

### Evaluation Metrics

For classification tasks, common metrics include:
- **Accuracy**: Overall classification accuracy
- **Precision, Recall, F1-Score**: Per-class and macro-averaged metrics
- **Confusion Matrix**: Per-class classification performance

For object detection tasks:
- **mAP@[.50:.95]**: Mean Average Precision at IoU thresholds from 0.5 to 0.95
- **mAP@0.5**: Mean Average Precision at IoU threshold 0.5

### Baseline Results

*Baseline results will be added as they become available.*

## Datasheet (Data Card)

### Motivation

This dataset was created to support research in automated plant disease detection and classification, specifically for Java plum (Syzygium cumini) leaves. The dataset enables the development of computer vision models for early disease detection in agricultural applications.

### Composition

The dataset contains:
- **2,400 high-resolution images** of Java plum leaves
- **6 disease/health categories**: healthy, bacterial_spot, brown_blight, sooty_mold, powdery_mildew, dry
- **Per-image annotations** in CSV and COCO JSON formats
- **Full-image bounding boxes** for classification tasks

### Collection Process

- Images were collected from various sources and processed for Java plum disease research
- Images include both raw and compressed versions
- Annotations were created using custom scripts in COCO format

### Preprocessing

- Images are organized by disease category
- Standardized directory structure following the dataset organization guidelines
- CSV and COCO JSON annotations generated for each image
- Dataset splits created with 70/15/15 ratio (train/val/test)

### Distribution

The dataset is distributed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

### Maintenance

The dataset is maintained by the community. Issues and contributions are welcome.

## Known Issues and Caveats

1. **Image Resolution**: Images have variable resolutions, typically 3456×4608 pixels or larger. Models should handle variable input sizes or resize images appropriately.

2. **Annotation Format**: For classification tasks, annotations use full-image bounding boxes `[0, 0, width, height]`. The category ID in the annotation indicates the image class.

3. **File Naming**: Original image files use parentheses in names (e.g., `Healthy (100).jpg`). This is preserved in the standardized structure.

4. **Data Source**: The dataset includes both "Raw Data" and "Compressed Data" directories. The standardized structure uses images from "Raw Data" by default.

5. **Coordinate System**: Bounding box coordinates use the standard image coordinate system with origin (0,0) at the top-left corner.

## License

This dataset is licensed under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

See the `LICENSE` file in the root directory for the full license text.

**Summary**: You are free to:
- Share — copy and redistribute the material in any medium or format
- Adapt — remix, transform, and build upon the material for any purpose, even commercially

Under the following terms:
- Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Check the original dataset terms and cite appropriately.

## Citation

If you use this dataset in your research, please cite:

```bibtex
@dataset{java_plum_leaf_disease_classification_2025,
  title={Java Plum Leaf Disease Classification Dataset},
  author={Dataset Contributors},
  year={2025},
  url={https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/y6d3z6f8z9-1.zip},
  license={CC BY 4.0}
}
```

## Changelog

- **V1.0.0** (2025-01): Initial standardized structure and COCO conversion utility
  - Reorganized dataset to standard structure following dataset organization guidelines
  - Created CSV and COCO JSON annotations
  - Generated dataset splits (train/val/test)
  - Added conversion scripts and documentation

## Contact

**Maintainers**: Dataset maintainers

**Original Authors**: Dataset contributors

**Source**: `https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/y6d3z6f8z9-1.zip`

For questions, issues, or contributions, please open an issue or submit a pull request.
