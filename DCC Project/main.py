from os import name
from flask import Flask, redirect, url_for, request, Response, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '#PASSWORD'
app.config['MYSQL_DB'] = 'DCCP'

mysql = MySQL(app)

def get_data():
    cursor=mysql.connection.cursor()
    cursor.execute('select distinct Name_of_the_Purchaser from bond_data1')
    Name_of_the_purchaser=cursor.fetchall()
    cursor.close()
    cursor=mysql.connection.cursor()
    cursor.execute('select distinct Name_of_Political_Party from bond_data')
    Name_of_Political_Party=cursor.fetchall()
    cursor.close()
    return Name_of_the_purchaser, Name_of_Political_Party

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search_records', methods=['GET','POST'])
def search_records():
    data = 0
    if request.method == 'POST':
        result_ = request.form
        cursor = mysql.connection.cursor()
        
        Encashed_fields = ["Bond_Number", "Name_of_the_Political_Party", "Date_of_Encashment", "Account_no_of_Political_Party", "Denominations","Pay_Branch_Code","Pay_Teller"]
        Purchased_fields = ["Bond_Number", "Name_of_the_Purchaser", "Date_of_Purchase", "Date_of_Enquiry", "Journal_Date", "Issue_Branch_Code", "Issue_Teller", "Reference_Number_URN"]
        if result_["table_selecter"] == "Purchased":
            k = "Purchased"

            for i in Purchased_fields:
                if i == result_["Fields_Purchased"]:
                    cursor.execute(f"select * from bond_data1 where {i} = %s", (result_["Field_val"],))
        else:
            k = "Encashed"
            for i in Encashed_fields:
                if i == result_["Fields_Encashed"]:
                    cursor.execute(f"select * from bond_data where {i} = %s", (result_["Field_val"],))


        data = cursor.fetchall()
        cursor.close()
        if len(data) == 0:
            data = "NA"

        return render_template("search_records.html",result = data, table = k)
    return render_template("search_records.html")


@app.route('/individual',methods=['POST','GET'])
def individual():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        value = request.form['Name_of_the_purchaser']
        cursor.execute("SELECT Bond_Number, Denominations, year from bond_data1 where Name_of_the_Purchaser = %s", (value,))
        data = cursor.fetchall()
        
        d = {}
        for row in data:
            Bond_number = row[0]
            Denominations = int(row[1].replace(',', ''))  # Remove commas and convert to integer
            year = row[2]
            d[year] = d.get(year, 0) + Denominations
        cursor.close()

        if len(data) == 0:
            return render_template('individual.html', individual_data=[['Not Found']])
        
        years = list(d.keys())
        amount = list(d.values())
        Name_of_the_purchaser, Name_of_Political_Party = get_data()
        return render_template('individual.html', individual_data=data, years=years, amount=amount, Name_of_the_purchaser=Name_of_the_purchaser, Name_of_Political_Party=Name_of_Political_Party)

    return render_template('individual.html')

@app.route('/get', methods=['POST'])
def get():
    return individual()

@app.route('/party', methods=['POST', 'GET'])
def party():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        value = request.form['Name_of_Political_Party']
        cursor.execute("SELECT Bond_Number, Denominations, year from bond_data where Name_of_Political_Party = %s", (value,))
        data = cursor.fetchall()
        d = {}
        for row in data:
            Bond_number = row[0]
            Denominations = int(row[1].replace(',', ''))  # Remove commas and convert to integer
            year = row[2]
            d[year] = d.get(year, 0) + Denominations
        cursor.close()

        if len(data) == 0:
            return render_template('party.html', party_data=[['Not Found']])

        years = list(d.keys())
        amount = list(d.values())
        Name_of_the_purchaser, Name_of_Political_Party = get_data()
        return render_template('party.html', party_data=data, years1=years, amount1=amount, Name_of_the_purchaser=Name_of_the_purchaser, Name_of_Political_Party=Name_of_Political_Party)

    return render_template('party.html')

@app.route('/get2', methods=['POST'])
def get2():
    return party()

@app.route('/party_got', methods=['POST', 'GET'])
def party_got():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        value = request.form['Name_of_Political_Party']
        cursor.execute("SELECT Bond_number, Name_of_the_Purchaser, Denominations FROM bond_data1 WHERE Bond_number IN (SELECT Bond_number FROM bond_data WHERE Name_of_Political_Party = %s)", (value,))
        data = cursor.fetchall()
        cursor.close()

        if len(data) == 0:
            return render_template('party_got.html', party_got_data=[['Not Found']])

        d = {}
        for row in data:
            name_of_purchaser = row[1]
            denominations = int(row[2].replace(',', ''))  # Remove commas and convert to integer
            d[name_of_purchaser] = d.get(name_of_purchaser, 0) + denominations

        companies = list(d.keys())
        total_amount = list(d.values())
        name_of_purchaser, name_of_party = get_data()

        return render_template('party_got.html', companies=companies, total_amount=total_amount, party_got_data=list(d.items()), name_of_purchaser=name_of_purchaser, name_of_party=name_of_party)

    return render_template('party_got.html')

@app.route('/get3', methods=['POST'])
def get3():
    return party_got()

@app.route('/company_gave', methods=['POST', 'GET'])
def company_gave():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        value = request.form['Name_of_the_purchaser']
        cursor.execute("SELECT Name_of_Political_Party, Denominations FROM bond_data WHERE Bond_number IN (SELECT Bond_number FROM bond_data1 WHERE Name_of_the_Purchaser = %s)", (value,))
        data = cursor.fetchall()
        cursor.close()

        if len(data) == 0:
            return render_template('company_gave.html', company_gave_data=[['Not Found']])

        d = {}
        for row in data:
            name_of_party = row[0]
            denominations = int(row[1].replace(',', ''))  # Remove commas and convert to integer
            d[name_of_party] = d.get(name_of_party, 0) + denominations

        parties = list(d.keys())
        total_amount = list(d.values())
        name_of_purchaser, name_of_party = get_data()

        return render_template('company_gave.html', company_gave_data=list(d.items()), parties=parties, total_amount=total_amount, name_of_purchaser=name_of_purchaser, name_of_party=name_of_party)
    return render_template('company_gave.html')

@app.route('/get4', methods=['POST'])
def get4():
    return company_gave()

@app.route('/total_donations', methods=['POST'])
def total_donations():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT Name_of_Political_Party, SUM(CAST(REPLACE(Denominations, ',', '') AS DECIMAL(10,2))) AS Total_Denominations FROM bond_data GROUP BY Name_of_Political_Party");
        data = cursor.fetchall()
        cursor.close()

        if len(data) == 0:
            return render_template('total_donations.html', total_donations_data=[['Not Found']])

        d = {}
        for row in data:
            name_of_party = row[1]
            denominations = row[2]

        party = list(d.keys())
        total_amount = list(d.values())

        return render_template('total_donations.html', total_amount=total_amount, total_donations_data=list(d.items()), name_of_party=name_of_party)

    return render_template('total_donations.html')

if __name__ == '__main__':
   app.run(host="0.0.0.0", port="80", debug = True)
