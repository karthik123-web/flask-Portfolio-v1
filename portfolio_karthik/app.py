from flask import Flask, render_template, request

app = Flask(__name__)

# --- PERSONAL DATA ---
personal_info = {
    "name": "Muddam Karthik",
    "role": "Python Developer & Full Stack Aspirant",
    "about": "I don't just write code; I build solutions. With a strong foundation in Python and a passion for full-stack architecture, I transform complex problems into clean, scalable applications.",
    "email": "karthikmuddam122@gmail.com",
    "linkedin": "https://www.linkedin.com/in/karthik-muddam",
    "github": "https://github.com/karthik123-web6"
}

skills = [
    {"name": "Python", "level": "90%"},
    {"name": "Flask", "level": "85%"},
    {"name": "HTML/CSS", "level": "80%"},
    {"name": "SQL", "level": "75%"},
    {"name": "PowerBI", "level": "70%"},
    {"name": "Git/GitHub", "level": "85%"}
]

projects_data = [
    {"title": "IoT Health Monitor", "category": "IoT & Python", "desc": "Real-time vitals monitoring system using Raspberry Pi with cloud data visualization.", "tech": "Python, Sensors, Cloud"},
    {"title": "Hospital Bed Dashboard", "category": "Data Analytics", "desc": "Interactive PowerBI dashboard to optimize hospital resource allocation and patient flow.", "tech": "PowerBI, Excel, SQL"},
    {"title": "News Scraper Engine", "category": "Automation", "desc": "Automated bot that extracts and categorizes global news headlines daily.", "tech": "Python, BeautifulSoup"},
    {"title": "User Management API", "category": "Backend Dev", "desc": "Secure REST API handling CRUD operations with authentication layers.", "tech": "Flask, JSON, SQL"},
    {"title": "Sales Analytics Suite", "category": "Data Science", "desc": "Processing large CSV datasets to derive actionable business insights.", "tech": "Pandas, Matplotlib"},
]

@app.route('/')
def home():
    return render_template('index.html', info=personal_info, skills=skills, projects=projects_data)

@app.route('/contact', methods=['POST'])
def contact():
    # In a real app, you'd add email logic here
    return render_template('index.html', info=personal_info, skills=skills, projects=projects_data, success=True)

if __name__ == '__main__':
    app.run(debug=True)