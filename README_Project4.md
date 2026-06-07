# Artificial Intelligence Project 4
## Image or Text Recognition (Basic)

## Project Goal
Implement a basic image or text recognition task using available AI libraries.

## Selected Path
This project uses **OCR (Optical Character Recognition)**.

The system reads text from an image using:
- **OpenCV** for image pre-processing
- **pytesseract** as the OCR engine
- **pandas** to save word-level confidence results

## Why OCR?
The project brief allows either:
1. OCR / Text Recognition
2. Object Detection

This implementation chooses OCR because it is simple, clear, and directly demonstrates the idea of converting visual data into machine-readable text.

## Project Pipeline

### 1. Input
The system receives a sample image.

### 2. Pre-processing
The image is processed using:
- Grayscale conversion
- Gaussian blur
- Adaptive thresholding

These steps make the text clearer for OCR.

### 3. Recognition
The preprocessed image is passed to pytesseract.

### 4. Confidence Filtering
Only text with confidence greater than or equal to **80%** is accepted.

### 5. Output
The system produces:
- Recognized text
- CSV file with confidence scores
- Preprocessed image
- Visual output image with bounding boxes

## Project Files
- `ai_project4_ocr_recognition.py`  
  Main Python script.
- `sample_input.png`  
  Sample image used for testing.
- `requirements.txt`  
  Required Python packages.
- `sample_output.txt`  
  Example output after running the project.
- `Project4_Report.md`  
  Short project report.
- `outputs/`  
  Folder where results will be saved.

## Installation

### Step 1: Install Python libraries
```bash
pip install -r requirements.txt
```

### Step 2: Install Tesseract OCR Engine

#### Windows
Install Tesseract OCR on your device, then add it to PATH.

If PATH is not configured, add this line inside the Python script before OCR:
```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

#### Google Colab
```python
!sudo apt update
!sudo apt install -y tesseract-ocr
!pip install pytesseract opencv-python pandas pillow
```

## How to Run
```bash
python ai_project4_ocr_recognition.py --image sample_input.png
```

## Optional Parameters
```bash
python ai_project4_ocr_recognition.py --image sample_input.png --min_confidence 80 --psm 6
```

## Example Recognized Text
```text
DecodeLabs AI Project 4 Image or Text Recognition OCR Pipeline using Python Confidence Threshold 80% Batch 2026
```

## Validation Checklist
- Library integration is included using OpenCV and pytesseract.
- Pre-processing includes grayscale conversion and adaptive thresholding.
- Confidence threshold is set to 80%.
- Visual confirmation is generated using bounding boxes.