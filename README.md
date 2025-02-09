# Text to Speech Generator using Google Cloud Text-to-Speech

This project is a simple Streamlit-based web application that converts text input into speech using Google Cloud's Text-to-Speech API.

## Features
- Convert text into high-quality speech.
- Uses Google Cloud's advanced text-to-speech models.
- Interactive Streamlit UI for ease of use.

## Installation and Setup

### Prerequisites
- Python 3.8+
- Google Cloud account with Text-to-Speech API enabled
- Streamlit installed
- Google Cloud SDK installed and authenticated

### Set Up Google Cloud Authentication

Follow this link to setup local authorization to use Google Vertex AI Services: https://cloud.google.com/sdk/docs/initializing

### Installing Dependencies
1. Clone the repository:
   ```sh
   git clone https://github.com/kakarlapudiakhilvarma1/Text-to-Speech-using-VertexAI.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Text-to-Speech-using-VertexAI
   ```
3. Create a virtual environment and activate it:
   ```sh
   conda create -p myenv python==3.10 -y
   conda activate myenv/   # On Windows use `venv\Scripts\activate`
   ```
4. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Running the Application
1. Ensure you have set up authentication (as described above).
2. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```

## Output Screenshots

![image](https://github.com/user-attachments/assets/9f4627c1-d41f-45c8-be22-de38c04f0823)

![image](https://github.com/user-attachments/assets/edf2d811-13ed-4719-84fd-f3014fff38f4)


## Notes
- Make sure your Google Cloud project has billing enabled to use the Text-to-Speech API.
- You can customize the voice and other parameters in the script.
- Ensure `GOOGLE_APPLICATION_CREDENTIALS` is set before running the app.

## License
This project is licensed under the MIT License.

## Contributing
Feel free to submit issues or pull requests to improve the project.


