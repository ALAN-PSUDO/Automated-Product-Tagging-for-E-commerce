# Fashion Product Auto-Tagging System

An AI-powered fashion product classification system using deep learning and transfer learning with ResNet50.

## 🎯 Project Overview

This system automatically classifies fashion products by:
- **Color**: 10 color classes (Black, White, Red, Blue, Navy, Grey, Beige, Pink, Green, Brown)
- **Product Type**: 10 product categories (T-shirt, Dress, Shirt, Blouse, Sweater, Jacket, Trousers, Shorts, Skirt, Vest Top)

## 🏗️ Architecture

- **Model**: ResNet50 (Transfer Learning)
- **Framework**: TensorFlow/Keras 2.20.0
- **Parameters**: 24.8M total (1.2M trainable, 23.6M frozen)
- **Input**: 224×224 RGB images
- **Output**: Multi-label classification (Color + Product Type)

## 📊 Model Specifications

| Metric | Value |
|--------|-------|
| Total Parameters | 24,783,508 |
| Trainable Parameters | 1,190,676 (4.8%) |
| Frozen Parameters | 23,592,832 (95.2%) |
| Model Size | 96 MB |
| Input Shape | (224, 224, 3) |
| Output Classes | 10 colors + 10 products |

## 🛠️ Technologies Used

- **Deep Learning**: TensorFlow 2.20.0, Keras
- **Backend API**: Flask (Python)
- **Model**: ResNet50 (Pre-trained on ImageNet)
- **Optimization**: Adam optimizer
- **Loss Function**: Binary Cross-Entropy
- **Regularization**: Dropout (0.5, 0.3) + Batch Normalization

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/ALAN-PSUDO/Automated-Product-Tagging-for-E-commerce.git
cd Automated-Product-Tagging-for-E-commerce
```

2. **Create and activate virtual environment**
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Setup Pre-trained Model

**Option 1: Auto-download from Google Drive (Recommended)**

1. Open `fashion_model.py`
2. Replace `YOUR_FILE_ID_HERE` with your Google Drive file ID
3. Run the script - it will auto-download if model doesn't exist

**How to get Google Drive File ID:**
- Upload `best_model.h5` to Google Drive
- Right-click → Share → Change to "Anyone with the link"
- Copy the sharing link: `https://drive.google.com/file/d/FILE_ID_HERE/view`
- Extract the `FILE_ID_HERE` part and paste it in `fashion_model.py`

**Option 2: Manual download**
- Download `best_model.h5` from the provided Google Drive link
- Place it in the project root directory

### Run the Model Builder

```bash
python fashion_model.py
```

**What it does:**
- ✅ Checks if `best_model.h5` exists locally
- ✅ If not, downloads from Google Drive (if FILE_ID is configured)
- ✅ Otherwise, builds a new model from scratch
- ✅ Saves to `best_model.h5`

## 📁 Project Structure

```
Automated-Product-Tagging-for-E-commerce/
├── .gitignore              # Git ignore (includes *.h5)
├── LICENSE                 # MIT License
├── README.md               # This file
├── fashion_model.py        # ML model architecture
├── requirements.txt        # Python dependencies
└── best_model.h5          # Trained model (auto-downloaded or built)
```

## 🎨 Supported Classes

### Colors (10)
- Black, White, Red, Blue, Navy
- Grey, Beige, Pink, Green, Brown

### Products (10)
- T-shirt, Dress, Shirt, Blouse, Sweater
- Jacket, Trousers, Shorts, Skirt, Vest Top

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**ALAN-PSUDO**
- GitHub: [@ALAN-PSUDO](https://github.com/ALAN-PSUDO)

## 🙏 Acknowledgments

- ResNet50 architecture from Keras Applications
- Pre-trained weights from ImageNet
- TensorFlow and Keras teams
