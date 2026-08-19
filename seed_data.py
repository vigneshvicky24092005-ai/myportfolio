import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from django.contrib.auth import get_user_model
from core.models import SiteProfile, Skill, Project, Education, Certification

def seed():
    print("Starting database seeding for Vignesh Portfolio...")

    # 1. Site Profile
    SiteProfile.objects.all().delete()
    profile = SiteProfile.objects.create(
        name="Vignesh",
        title="Final-Year ECE Engineer & Full-Stack Developer",
        bio="Electronics & Communication Engineering student passionate about connecting smart hardware systems with modern full-stack web applications and scalable SQL databases.",
        email="vigneshvicky24092005@gmail.com",
        github_url="https://github.com/vigneshvicky24092005-ai",
        linkedin_url="https://linkedin.com",
        location="India"
    )
    print("[OK] SiteProfile created.")

    # 2. Projects
    Project.objects.all().delete()
    projects_data = [
        (
            "Full-Stack Django Portfolio Web App",
            "web",
            "A modern and responsive personal portfolio web application engineered with Python, Django, custom dark glassmorphic CSS, database admin management, and automated email inquiry forwarding.",
            "Python, Django, SQLite, JavaScript, HTML5, CSS3, Email Integration",
            "https://github.com/vigneshvicky24092005-ai/myportfolio",
            1
        ),
        (
            "JavaScript Counter App",
            "web",
            "A modern and interactive JavaScript counter web application built with vanilla JS, featuring responsive controls, increment/decrement step customization, persistent state, and clean glassmorphism UI.",
            "JavaScript, HTML5, CSS3, DOM Manipulation, LocalStorage",
            "https://github.com/vigneshvicky24092005-ai/javascript-counter-app",
            2
        ),
        (
            "Interactive Quiz Web Application",
            "web",
            "A dynamic quiz platform designed with timed challenges, category-based questions, automated score calculations, instant feedback, and responsive layout across all device viewports.",
            "JavaScript, CSS3, HTML5, JSON Data, Interactive UI",
            "https://github.com/vigneshvicky24092005-ai/Quiz-App",
            3
        ),
        (
            "Staff Management SQL Database System",
            "database",
            "A comprehensive enterprise relational database management system designed to track employee records, department structures, payroll calculation, attendance logs, and complex analytical SQL queries.",
            "SQL, Relational DB, Python, CRUD Architecture, Database Schema",
            "https://github.com/vigneshvicky24092005-ai/Staff-Management-SQL",
            4
        ),
    ]

    for title, cat, desc, tech, gh, ord_num in projects_data:
        Project.objects.create(
            title=title,
            category=cat,
            description=desc,
            tech_stack=tech,
            github_link=gh,
            featured=True,
            order=ord_num
        )
    print(f"[OK] {len(projects_data)} User Projects seeded successfully.")

    # 3. Skills
    Skill.objects.all().delete()
    skills_data = [
        # Software & Web
        ('JavaScript (ES6+)', 'software', 'Proficient', 'fab fa-js', 1),
        ('Python 3', 'software', 'Advanced', 'fab fa-python', 2),
        ('Django Framework', 'software', 'Proficient', 'fas fa-server', 3),
        ('HTML5 & Semantic Markup', 'software', 'Advanced', 'fab fa-html5', 4),
        ('CSS3 & Responsive Design', 'software', 'Advanced', 'fab fa-css3-alt', 5),
        ('DOM Manipulation', 'software', 'Proficient', 'fas fa-cubes', 6),
        # Database & SQL
        ('SQL Queries & Subqueries', 'database', 'Advanced', 'fas fa-database', 1),
        ('Relational Schema Design', 'database', 'Advanced', 'fas fa-table', 2),
        ('SQLite & Database Integration', 'database', 'Proficient', 'fas fa-server', 3),
        ('Data Normalization & Indexing', 'database', 'Proficient', 'fas fa-sitemap', 4),
        # ECE & IoT
        ('ESP32 & Microcontrollers', 'ece', 'Proficient', 'fas fa-microchip', 1),
        ('Embedded C / Arduino', 'ece', 'Proficient', 'fas fa-code', 2),
        ('IoT & MQTT Protocol', 'ece', 'Proficient', 'fas fa-satellite-dish', 3),
        ('Signal Processing Basics', 'ece', 'Intermediate', 'fas fa-wave-square', 4),
        ('Circuit Simulation', 'ece', 'Intermediate', 'fas fa-project-diagram', 5),
        # Tools
        ('Git & GitHub Workflows', 'tools', 'Proficient', 'fab fa-github', 1),
        ('VS Code & CLI Terminal', 'tools', 'Advanced', 'fas fa-terminal', 2),
        ('Postman API Testing', 'tools', 'Proficient', 'fas fa-flask', 3),
    ]
    for name, cat, prof, icon, ord_num in skills_data:
        Skill.objects.create(name=name, category=cat, proficiency=prof, icon_class=icon, order=ord_num)
    print("[OK] Technical Skills seeded.")

    # 4. Education
    Education.objects.all().delete()
    Education.objects.create(
        degree="B.E. in Electronics and Communication Engineering",
        institution="Engineering College / University",
        duration="2021 - 2025",
        grade="CGPA: 8.75 / 10.0 (Final Year)",
        description="Specialized in microcontroller systems, embedded development, digital signal processing, communication networks, and full-stack software architecture.",
        order=1
    )
    Education.objects.create(
        degree="Higher Secondary Certificate (HSC - 12th Grade)",
        institution="State Board Higher Secondary School",
        duration="2019 - 2021",
        grade="Score: 92.4%",
        description="Majored in Physics, Chemistry, Mathematics, and Computer Science with Distinction.",
        order=2
    )
    print("[OK] Education history seeded.")

    # 5. Certifications
    Certification.objects.all().delete()
    Certification.objects.create(
        title="Full-Stack Web Development with Python & Django",
        issuing_organization="Coursera / Udemy",
        issue_date="August 2024",
        credential_url="https://coursera.org",
        order=1
    )
    Certification.objects.create(
        title="Relational Database Design & SQL Query Optimization",
        issuing_organization="Database Systems Academy",
        issue_date="June 2024",
        credential_url="https://github.com/vigneshvicky24092005-ai/Staff-Management-SQL",
        order=2
    )
    Certification.objects.create(
        title="Modern JavaScript & Interactive Web UI Development",
        issuing_organization="Frontend Masters / FreeCodeCamp",
        issue_date="January 2024",
        credential_url="https://github.com/vigneshvicky24092005-ai/javascript-counter-app",
        order=3
    )
    print("[OK] Certifications seeded.")

    # 6. Django Superuser
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'vigneshvicky24092005@gmail.com', 'admin123')
        print("[OK] Superuser 'admin' created with password 'admin123'.")
    else:
        print("[INFO] Superuser 'admin' already exists.")

    print("\n[SUCCESS] All database data seeded successfully!")

if __name__ == '__main__':
    seed()
