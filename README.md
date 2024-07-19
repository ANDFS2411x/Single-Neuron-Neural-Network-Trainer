# Single Neuron Neural Network Trainer

This application is a simple neural network trainer built using Python and Flask. It allows users to input training data, specify training parameters, and visualize the training process and predictions using a single neuron model. The app is designed for educational purposes to demonstrate how a basic neural network operates.

## Features

- Train a single neuron model using user-provided data.
- Customize learning rate and number of epochs.
- Visualize the loss function over epochs.
- Make predictions using the trained model.

## Files in the Repository

- `app.py`: The main Flask application file.
- `templates/index.html`: HTML template for the app's front-end.
- `static/images/`: Directory where the loss plot image is saved.

## Requirements

- Python 3.12.4
- Flask
- TensorFlow
- NumPy
- Matplotlib
- Waitress

## Setup and Installation

### Local Development

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install the required packages:**
    ```sh
    pip install Flask tensorflow numpy matplotlib waitress
    ```

5. **Run the application:**
    ```sh
    python app.py
    ```

6. **Access the application:**
    Open your browser and navigate to `http://127.0.0.1:8080/`.


## Usage

1. **Navigate to the homepage.**
2. **Enter the input data (comma-separated), output data (comma-separated), learning rate, number of epochs, and the value to predict.**
3. **Click on the "Entrenar y Predecir" button.**
4. **View the predicted value and the loss plot.**

## Contributing

If you would like to contribute to the project, please fork the repository and submit a pull request with your changes.


