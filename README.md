# Simple Quiz Game

A simple command-line and GUI (Flask) quiz game written in Python that allows users to test their knowledge through multiple-choice questions. The application provides feedback on the user's answers and displays their final score at the end of the quiz. The CLI version runs entirely in the terminal, while the GUI version offers an interactive web interface built using Flask.

## Features

- Multiple-choice questions
- Score tracking
- Immediate feedback on answers
- CLI and GUI (Flask) versions
- Unit tests using `pytest`

## GUI-Only Features

- User-friendly web interface
- Interactive question navigation
- Styled pages for a better user experience

## Getting Started

### Prerequisites

- Python 3.x installed
- `pip` (Python package manager)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/iamluckycheema/EcodeCamp_Task_Number_Three.git
   ```

2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

#### Method 1: CLI-Based

No extra dependencies are required beyond Python itself.

4. Run:

   ```bash
   python quiz_cli.py
   ```

##### CLI Usage

1. Answer Questions: Enter the letter corresponding to your answer choice and press Enter.
2. View Score: At the end of the quiz, your score will be displayed.
3. Restart or Exit: Choose to restart the quiz or exit the application.

#### Method 2: Flask GUI

For a more interactive experience with additional features, use the GUI version.

4. Run:

   ```bash
   python app.py
   ```

5. Open your browser and go to `http://127.0.0.1:5000/` to start the quiz.

##### GUI Usage

1. **Start Quiz:** Click the "Start Quiz" button on the homepage.
2. **Answer Questions:** Select your answer from the available options and click "Next" to proceed to the next question.
3. **View Results:** At the end of the quiz, your score will be displayed along with feedback on your performance.

### Customization

#### Styling

The Flask application uses basic CSS for styling. You can customize the appearance by modifying the `static/style.css` file.

#### Modifying the Questions

Questions are hardcoded in the application for simplicity. To modify or add new questions, you can edit the `quiz_cli.py` and `app.py` files.

### Testing the Application

Unit tests are provided to verify the functionality of the CLI and GUI versions of the application. To run the tests:

1. Install pytest:

   ```bash
   pip install pytest
   ```

2. Run the tests:

   ```bash
   pytest
   ```

### Contact

For any questions or concerns, please feel free to reach out to me at <iamluckycheema@gmail.com>.

---

This README provides a clear guide for users on how to set up, run, and customize your quiz game, with a structure similar to the To-Do List Application README you shared. Let me know if you'd like any further adjustments!
