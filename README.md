## BigProject

This project is part of the module of Web Services and Applications for the Data Analytics course at Atlantic Technological University, taught by Andrew Beatty.

#### The Requeriment for the project.

A basic Flask server that has a REST API, (to perform CRUD operations), One database table and Accompanying web interface, using AJAX calls, to perform these CRUD operations. 
Make it look nice 
Have more than one database table  
Link to an outside data source and either: 
• Save the data into a database table that you view elsewhere in your 
application. 
• Manipulate/analyse the data in real time. 
Hosted your application online (e.g.  Azure, Pythonanywhere). 
• This is the best way to showcase what you have done. 
▪ Be warned that some free hosting does not allow access to third party systems 
Perform more than CRUD operations on your data


## Installation Instructions

### Prerequisites
- Python 3.13
- MySQL database
- PythonAnywhere account (if deploying there)
- TMDB API account

### Setup Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/IanaraFer/bigproject.git
   ```

2. **Set up virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip Flask 
   pip install -r requirements.txt
   ```

4. **Database configuration**:
   - Rename `dbconfig_template.py` to `dbconfig.py`
   - For MySQL setup on PythonAnywhere

5. **Database setup**:
   - Create a MySQL database with the following tables:
   ```sql
   CREATE TABLE actor (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255),
       gender VARCHAR(255),
       dob DATE,
       country VARCHAR(250)
   );
   
   CREATE TABLE country (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(250) NOT NULL
   );
   ```

6. **Run the application**:
   ```bash
   python 


## Deployment to PythonAnywhere

1. Upload all files to your PythonAnywhere account
2. Create a new web app and configure it to use your WSGI file
3. Set up the MySQL database in PythonAnywhere's database tab
4. Configure the virtual environment and install requirements
5. Update the `dbconfig.py` with your PythonAnywhere MySQL credentials


## Troubleshooting
- **Database connection issues**: Verify credentials in `dbconfig.py` and ensure MySQL service is running, bookDAO and others...
- **TMDB API errors**: Check your API key and bearer token, and verify your TMDB account is active
- **Missing dependencies**: Run `pip install -r requirements.txt` to ensure all packages are installed


## References:
 
https://www.ibm.com/think/topics/api

https://en.wikipedia.org/wiki/API

https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging#_basic_merge_conflicts

https://flask.palletsprojects.com/en/latest/

https://docs.sqlalchemy.org/en/20/

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xi-email-support

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xi-email-support

https://help.pythonanywhere.com/pages/Flask/
