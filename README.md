# Text_Detector

Text extraction from a 16-segment display using computer vision techniques.

## Table of Contents

1. [Introduction](#introduction)
2. [Setup](#setup)
3. [Usage](#usage)
4. [Scripts Overview](#scripts-overview)
5. [Web UI](#web-ui)
6. [Contributing](#contributing)

## Introduction

`Text_Detector` is designed to detect and extract text from videos and images, especially from a 16-segment display. The project utilizes OpenCV for image and video processing and EasyOCR for text recognition. A Flask-based UI is also provided for visualization.

## Setup

1. Make sure Python 3.x is installed.
2. Clone the repository:

```bash
git clone [repository-link]
cd Text_Detector
```

3. Install the required libraries:

```bash
pip install -r requirements.txt
```

## Usage

1. Extract frames from video:

```bash
python ComputerVision/CameraVision.py
```

2. Detect text from video:

```bash
python ComputerVision/ComputerVision.py
```

3. Detect and test text extraction from image:

```bash
python ComputerVision/ImageVision.py
```

4. Launch the Flask UI:

```bash
python ui/app.py
```

Then access the UI at `http://127.0.0.1:5000/`.

## Scripts Overview

1. **CameraVision.py**: Extracts frames from videos, specifically every 21st frame.
2. **ComputerVision.py**: Processes videos to extract text, leaning on `ImageVision.py` for detecting text inside red boxes.
3. **ImageVision.py**: Discovers red boxes in images, extracting text from these zones using EasyOCR.
4. **app.py**: The Flask UI, showcasing extracted frames and detected text.

## Web UI

The web UI is built using Flask, allowing users to visualize text detection results:

-   **index.html**: Main UI for viewing images and extracted text.
-   **style.css**: Contains styling for the UI.

For a detailed walkthrough of the UI components, view the code in the `ui` directory.

## Contributing

Before contributing, please review the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md). Adherence to these rules ensures smooth collaboration and code integration.

---
