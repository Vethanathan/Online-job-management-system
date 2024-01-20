# Online Job Management System with Tkinter

## Project Overview

This repository contains an Online Job Management System developed in Python using Tkinter for the GUI. The system serves as a desktop application for managing job listings, applications, and recruitment processes. It provides a user-friendly interface for both employers and job seekers to streamline the entire job management lifecycle.

## Features

- **Job Listings:** Employers can post job listings with detailed descriptions, requirements, and application deadlines.
- **Job Applications:** Job seekers can submit applications online, attaching relevant documents and providing necessary details.
- **User Authentication:** Secure user authentication ensures data privacy and access control.
- **Automated Notifications:** Automatic notifications for application status updates, interview schedules, and other important events.
- **Tkinter GUI:** The system utilizes Tkinter for building the graphical user interface.
- **Python-Based:** Developed entirely in Python, ensuring simplicity and ease of customization.

## Requirements

Ensure you have the following dependencies installed:

- Python 3.x

Install required Python packages using:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the job management system script:

```bash
python app.py
```

2. Access the system through the Tkinter GUI and start managing job listings and applications.

## File Structure

- **`app.py`**: Main script for the job management system with Tkinter GUI.
- **`database/`**: Directory for storing the SQLite database file.
- **`icons/`**: Directory for storing icons used in the GUI.

## Configuration

Adjust the configuration parameters in `config.py` as needed:

```python
# Configuration Parameters
DATABASE_FILE = "database/site.db"
SECRET_KEY = "your_secret_key"
```

## Database

The system uses an SQLite database to store job listings, applications, and user data. The database file is located in the `database/` directory and named `site.db`.

## Acknowledgments

- Tkinter: [https://docs.python.org/3/library/tkinter.html](https://docs.python.org/3/library/tkinter.html)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## Contact

For any questions or inquiries, please contact [Vethanatahn] at [vethanathanvk@gmail.com].
