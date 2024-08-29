# NLP Tweet Classification Project

## Overview

This project focuses on classifying tweets using Natural Language Processing (NLP) techniques. A model from HuggingFace is employed for accurate and efficient tweet classification. The backend is developed using FastAPI and MongoDB to ensure robust data handling and scalable API services. The user interface is designed with Gradio, offering an intuitive and interactive experience for users to classify and analyze tweets effortlessly.

## Features

### 1. **Tweet Classification**
- **What It Does:** The project classifies tweets based on their content, helping users quickly categorize and analyze large volumes of Twitter data.
- **Why It’s Used:** NLP-based tweet classification is essential for social media analysis, sentiment analysis, and various other applications in data science and business intelligence.

### 2. **Backend with FastAPI**
- **What It Does:** The backend is built using FastAPI, a modern web framework for building APIs with Python.
- **Why It’s Used:** FastAPI is chosen for its high performance, ease of use, and asynchronous capabilities, which make it ideal for handling multiple API requests efficiently.
- **How It Works:** FastAPI processes incoming requests, interacts with the database, and communicates with the NLP model to provide classification results.

### 3. **Database with MongoDB**
- **What It Does:** MongoDB is used for storing tweet data and classification results.
- **Why It’s Used:** MongoDB’s flexibility and scalability make it suitable for handling large datasets, such as tweets, which can vary significantly in structure and volume.
- **How It Works:** The database stores raw tweet data and the corresponding classification results, allowing for efficient retrieval and analysis.

### 4. **User Interface with Gradio**
- **What It Does:** The user interface is built using Gradio, enabling users to interact with the tweet classification model directly through a web interface.
- **Why It’s Used:** Gradio provides a simple yet powerful platform for creating interactive machine learning demos, making it easy for users to input tweets and receive classification results.
- **How It Works:** Users input tweet text into the Gradio interface, which then sends the data to the backend for processing. The classification results are displayed in real-time, allowing users to analyze the outcomes instantly.

## Installation and Setup

### 1. **Clone the Repository**
```bash
git clone https://github.com/AsawirShafiq/Gradio-Tweet-Classification.git
cd Gradio-Tweet-classification
```
### 2. **Install Dependencies**
```bash
pip install -r requirements.txt
```
### 3. **Set up MongoDB**
- Ensure MongoDB is installed and running on your machine.
- Configure the connection settings in the project’s configuration file.
### 4. **Run the FastAPI Backend**
```bash
uvicorn main:app --reload
```
### 5. **Launch the Gradio Interface**
```bash
python interface.py
```


