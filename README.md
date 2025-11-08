# Fashion Product Auto-Tagging System# Fashion Product Auto-Tagging System



An AI-powered fashion product classification system using deep learning and transfer learning with ResNet50.An AI-powered fashion product classification system using deep learning and transfer learning with ResNet50.



## 🎯 Project Overview## 🎯 Project Overview



This system automatically classifies fashion products by:This system automatically classifies fashion products by:

- **Color**: 10 color classes (Black, White, Red, Blue, Navy, Grey, Beige, Pink, Green, Brown)- **Color**: 10 color classes (Black, White, Red, Blue, Navy, Grey, Beige, Pink, Green, Brown)

- **Product Type**: 10 product categories (T-shirt, Dress, Shirt, Blouse, Sweater, Jacket, Trousers, Shorts, Skirt, Vest Top)- **Product Type**: 10 product categories (T-shirt, Dress, Shirt, Blouse, Sweater, Jacket, Trousers, Shorts, Skirt, Vest Top)



## 🏗️ Architecture## 🏗️ Architecture



- **Model**: ResNet50 (Transfer Learning)- **Model**: ResNet50 (Transfer Learning)

- **Framework**: TensorFlow/Keras 2.20.0- **Framework**: TensorFlow/Keras

- **Parameters**: 24.8M total (1.2M trainable, 23.6M frozen)- **Parameters**: 25.9M total (2.4M trainable, 23.6M frozen)

- **Input**: 224×224 RGB images- **Input**: 224×224 RGB images

- **Output**: Multi-label classification (Color + Product Type)- **Output**: Multi-label classification (Color + Product Type)



## 📊 Model Specifications## 📊 Model Specifications



| Metric | Value || Metric | Value |

|--------|-------||--------|-------|

| Total Parameters | 24,783,508 || Total Parameters | 25,951,882 |

| Trainable Parameters | 1,190,676 (4.8%) || Trainable Parameters | 2,364,170 (9.1%) |

| Frozen Parameters | 23,592,832 (95.2%) || Frozen Parameters | 23,587,712 (90.9%) |

| Model Size | 96 MB || Model Size | 104.2 MB |

| Input Shape | (224, 224, 3) || Input Shape | (224, 224, 3) |

| Output Classes | 10 colors + 10 products || Output Classes | 10 colors + 10 products |



## 🛠️ Technologies Used## 🛠️ Technologies Used



- **Deep Learning**: TensorFlow 2.20.0, Keras- **Deep Learning**: TensorFlow, Keras

- **Backend API**: Flask (Python)- **Backend API**: Flask (Python)

- **Model**: ResNet50 (Pre-trained on ImageNet)- **Frontend**: React.js

- **Optimization**: Adam optimizer- **Model**: ResNet50 (Pre-trained on ImageNet)

- **Loss Function**: Binary Cross-Entropy- **Optimization**: Adam optimizer

- **Regularization**: Dropout (0.5, 0.3) + Batch Normalization- **Loss Function**: Binary Cross-Entropy

- **Regularization**: Dropout (0.5, 0.3) + Batch Normalization

## 🚀 Quick Start

## 🚀 Quick Start

### Prerequisites

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

### Build the Model

Run the model builder to create the initial model architecture:

```bash
python fashion_model.py
```

This creates `best_model.h5` with the ResNet50 architecture and pre-trained ImageNet weights.

## 📚 Usage

### 1. Training the Model

Prepare your dataset:
- Create `data/fashion_dataset.csv` with columns: `image_filename`, `color`, `product_type`
- Place images in `data/images/`

Train the model:
```bash
python src/train.py
```

### 2. Making Predictions

Predict a single image:
```bash
python src/predict.py path/to/image.jpg
```

With custom model:
```bash
python src/predict.py path/to/image.jpg path/to/model.h5
```

### 3. Running the API Server

Start the Flask API:
```bash
python src/app.py
```

The API will be available at `http://localhost:5000`

#### API Endpoints

**Health Check**
```bash
curl http://localhost:5000/health
```

**Get Available Classes**
```bash
curl http://localhost:5000/classes
```

**Predict with File Upload**
```bash
curl -X POST -F "image=@test_image.jpg" http://localhost:5000/predict
```

**Predict with Base64**
```bash
curl -X POST http://localhost:5000/predict/base64 \
  -H "Content-Type: application/json" \
  -d '{"image": "data:image/jpeg;base64,..."}'
```

#### Example Response

```json
{
  "success": true,
  "predictions": {
    "colors": ["Black", "White"],
    "products": ["T-shirt"]
  },
  "probabilities": {
    "colors": {
      "Black": 0.95,
      "White": 0.12,
      "Red": 0.03,
      ...
    },
    "products": {
      "T-shirt": 0.98,
      "Dress": 0.02,
      ...
    }
  }
}
```

## 📁 Project Structure

```
Automated-Product-Tagging-for-E-commerce/
├── fashion_model.py          # Model architecture builder
├── best_model.h5             # Trained model (96 MB)
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── src/
│   ├── app.py               # Flask API server
│   ├── train.py             # Training script
│   ├── predict.py           # Inference script
│   └── data_utils.py        # Data preprocessing utilities
├── data/
│   ├── images/              # Training images
│   └── fashion_dataset.csv  # Dataset labels
├── models/                   # Saved model checkpoints
├── notebooks/               # Jupyter notebooks
└── config/                  # Configuration files
```

## 🎨 Supported Classes

### Colors (10)
- Black
- White
- Red
- Blue
- Navy
- Grey
- Beige
- Pink
- Green
- Brown

### Products (10)
- T-shirt
- Dress
- Shirt
- Blouse
- Sweater
- Jacket
- Trousers
- Shorts
- Skirt
- Vest Top

## 🔧 Configuration

### Environment Variables

```bash
export MODEL_PATH=best_model.h5    # Path to model file
export PORT=5000                    # API server port
export DEBUG=False                  # Debug mode
```

### Training Parameters

Edit `src/train.py` to customize:
- `epochs`: Number of training epochs (default: 50)
- `batch_size`: Batch size (default: 32)
- `learning_rate`: Optimizer learning rate
- Data augmentation parameters

## 📊 Model Performance

The model uses:
- **Transfer Learning**: ResNet50 pre-trained on ImageNet
- **Frozen Base**: 95% of parameters frozen for faster training
- **Custom Head**: 2 dense layers with dropout and batch normalization
- **Multi-output**: Simultaneous color and product classification

## 🚀 Deployment

### Docker (Optional)

Create `Dockerfile`:
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "src/app.py"]
```

Build and run:
```bash
docker build -t fashion-tagger .
docker run -p 5000:5000 fashion-tagger
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**ALAN-PSUDO**
- GitHub: [@ALAN-PSUDO](https://github.com/ALAN-PSUDO)

## 🙏 Acknowledgments

- ResNet50 architecture from Keras Applications
- Pre-trained weights from ImageNet
- TensorFlow and Keras teams

---

**Note**: This is a demonstration project. For production use, consider:
- Adding authentication to the API
- Implementing rate limiting
- Using a production WSGI server (Gunicorn, uWSGI)
- Adding monitoring and logging
- Implementing model versioning
- Adding unit tests and CI/CD
