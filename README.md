# name_picker

This application picks random names from a list without repeating. It is built using Flask for the backend and HTML/CSS/JavaScript for the frontend.

## Prerequisites

- Python 3.x
- Flask

## Installation

1. Clone the repository to your local machine:

    ```sh
    git clone https://github.com/ThePraxium/name_picker.git
    cd name_picker
    ```

2. Navigate to the `flask_app` directory:

    ```sh
    cd random_student_picker/flask_app
    ```

3. Install the required Python packages:

    ```sh
    pip install flask
    ```

## Running the Application

1. Ensure you have the `student_not-answered.txt` file with student names in the `flask_app` directory. Each name should be on a new line.

2. Run the Flask application:

    ```sh
    python app.py
    ```

3. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the application.

## Usage

- **Choose a Student**: Click the "Choose a Student" button to randomly select a student from the list of students who have not yet answered. The selected student's name will be displayed on the screen and added to the [student_answered.txt](http://_vscodecontentref_/0) file.
- **Reset List**: Click the "Reset List" button to clear the [student_answered.txt](http://_vscodecontentref_/1) file, allowing all students to be available for selection again.

## File Structure

- [app.py](http://_vscodecontentref_/2): The main Flask application file.
- [students.py](http://_vscodecontentref_/3): Contains the logic for loading, saving, and selecting students.
- [index.html](http://_vscodecontentref_/4): The HTML template for the web interface.
- `student_not-answered.txt`: A text file containing the list of students who have not yet answered.
- [student_answered.txt](http://_vscodecontentref_/5): A text file containing the list of students who have already answered.

## Notes

- Ensure that the `student_not-answered.txt` file is in the same directory as [students.py](http://_vscodecontentref_/6) and [app.py](http://_vscodecontentref_/7).
- The application will create and update the [student_answered.txt](http://_vscodecontentref_/8) file in the same directory.

## License

This project is licensed under the MIT License.