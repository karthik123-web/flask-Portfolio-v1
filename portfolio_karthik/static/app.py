from flask import Flask, render_template, request

app = Flask(__name__)

# --- PERSONAL DATA ---
personal_info = {
    "name": "Muddam Karthik",
    "role": "Python Developer & Full Stack Engineer",
    "about": "I engineer robust backend solutions and scalable architectures. Specialized in Python and Data Analytics, I bridge the gap between complex data and user-friendly applications.",
    "email": "karthikmuddam122@gmail.com",
    "linkedin": "https://www.linkedin.com/in/karthik-muddam",
    "github": "https://github.com/karthik123-web6"
}

skills = [
    {"name": "Python (Core & Advanced)", "level": "90%"},
    {"name": "Flask & API Development", "level": "85%"},
    {"name": "HTML5 / CSS3", "level": "80%"},
    {"name": "SQL & Database Design", "level": "75%"},
    {"name": "PowerBI & Analytics", "level": "70%"},
    {"name": "Git / Version Control", "level": "85%"}
]

projects_data = [
    {"title": "IoT Health Monitor", "category": "IoT System", "desc": "Real-time vitals monitoring system utilizing Raspberry Pi integration and cloud-based data visualization.", "tech": "Python, MQTT, Cloud API"},
    {"title": "Resource Dashboard", "category": "Data Analytics", "desc": "Interactive PowerBI dashboard designed to optimize hospital resource allocation and patient flow.", "tech": "PowerBI, SQL, Excel"},
    {"title": "News Automation Engine", "category": "Bot / Scripting", "desc": "Automated web crawler that extracts, categorizes, and archives global news headlines daily.", "tech": "Python, BeautifulSoup"},
    {"title": "User Management API", "category": "Backend Architecture", "desc": "Secure RESTful API handling complex CRUD operations with JWT authentication.", "tech": "Flask, SQLAlchemy, JSON"},
    {"title": "Sales Analytics Suite", "category": "Data Science", "desc": "Data processing pipeline transforming large CSV datasets into actionable business intelligence.", "tech": "Pandas, Matplotlib"},
]

@app.route('/')
def home():
    return render_template('index.html', info=personal_info, skills=skills, projects=projects_data)

@app.route('/contact', methods=['POST'])
def contact():
    # Logic to handle form submission would go here
    print(f"New message from {request.form.get('name')}") # meaningful log
    return render_template('index.html', info=personal_info, skills=skills, projects=projects_data, success=True)

if __name__ == '__main__':
    app.run(debug=True)