# GitHub QR Code Generator

A Python project that generates a custom QR code for a GitHub profile, making it easy to share a developer portfolio or resume profile with a quick scan.

This is a simple, portfolio-friendly project built to demonstrate practical Python skills, image processing, and QR generation for real-world use cases.

## Screenshot

![GitHub QR Code Preview](github_qr_resume.png)

## Project Overview

The application takes a GitHub profile link, creates a high-quality QR code, and saves it as a PNG image. The generated QR code is designed to be clean, scannable, and suitable for resumes, personal portfolios, and professional introductions.

## Key Features

- Generates a QR code for any GitHub profile URL
- Supports custom color styling
- Uses high error correction for reliable scanning
- Saves the QR image as a PNG file
- Displays the generated QR code for instant verification
- Suitable for resumes, portfolios, and developer branding

## Tech Stack

- Python
- qrcode
- OpenCV (cv2)
- NumPy
- Pillow (PIL)

## How It Works

1. Define the GitHub profile URL
2. Generate a QR code using the qrcode library
3. Apply custom styling and colors
4. Save the output as a PNG image
5. Display the QR code for visual confirmation

## Example Use Cases

- Resume enhancement
- Portfolio profile sharing
- Personal branding
- Quick access to GitHub repositories
- Interview project demo

## Run the Project

Install the required packages:

```bash
pip install qrcode opencv-python numpy pillow
```

Run the script:

```bash
python app.py
```

The script will generate the QR code and save it as `github_qr_resume.png`.

## Interview Presentation Summary

This project highlights practical Python development skills, including:

- QR code generation
- Image processing
- Working with external libraries
- Creating a usable and visually polished output
- Building a small but valuable developer tool for profile sharing

It demonstrates how simple ideas can become professional, presentation-ready solutions that are useful in real-world networking and personal branding scenarios.
