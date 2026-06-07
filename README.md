# Project Report: AI Project 4 - Image or Text Recognition

## 1. Introduction
This project implements a basic text recognition pipeline using Optical Character Recognition (OCR). The goal is to allow the machine to read text from an image and convert it into machine-readable output.

## 2. Input-Process-Output Model
### Input
A raw image containing text.

### Process
The system applies image pre-processing and then OCR recognition.

### Output
The final output contains recognized text, confidence scores, and a visual image with detected text boxes.

## 3. Libraries Used
- OpenCV: image reading and pre-processing.
- pytesseract: OCR engine wrapper.
- pandas: storing recognition results in CSV format.

## 4. Pre-processing Steps
1. Grayscale conversion: reduces the image from RGB to one intensity channel.
2. Gaussian blur: reduces noise.
3. Adaptive thresholding: converts the image into black-and-white text regions.

## 5. Recognition Method
The system uses pytesseract to extract text and confidence values from the processed image.

## 6. Confidence Filtering
A minimum confidence threshold of 80% is used. Words below this threshold are ignored to reduce false positives.

## 7. Final Output
The system saves:
- preprocessed image
- recognized text file
- CSV table
- visual confirmation image with bounding boxes

## 8. Conclusion
The project demonstrates a simple but complete recognition workflow. It shows how raw visual input can be converted into readable text using pre-processing, OCR, confidence filtering, and visual confirmation.
