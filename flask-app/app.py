from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    "host": "mysql-db",  # MySQL container name
    "user": "root",
    "password": "rootpassword",
    "database": "customdb"
}

@app.route("/", methods=["GET", "POST"])
def index():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    if request.method == "POST":
        user_input = request.form.get("user_input")
        if user_input:
            cursor.execute("INSERT INTO prompts (prompt) VALUES (%s)", (user_input,))
            conn.commit()

    cursor.execute("SELECT prompt FROM prompts")
    prompts = cursor.fetchall()
    
    conn.close()
    return render_template("index.html", prompts=prompts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
