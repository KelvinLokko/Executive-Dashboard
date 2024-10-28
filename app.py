from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Function to establish database connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='95.217.63.56',
            database='business_kedebah',
            user='kedebahBusinessUser',
            password='n3wKedebahuSer!',
            port='1632',
        )
        if connection.is_connected():
            print("Connected to MySQL database")
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Route for Gross Profit Score
@app.route('/gross_profit_score', methods=['GET'])
def gross_profit_score():
    query = """
    SELECT 
      ( 
        (SELECT SUM(credit_amount - debit_amount) 
         FROM ledger_entries 
         WHERE account_id IN (0, 3, 5, 7, 11, 16, 19, 31, 41, 69, 81, 82, 97, 141, 146, 170, 209, 281, 308) 
         AND deleted_at IS NULL) 
        - 
        (SELECT SUM(debit_amount - credit_amount) 
         FROM ledger_entries 
         WHERE account_id IN (0, 3, 5, 7, 11, 16, 19, 31, 41, 69, 81, 82, 97, 141, 146, 170, 209, 281, 308) 
         AND deleted_at IS NULL) 
      ) AS Gross_profit_score;
    """
    return execute_query(query)

# Route for Total Revenue
@app.route('/total_revenue', methods=['GET'])
def total_revenue():
    query = """
    SELECT 
      (SELECT SUM(credit_amount - debit_amount) 
       FROM ledger_entries 
       WHERE account_id IN (0, 3, 5, 7, 11, 16, 19, 31, 41, 69, 81, 82, 97, 141, 146, 170, 209, 281, 308) 
       AND deleted_at IS NULL) AS Total_revenue;
    """
    return execute_query(query)

# Route for Gross Profit Margin
@app.route('/gross_profit_margin', methods=['GET'])
def gross_profit_margin():
    query = """
    SELECT 
      (
        (
          (SELECT SUM(credit_amount - debit_amount) 
           FROM ledger_entries 
           WHERE account_id IN (0, 3, 5, 7, 11, 16, 19, 31, 41, 69, 81, 82, 97, 141, 146, 170, 209, 281, 308) 
           AND deleted_at IS NULL) 
          - 
          (SELECT SUM(debit_amount - credit_amount) 
           FROM ledger_entries 
           WHERE account_id IN (0, 3, 5, 7, 11, 16, 19, 31, 41, 69, 81, 82, 97, 141, 146, 170, 209, 281, 308) 
           AND deleted_at IS NULL)
        ) 
        / 
        NULLIF((SELECT SUM(credit_amount - debit_amount) 
                FROM ledger_entries 
                WHERE account_id IN (0, 3, 5, 7, 11, 16, 19, 31, 41, 69, 81, 82, 97, 141, 146, 170, 209, 281, 308) 
                AND deleted_at IS NULL), 0) 
      ) * 100 AS Gross_profit_margin;
    """
    return execute_query(query)

# Function to execute a query and return the result
def execute_query(query):
    # Create a connection to the database
    connection = create_connection()
    
    if connection is None:
        return jsonify({"error": "Failed to connect to the database"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchone()  # Use fetchone since we expect only one result
        return jsonify(result)
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()

# Main entry point for running the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
