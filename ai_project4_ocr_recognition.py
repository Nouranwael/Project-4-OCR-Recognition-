"""
Artificial Intelligence - Project 4
Image or Text Recognition (Basic)

Selected Path: OCR (Optical Character Recognition)

This script:
1. Reads an image.
2. Applies systematic image pre-processing:
   - Grayscale conversion
   - Gaussian blur
   - Adaptive thresholding
3. Uses pytesseract OCR to recognize text.
4. Filters OCR words using a confidence threshold.
5. Saves clear outputs:
   - Preprocessed image
   - Visual output with bounding boxes
   - Recognized text file
   - CSV file with word-level confidence scores

Author: Your Name
"""

from pathlib import Path
import argparse

import cv2
import pandas as pd
import pytesseract
from pytesseract import Output


def preprocess_image(image_path: str, output_dir: Path):
    """
    Convert the image into a cleaner binary format for OCR.

    Steps:
    1. Grayscale conversion:
       Converts the image from 3 RGB channels to 1 intensity channel.
    2. Gaussian blur:
       Reduces tiny noise and imperfections.
    3. Adaptive thresholding:
       Converts the image into black and white pixels while handling lighting changes.
    """
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Could not read image: {image_path}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    thresholded = cv2.adaptiveThreshold(
        blurred,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        11
    )

    preprocessed_path = output_dir / 'preprocessed_image.png'
    cv2.imwrite(str(preprocessed_path), thresholded)

    return image, thresholded, preprocessed_path


def run_ocr(original_image, processed_image, output_dir: Path, min_confidence: int = 80, psm: int = 6):
    """
    Run OCR using pytesseract and filter results by confidence.

    PSM means Page Segmentation Mode:
    - 3: Fully automatic page segmentation
    - 6: Assume a single uniform block of text
    - 7: Treat the image as a single text line
    - 11: Sparse text
    """
    config = f'--oem 3 --psm {psm}'

    data = pytesseract.image_to_data(
        processed_image,
        config=config,
        output_type=Output.DICT
    )

    visual_output = original_image.copy()
    rows = []
    accepted_words = []

    for i in range(len(data['text'])):
        text = data['text'][i].strip()

        try:
            confidence = float(data['conf'][i])
        except ValueError:
            confidence = -1

        if text and confidence >= min_confidence:
            x = data['left'][i]
            y = data['top'][i]
            w = data['width'][i]
            h = data['height'][i]

            accepted_words.append(text)

            rows.append({
                'text': text,
                'confidence': round(confidence, 2),
                'x': x,
                'y': y,
                'width': w,
                'height': h
            })

            cv2.rectangle(visual_output, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(
                visual_output,
                f'{text} ({confidence:.0f}%)',
                (x, max(y - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 0, 255),
                2
            )

    results_df = pd.DataFrame(rows)

    csv_path = output_dir / 'ocr_results.csv'
    text_path = output_dir / 'recognized_text.txt'
    visual_path = output_dir / 'ocr_visual_output.png'

    results_df.to_csv(csv_path, index=False, encoding='utf-8')

    recognized_text = ' '.join(accepted_words)
    text_path.write_text(recognized_text, encoding='utf-8')
    cv2.imwrite(str(visual_path), visual_output)

    return recognized_text, results_df, csv_path, text_path, visual_path


def main():
    parser = argparse.ArgumentParser(description='AI Project 4 - Basic OCR Recognition')
    parser.add_argument('--image', default='sample_input.png', help='Path to input image')
    parser.add_argument('--min_confidence', type=int, default=80, help='Minimum confidence threshold')
    parser.add_argument('--psm', type=int, default=6, help='Tesseract Page Segmentation Mode')
    args = parser.parse_args()

    output_dir = Path('outputs')
    output_dir.mkdir(exist_ok=True)

    print('=' * 70)
    print('Artificial Intelligence Project 4 - Image/Text Recognition')
    print('Selected path: OCR using OpenCV + pytesseract')
    print('=' * 70)

    original_image, processed_image, preprocessed_path = preprocess_image(args.image, output_dir)

    recognized_text, results_df, csv_path, text_path, visual_path = run_ocr(
        original_image=original_image,
        processed_image=processed_image,
        output_dir=output_dir,
        min_confidence=args.min_confidence,
        psm=args.psm
    )

    print('\nPre-processing completed successfully.')
    print(f'Saved preprocessed image to: {preprocessed_path}')

    print('\nRecognition Output:')
    print('-' * 70)

    if recognized_text.strip():
        print(recognized_text)
    else:
        print('No text passed the confidence threshold. Try lowering the threshold or improving image quality.')

    print('-' * 70)
    print(f'Saved recognized text to: {text_path}')
    print(f'Saved OCR table to: {csv_path}')
    print(f'Saved visual confirmation image to: {visual_path}')

    if not results_df.empty:
        average_confidence = results_df['confidence'].mean()
        print(f'\nAverage accepted confidence: {average_confidence:.2f}%')
        print(f'Accepted words count: {len(results_df)}')
    else:
        print('\nAccepted words count: 0')


if __name__ == '__main__':
    main()