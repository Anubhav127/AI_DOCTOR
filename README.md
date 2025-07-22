# AI Nutritionist App

This project is a web application that acts as an AI Nutritionist. It leverages Google's Gemini Pro Vision model to analyze images of food items, calculate the total calories, and provide a detailed breakdown of each food item with its respective calorie count.

## Features

-   **Image-based Calorie Calculation:** Upload an image of your meal, and the application will identify the food items and estimate the total calories.
-   **Detailed Nutritional Information:** Get a list of all identified food items along with their individual calorie counts.
-   **User-Friendly Interface:** The application is built with Streamlit, providing a simple and intuitive user interface.

## Technologies Used

-   **Python:** The core programming language for the application.
-   **Streamlit:** An open-source app framework for Machine Learning and Data Science projects.
-   **Google Gemini Pro Vision:** A multimodal AI model that can understand information from both images and text.
-   **python-dotenv:** For managing environment variables.

## Setup and Installation

Follow these steps to set up and run the project locally.

### Prerequisites

-   Python 3.8 or higher
-   An IDE or code editor (e.g., VS Code)
-   A Google Gemini API Key. You can obtain one from [Google AI Studio](https://aistudio.google.com/).

### Installation Steps

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Anubhav127/AI_DOCTOR.git
    cd AI_DOCTOR
    ```

2.  **Create and activate a virtual environment:**

    -   **Using `venv`:**
        ```bash
        # For Windows
        python -m venv venv
        .\venv\Scripts\activate

        # For macOS/Linux
        python3 -m venv venv
        source venv/bin/activate
        ```

    -   **Using `conda`:**
        ```bash
        conda create --prefix ./venv python=3.10 -y
        conda activate ./venv
        ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a file named `.env` in the root directory of the project and add your Google Gemini API key as follows:
    ```
    GOOGLE_GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
    ```

## Usage

To run the application, execute the following command in your terminal:

```bash
streamlit run app.py
```

This will start the Streamlit server, and you can access the application by navigating to the URL displayed in the terminal (usually `http://localhost:8501`).

## Project Structure

```
.
├── .env                # Stores environment variables (e.g., API keys)
├── .gitignore          # Specifies files and directories to be ignored by Git
├── app.py              # The main Streamlit application script
├── requirements.txt    # A list of Python packages required for the project
└── venv/               # Virtual environment directory (ignored by .gitignore)
```

## How It Works

The application takes an image of a meal as input. This image is then processed and sent to the Google Gemini Pro Vision model along with a predefined prompt. The model analyzes the image, identifies the food items, and returns a detailed list of each item with its estimated calorie count. The results are then displayed to the user in a clean and readable format.

---

Feel free to customize this documentation further to better suit your project's needs.
