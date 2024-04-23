# Website with Fully Integrated Backend
This repository contains the code for designing a website with a fully integrated backend. The website is built to handle the following tasks:

**Loading PDF files into two different database tables:**
Electoral Bonds submitted by SBI on 21st March 2024 (EB_Redemption_Details)
Bonds encashed by political parties
Electoral Bonds submitted by SBI on 21st March 2024 (EB_Purchase_Details)
Bonds purchased by Individuals and Companies

**Steps**
*1. Backend Development*
a. PDF to CSV Conversion and Database Loading:
Used FITZ library in Python for PDF extraction and preprocessing.
Converted the extracted data to CSV format.
Loaded the CSV files into the database tables.

b. Database Integration:
Used My SQL to connect to the database and define ORM models.
Implemented functions to interact with the database (insert, query).

*2. Frontend Development*
c. Frontend Creation:
Developed the frontend using FLASK, Bootstrap, CSS, JavaScript, etc.
Implemented robust search functionality, dropdown/select options, and displayed data from the database in tables.

d. Database Connection:
Connected the frontend to the database to fetch and display data.

*3. Web Design*
e. Web Design Features:
Implemented various features as per requirements, including search functionality, dropdown options for filtering, and displaying data in tables.
Created bar plots and pie charts using ChartJS to visualize data.
![Screenshot 2024-04-23 225106](https://github.com/AnuragSingh0000/Electoral-Bond/assets/143340413/86dc9ec4-4519-4677-953a-88ccc276a4a7)
![Screenshot 2024-04-23 225126](https://github.com/AnuragSingh0000/Electoral-Bond/assets/143340413/48b2a038-b84a-41ec-a5bf-3f46cf34ed04)
![Screenshot 2024-04-23 225237](https://github.com/AnuragSingh0000/Electoral-Bond/assets/143340413/5f66afe4-9026-4cce-9ec6-3879427b6260)
![Screenshot 2024-04-23 225301](https://github.com/AnuragSingh0000/Electoral-Bond/assets/143340413/4e6cce33-19fd-41b6-ad04-27dd319dde76)
![Screenshot 2024-04-23 225309](https://github.com/AnuragSingh0000/Electoral-Bond/assets/143340413/78919a8c-f72f-4b07-b9ac-abc4d9a36c20)
![Screenshot 2024-04-23 225406](https://github.com/AnuragSingh0000/Electoral-Bond/assets/143340413/4603540b-810e-443e-a349-e16497efc97b)
![Screenshot 2024-04-23 225514](https://github.com/AnuragSingh0000/Electoral-Bond/assets/143340413/5e828bf9-bfa2-4f82-98d5-61cecfe7a68f)
![Screenshot 2024-04-23 225447](https://github.com/AnuragSingh0000/Electoral-Bond/assets/143340413/2740374c-483c-41d0-8f16-83ac0bb20785)
![Screenshot 2024-04-23 225554](https://github.com/AnuragSingh0000/Electoral-Bond/assets/143340413/3624125b-f202-4336-a65f-c692fba2660e)
![Screenshot 2024-04-23 231046](https://github.com/AnuragSingh0000/Electoral-Bond/assets/143340413/c920b7cc-ab2a-4fb6-ac48-a68e79d7f778)




f. Plot Saving Functionality:
Added functionality to save displayed plots in PNG/JPEG format.

**Plots**
Created and showcased plots using data fetched from the database.
Used ChartJS for displaying the plots, including bar charts, line charts, and pie charts.
Designed new ways to display results using unique plot types with ChartJS.
Note: For the detailed implementation of the website and backend functionality, please refer to the code in this repository. Screenshots of the UI can be found in the Readme file of the repository.

