from flask import Flask, render_template, redirect, request, send_from_directory
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)


receiver_email = "shinothankachan17@gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port = 587
email_password = "uxml xtpm heek eobu"


def send_email(sender_email, name, email, subject, message):
    try:
    
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = f"New Contact Form Submission: {subject}"
        
       
        body = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage:\n{message}"
        msg.attach(MIMEText(body, 'plain'))
        
       
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  
            server.login(receiver_email, email_password)  
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)  
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")

@app.route('/')
def fun1():
    return render_template('index.html')

@app.route("/view_resume")
def view_resume():
    return send_from_directory(directory="static/images", path="DOC-20240905-WA0038.pdf")

@app.route('/submit', methods=['POST'])
def submit_form():
 
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']
    
   
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contact (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        subject TEXT,
                        message TEXT NOT NULL)''')
    cursor.execute("INSERT INTO contact (name, email, subject, message) VALUES (?, ?, ?, ?)",
                   (name, email, subject, message))
    conn.commit()
    conn.close()
    
    
    send_email(email, name, email, subject, message)  
    
   
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
