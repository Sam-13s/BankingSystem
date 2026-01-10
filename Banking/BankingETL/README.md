# Banking ETL Project


## Prerequisites

- Python 3.8 or higher
- Virtual environment (already set up in `../myenv/`)

## Installation

1. **Clone or navigate to the project directory:**
   ```
   cd Banking/BankingETL
   ```

2. **Activate the virtual environment:**
   - On Windows:
     ```
     ..\myenv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source ../myenv/bin/activate
     ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run database migrations:**
   ```
   python manage.py migrate
   ```

5. **Create a superuser (admin account):**
   ```
   python manage.py createsuperuser
   ```
   Follow the prompts to set up the admin username, email, and password.

## Running the Project

1. **Start the development server:**
   ```
   python manage.py runserver
   ```

2. **Access the application:**
   - Open your web browser and go to `http://127.0.0.1:8000/`
   - Login at `http://127.0.0.1:8000/accounts/login/`
   - Admin panel at `http://127.0.0.1:8000/admin/`

## Project Structure

- `bankingetl/`: Main Django project settings
- `customers/`: Customer management
- `accounts/`: Account management
- `transactions/`: Transaction handling
- `branches/`: Branch management
- `cards/`: Card management
- `employees/`: Employee management
- `loans/`: Loan management
- `reports/`: Reports and ETL logs
- `dashboard/`: Main dashboard
- `templates/`: HTML templates
- `static/`: Static files (CSS, JS, images)

## Features

- User authentication and authorization
- Customer and account management
- Transaction processing
- Branch and employee management
- Card services
- Loan management
- Reporting and ETL operations
- Dashboard for overview

## Technologies Used

- Django 4.2.20
- SQLite (default database)
- ReportLab (for PDF generation)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests if available
5. Submit a pull request

## License

This project is licensed under the MIT License.
