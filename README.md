<div align="center">

# GitHub ID Scanner

### A lightweight Python utility for generating a customizable, resume-ready QR code for a GitHub profile.

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Image%20Display-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![QR Code](https://img.shields.io/badge/QR%20Code-Error%20Correction%20H-111827?style=for-the-badge)](https://pypi.org/project/qrcode/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<p>
  <a href="#demo">Demo</a> •
  <a href="#features">Features</a> •
  <a href="#architecture">Architecture</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#future-enhancements">Future Enhancements</a>
</p>

</div>

---

## Overview

**GitHub ID Scanner** converts a GitHub profile URL into a high-quality, scannable QR code. The application uses Python to generate the QR image, applies a randomly selected RGB foreground color, exports the result as a PNG file, and renders it with OpenCV for immediate visual verification.

The project demonstrates a compact image-generation pipeline that can be used for resumes, portfolio pages, business cards, and technical interview demonstrations.

## Demo

The generated QR code points to the GitHub profile configured in `app.py`.

<div align="center">

![Generated GitHub QR code](github_qr_resume.png)

*Generated output: `github_qr_resume.png`*

</div>

## Features

- **Profile URL encoding** — embeds a GitHub profile or any URL into the QR payload.
- **High reliability scanning** — uses `ERROR_CORRECT_H` error correction.
- **Dynamic visual styling** — generates a random RGB foreground color for each run.
- **PNG export** — saves a resume-ready image as `github_qr_resume.png`.
- **OpenCV preview** — converts the PIL image into an OpenCV-compatible BGR array and displays it.
- **Minimal and extensible design** — keeps the generation flow in one easy-to-maintain Python module.

## Technology Stack

| Layer | Technology | Responsibility |
|---|---|---|
| Runtime | Python 3.8+ | Application execution |
| QR generation | `qrcode` | QR configuration, payload encoding, and image creation |
| Image representation | Pillow (`PIL`) | RGB image conversion and PNG export |
| Array processing | NumPy | Converts the image into an array for OpenCV |
| Preview UI | OpenCV (`cv2`) | Color conversion and on-screen preview |

## Architecture

The application follows a simple sequential processing pipeline:

```text
┌─────────────────────┐
│ GitHub profile URL  │
└──────────┬──────────┘
           │ add_data()
           ▼
┌─────────────────────┐
│ QRCode configuration│  Version 1 • ECC H • border 4
└──────────┬──────────┘
           │ make(fit=True)
           ▼
┌─────────────────────┐
│ PIL RGB image       │  Custom RGB foreground + white background
└───────┬─────────┬───┘
        │         │
        │ save()  │ np.array() → cvtColor(RGB2BGR)
        ▼         ▼
┌─────────────┐  ┌────────────────┐
│ PNG artifact │  │ OpenCV preview │
└─────────────┘  └────────────────┘
```

### Processing flow

1. Configure the GitHub profile URL.
2. Generate a random RGB foreground color.
3. Create a `QRCode` object with high error correction.
4. Add the URL and fit the QR matrix to the payload.
5. Render the QR image with `qrcode` and Pillow.
6. Save the RGB image to `github_qr_resume.png`.
7. Convert RGB to BGR and display the result with OpenCV.

## Project Structure

```text
.
├── app.py                 # QR generation, image conversion, export, and preview
├── github_qr.png          # QR image asset
├── github_qr_resume.png  # Resume-ready generated output
└── README.md              # Project documentation
```

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/sgsinghashka-del/Ashka_Github-ID_Scanner.git
cd Ashka_Github-ID_Scanner
```

### 2. Create and activate a virtual environment *(recommended)*

```bash
python -m venv .venv
```

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install qrcode opencv-python numpy pillow
```

### 4. Configure and run

Update `github_url` in `app.py`, then run:

```bash
python app.py
```

The generated file will be written to the project root as `github_qr_resume.png`. Close the OpenCV preview window to allow the script to finish.

## Configuration

The primary configuration value is defined near the top of `app.py`:

```python
github_url = "https://github.com/sgsinghashka-del"
```

The QR settings can also be adjusted for different output requirements:

- `version` — QR symbol size; `fit=True` automatically expands for larger payloads.
- `error_correction` — currently `ERROR_CORRECT_H` for maximum recovery capability.
- `box_size` — pixel size of each QR module.
- `border` — quiet-zone width around the QR code.
- `fill_color` and `back_color` — foreground and background colors.

## Engineering Notes

- The QR foreground color is randomly generated on every execution; very light colors may reduce scan reliability.
- The application currently uses a fixed URL in source code rather than command-line arguments or a configuration file.
- OpenCV preview functionality requires a graphical desktop environment; headless environments can use the generated PNG without calling `cv2.imshow()`.
- `ERROR_CORRECT_H` improves resilience to damage but may increase the QR symbol size.

## Future Enhancements

- Add command-line arguments for URL, output filename, colors, and QR size.
- Validate URLs before generating the QR code.
- Replace random colors with contrast-aware color generation.
- Add a logo or GitHub mark while preserving scan reliability.
- Add automated QR decoding tests to verify generated output.
- Provide a headless mode for CI/CD and server environments.
- Add a small web interface using Flask or Streamlit.
- Add dependency management with `requirements.txt` and automated checks with GitHub Actions.

## Interview Talking Points

- **Problem:** Make a developer profile immediately accessible from a physical resume or portfolio.
- **Solution:** Encode the profile URL into a styled QR image and export it as a reusable artifact.
- **Technical decision:** Use high QR error correction and a quiet border to improve scan reliability.
- **Data flow:** URL → QR matrix → Pillow RGB image → PNG/OpenCV preview.
- **Extension path:** Separate configuration, generation, export, and preview into testable modules, then expose a CLI or web interface.

## License

This project is available under the [MIT License](LICENSE).

---

<div align="center">

Built with Python for developer portfolio sharing.

</div>
