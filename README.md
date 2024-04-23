# Website with Fully Integrated Backend
This repository contains the code for designing a website with a fully integrated backend. The website is built to handle the following tasks:

**Loading PDF files into two different database tables:**
Electoral Bonds submitted by SBI on 21st March 2024 (EB_Redemption_Details)
Bonds encashed by political parties
Electoral Bonds submitted by SBI on 21st March 2024 (EB_Purchase_Details)
Bonds purchased by Individuals and Companies

**Steps**
1. Backend Development
a. PDF to CSV Conversion and Database Loading:

Used FITZ library in Python for PDF extraction and preprocessing.
Converted the extracted data to CSV format.
Loaded the CSV files into the database tables.
b. Database Integration:

Used SQLAlchemy to connect to the database and define ORM models.
Implemented functions to interact with the database (insert, query).
2. Frontend Development
c. Frontend Creation:

Developed the frontend using FLASK, Bootstrap, CSS, JavaScript, etc.
Implemented robust search functionality, dropdown/select options, and displayed data from the database in tables.
d. Database Connection:

Connected the frontend to the database to fetch and display data.
3. Web Design
e. Web Design Features:

Implemented various features as per requirements, including search functionality, dropdown options for filtering, and displaying data in tables.
Created bar plots and pie charts using ChartJS to visualize data.
f. Plot Saving Functionality:

Added functionality to save displayed plots in PNG/JPEG format.
Plots
Created and showcased plots using data fetched from the database.
Used ChartJS for displaying the plots, including bar charts, line charts, and pie charts.
Bonus Feature
Implemented additional features not specified in the requirements.
Designed new ways to display results using unique plot types with ChartJS.
GitHub Repository
Created a public GitHub repository for the assignment.
Pushed all files to the repository, including code and screenshots of the UI in the Readme file.
Provided instructions on how to set up the website locally and documented every aspect of the project.
Note: For the detailed implementation of the website and backend functionality, please refer to the code in this repository. Screenshots of the UI can be found in the Readme file of the repository.
