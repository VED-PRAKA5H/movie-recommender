# Movie Recommender System

## Project Overview
The Movie Recommender System is a machine learning project that provides personalized movie recommendations based on user preferences and historical data. This project utilizes collaborative filtering and content-based filtering techniques to suggest movies that users are likely to enjoy. By implementing this system, I aimed to enhance user experience and engagement in movie selection.

## Key Features
- **Data Collection**: Utilized the PMDB 500 Movie Dataset, which includes detailed information about movies, such as metadata and credits.
- **Data Preprocessing**: Cleaned and prepared the dataset for analysis, handling missing values and merging datasets effectively.
- **Recommendation Algorithms**: Implemented both content-based and collaborative filtering algorithms to generate movie recommendations based on user behavior and movie attributes.
- **Web Application Development**: Developed a user-friendly web interface that allows users to interact with the recommendation system seamlessly.
- **Deployment**: Deployed the application on a cloud platform to make it accessible to users.

## Project Structure
```text
movie-recommender/
│
├── data/
│ ├── raw/ # Original, immutable data dump
│ ├── processed/ # Cleaned and processed data
│ └── README.md # Description of the data used
│
├── notebooks/ # Jupyter notebooks for exploration
│ ├── EDA.ipynb # Exploratory Data Analysis
│ └── model_training.ipynb # Model training and evaluation
│
├── src/ # Source code for the project
│ ├── `__init__.py` # Makes src a Python package
│ ├── data_preprocessing.py # Data preprocessing functions
│ ├── model.py # Model definition and training functions
│ └── utils.py # Utility functions
│
├── tests/ # Unit tests for the project
│ └── test_model.py # Tests for the model
│
├── requirements.txt # List of dependencies
├── README.md # Project overview and instructions
└── main.py # Main script to run the application
```

## Technologies Used
- **Programming Languages**: Python==3.12.4
- **Libraries**: Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib, Flask
- **Tools**: Jupyter Notebook, Git, GitHub
- **Deployment**: Heroku/AWS

## Installation
To set up the project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/VED-PRAKA5H/movie-recommender.git
   cd movie-recommender
   ```
2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```
# Usage
  ```bash
    python main.py

