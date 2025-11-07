# Fashion Product Auto-Tagging System

An AI-powered fashion product classification system using deep learning and transfer learning with ResNet50.

## 🎯 Project Overview

This system automatically classifies fashion products by:
- **Color**: 10 color classes (Black, White, Red, Blue, Navy, Grey, Beige, Pink, Green, Brown)
- **Product Type**: 10 product categories (T-shirt, Dress, Shirt, Blouse, Sweater, Jacket, Trousers, Shorts, Skirt, Vest Top)

## 🏗️ Architecture

- **Model**: ResNet50 (Transfer Learning)
- **Framework**: TensorFlow/Keras
- **Parameters**: 25.9M total (2.4M trainable, 23.6M frozen)
- **Input**: 224×224 RGB images
- **Output**: Multi-label classification (Color + Product Type)

## 📊 Model Specifications

| Metric | Value |
|--------|-------|
| Total Parameters | 25,951,882 |
| Trainable Parameters | 2,364,170 (9.1%) |
| Frozen Parameters | 23,587,712 (90.9%) |
| Model Size | 104.2 MB |
| Input Shape | (224, 224, 3) |
| Output Classes | 10 colors + 10 products |

## 🛠️ Technologies Used

- **Deep Learning**: TensorFlow, Keras
- **Backend API**: Flask (Python)
- **Frontend**: React.js
- **Model**: ResNet50 (Pre-trained on ImageNet)
- **Optimization**: Adam optimizer
- **Loss Function**: Binary Cross-Entropy
- **Regularization**: Dropout (0.5, 0.3) + Batch Normalization

## 🚀 Quick Start

### Prerequisites
