# 💻 Laptop Price Prediction

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red.svg)](https://streamlit.io/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3%2B-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A machine learning project that predicts laptop prices based on various hardware specifications using advanced regression models and a user-friendly web interface.

## 🎯 Project Overview

This project leverages machine learning to predict laptop prices from technical specifications including brand, processor, RAM, GPU, display features, and more. The system uses a Gradient Boosting Regressor model with an R² score of **88.04%** and provides an interactive Streamlit web application for real-time predictions.

### ✨ Key Features

- **High Accuracy**: Gradient Boosting Regressor with 88.04% R² score
- **Interactive Web App**: User-friendly Streamlit interface
- **Comprehensive Feature Set**: 10+ technical specifications considered
- **Real-time Predictions**: Instant price estimates
- **Data-driven Insights**: EDA and feature engineering included
- **Model Comparison**: Evaluation of 9 different ML algorithms

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Laptop-Price-Prediction.git
   cd Laptop-Price-Prediction
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit pandas numpy scikit-learn xgboost matplotlib seaborn
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8501` to access the web application.

## 📊 Technical Architecture

### Data Pipeline

1. **Data Collection**: Laptop specifications dataset (1,303 samples)
2. **Preprocessing**: Feature engineering, encoding, and scaling
3. **Feature Engineering**: PPI calculation, binary indicators for touchscreen/IPS
4. **Model Training**: 9 ML algorithms compared
5. **Deployment**: Pickle serialization with Streamlit frontend

### Feature Set

| Feature | Type | Description |
|---------|------|-------------|
| Company | Categorical | Laptop brand (Dell, HP, Lenovo, etc.) |
| TypeName | Categorical | Laptop type (Notebook, Gaming, Ultrabook, etc.) |
| CPU | Categorical | Processor type and generation |
| RAM | Numerical | Memory in GB (2-128GB) |
| GPU | Categorical | Graphics card manufacturer |
| OS | Categorical | Operating system |
| Weight | Numerical | Weight in kg |
| Touchscreen | Binary | Touchscreen capability |
| IPS | Binary | IPS display panel |
| PPI | Numerical | Pixels per inch |

## 🤖 Model Performance

### Algorithm Comparison

| Model | R² Score | MAE | MSE |
|-------|----------|-----|-----|
| **Gradient Boosting** | **0.8804** | **0.1443** | **0.0378** |
| XGBoost | 0.8775 | 0.1459 | 0.0387 |
| Random Forest | 0.8668 | 0.1565 | 0.0420 |
| Decision Tree | 0.8175 | 0.1828 | 0.0576 |
| SVR | 0.8144 | 0.1811 | 0.0586 |
| AdaBoost | 0.8049 | 0.1967 | 0.0616 |
| Lasso | 0.7925 | 0.1951 | 0.0655 |
| Ridge | 0.7903 | 0.1967 | 0.0662 |
| Linear Regression | 0.7850 | 0.2001 | 0.0679 |

### Model Details

- **Best Model**: Gradient Boosting Regressor (300 estimators)
- **Training/Test Split**: 85%/15%
- **Target Variable**: Log-transformed price (for better distribution)
- **Feature Encoding**: OneHotEncoder for categorical variables
- **Pipeline**: ColumnTransformer + GradientBoostingRegressor

## 📈 Data Analysis & Insights

### Key Findings

- **RAM** has the strongest correlation with price (r = 0.73)
- **PPI** (Pixels Per Inch) shows significant impact on pricing
- **Gaming laptops** and **workstations** command premium prices
- **Apple** laptops tend to be priced higher than competitors
- **Touchscreen** and **IPS display** features add value

### Data Processing Steps

1. Removed duplicates and low-frequency brands
2. Engineered PPI feature from screen resolution and size
3. Created binary features for touchscreen and IPS displays
4. Simplified CPU categorization (Intel Core i3/i5/i7 vs others)
5. Grouped operating systems into major categories
6. Applied log transformation to price for normality

## 🖥️ Web Application Features

### User Interface

- **Brand Selection**: Choose from major laptop manufacturers
- **Type Selection**: Notebook, Gaming, Ultrabook, 2-in-1, etc.
- **Hardware Specs**: CPU, RAM, GPU configuration
- **Display Options**: Touchscreen, IPS panel, PPI settings
- **System Info**: Operating system and weight
- **Instant Results**: Real-time price prediction

### Technical Stack

- **Frontend**: Streamlit
- **Backend**: Python/Scikit-learn
- **Model Serialization**: Pickle
- **Data Processing**: Pandas, NumPy

## 📁 Project Structure

```
Laptop-Price-Prediction/
├── README.md                 # Project documentation
├── LICENSE                   # MIT License
├── app.py                    # Streamlit web application
├── Laptop_Price_Prediction.ipynb  # Jupyter notebook with full analysis
├── laptop_price.csv          # Raw dataset
├── df.pkl                    # Processed dataframe
├── pipe.pkl                  # Trained model pipeline
└── requirements.txt          # Python dependencies (create if needed)
```

## 🔧 Usage Examples

### Command Line Usage

```python
import pickle
import numpy as np

# Load model and data
df = pickle.load(open('df.pkl', 'rb'))
pipe = pickle.load(open('pipe.pkl', 'rb'))

# Make prediction
input_data = np.array([['Dell', 'Notebook', 'Intel Core i5', 8, 'Intel', 'Windows 10', 1.5, 0, 1, 141]])
prediction = pipe.predict(input_data)
price = np.exp(prediction[0])  # Reverse log transform
print(f"Predicted price: ${price:.2f}")
```

### Web Interface

1. Select laptop brand from dropdown
2. Choose laptop type (Gaming, Ultrabook, etc.)
3. Configure hardware specifications
4. Set display preferences
5. Click "Predict" for instant price estimate

## 📊 Dataset Information

- **Source**: Laptop price dataset with 1,303 samples
- **Features**: 13 original features, engineered to 10 final features
- **Target**: Price in Euros (converted to local currency)
- **Time Period**: Contemporary laptop models
- **Price Range**: ~$200 - $25,000

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Future Enhancements

- [ ] Add more laptop brands and models
- [ ] Implement deep learning models
- [ ] Add price trend analysis over time
- [ ] Include user reviews and ratings
- [ ] Deploy as cloud-based API
- [ ] Add mobile-responsive design
- [ ] Implement batch prediction feature

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Dataset providers for comprehensive laptop specifications
- Scikit-learn team for excellent ML tools
- Streamlit team for the web framework
- Open-source community for inspiration and tools

## 📞 Contact

If you have any questions or suggestions, feel free to reach out:

- Create an issue in this repository
- Connect on [LinkedIn](https://linkedin.com/in/suraj-g-rao)
- Email: surajgrao0203@gmail.com

---

**⭐ If this project helped you, please give it a star!**
