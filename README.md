# Interview Script Tool

A Flask-based web application designed to facilitate structured interviews with automatic transcription and markdown export capabilities.

## Features

- 🎯 Structured interview flow with categorized questions
- 📝 Real-time response recording
- 📊 Automatic markdown transcript generation
- 🌐 Web-based interface for easy use
- 📋 Category-based question organization
- 🔄 Session management for multiple interviews

## Technology Stack

- Python 3.x
- Flask (Web Framework)
- HTML/CSS (Frontend)
- Markdown (Export Format)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/trentclat/interview-script-tool.git
cd interview-script-tool
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to `http://localhost:5000`

3. Click "Start Interview" to begin a new session

4. Answer questions as they appear

5. At the end of the interview, you can export the transcript in markdown format

## Project Structure

- `app.py` - Main Flask application and interview logic
- `templates/` - HTML templates for the web interface
- `interview_questions.txt` - Source file for interview questions
- `requirements.txt` - Python dependencies

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

Created by @trentclat 