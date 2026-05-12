# ML Pipeline

An end-to-end machine learning pipeline for data processing, model training, and evaluation using DVC (Data Version Control).

## Project Overview

This project implements a complete ML workflow that includes:
- Data collection and preprocessing
- Feature engineering and data preparation
- Model building and training
- Model evaluation and metrics tracking

## Project Structure

```
ml_pipeline/
├── data/
│   ├── raw/                          # Raw input data
│   │   ├── train_data.csv
│   │   └── test_data.csv
│   └── processed/                    # Processed data after preprocessing
│       ├── train_processed_data.csv
│       └── test_processed_data.csv
├── src/
│   ├── data_collection.py            # Data collection module
│   ├── data_prep.py                  # Data preprocessing and preparation
│   ├── data_model.py                 # Data model definitions
│   ├── model_building.py             # Model training
│   ├── model_eval.py                 # Model evaluation
│   └── main.py                       # Main pipeline execution
├── dvc.yaml                          # DVC pipeline configuration
├── params.yaml                       # Pipeline parameters
├── metrics.json                      # Model metrics and results
└── README.md                         # This file
```

## Setup & Installation

### Prerequisites
- Python 3.8 or higher
- Git
- DVC

### Installation

1. Clone the repository and navigate to the project:
```bash
cd ml_pipeline
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
# or
source .venv/bin/activate  # On macOS/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Pipeline

### Execute the full pipeline:
```bash
dvc repro
```

### Run specific stages:
```bash
# Data collection
python src/data_collection.py

# Data preparation
python src/data_prep.py

# Model building
python src/model_building.py

# Model evaluation
python src/model_eval.py
```

### Run the main pipeline:
```bash
python src/main.py
```

## Configuration

Pipeline parameters are defined in `params.yaml`. Modify these to adjust:
- Data preprocessing settings
- Model hyperparameters
- Train/test split ratios
- Other pipeline configurations

## Monitoring Results

View model metrics and performance in `metrics.json`. DVC tracks experiments and allows comparison across runs.

## Key Modules

- **data_collection.py** - Loads and collects raw data
- **data_prep.py** - Cleans, transforms, and prepares data for modeling
- **data_model.py** - Defines data structures and schemas
- **model_building.py** - Trains the machine learning model
- **model_eval.py** - Evaluates model performance and generates metrics
- **main.py** - Orchestrates the complete pipeline workflow

## Dependencies

All required packages are listed in `requirements.txt`. Key dependencies include:
- pandas - Data manipulation
- scikit-learn - Machine learning
- dvc - Pipeline versioning and tracking
- numpy - Numerical computations

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]
