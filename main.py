from fpdf import FPDF
from fpdf.enums import XPos, YPos

pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Add Unicode font
pdf.add_font("DejaVu", "", "DejaVuSans.ttf")
pdf.set_font("DejaVu", "", 12)

# Title
pdf.set_font("DejaVu", "", 16)
pdf.cell(0, 10, "Why You Should Program with Laravel", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

# Copyright
pdf.set_font("DejaVu", "", 10)
pdf.cell(0, 10, "© 2025 Marwane Elhosni", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
pdf.ln(10)

# Body content
content = """
Laravel is a popular PHP framework designed for building modern web applications. Known for its elegant syntax, extensive documentation, and robust ecosystem, Laravel has become a favorite among developers worldwide.

1. Elegant Syntax and MVC Architecture
Laravel’s syntax is clean and expressive. It follows the Model-View-Controller (MVC) architectural pattern, which separates logic, UI, and data, making your codebase organized and maintainable.

2. Robust Routing and Middleware
Laravel makes routing intuitive and flexible. Middleware allows developers to filter HTTP requests entering the application, helping in authentication, logging, and more.

3. Built-in Authentication and Authorization
Laravel provides ready-to-use tools for user authentication and role-based access control. This saves time and reduces vulnerabilities in custom implementations.

4. Blade Templating Engine
Laravel includes Blade, a simple yet powerful templating engine that allows you to build dynamic interfaces with ease.

5. Eloquent ORM (Object-Relational Mapping)
Eloquent makes interacting with databases more intuitive. You can manipulate database records as PHP objects without writing raw SQL queries.

6. Security Features
Laravel includes protection against CSRF, XSS, and SQL injection out-of-the-box. The framework uses secure password hashing and offers easy implementation of secure login systems.

7. Laravel Ecosystem
With tools like Laravel Forge, Laravel Vapor, Laravel Nova, Laravel Mix, and Laravel Sail, developers have a complete suite of tools to build scalable applications.

8. Vibrant Community and Learning Resources
Laravel has one of the most active communities in the PHP world. It is backed by high-quality documentation, Laracasts video tutorials, and a strong ecosystem of packages.

Conclusion:
Laravel isn’t just a framework—it’s a comprehensive development platform that empowers developers to build secure, maintainable, and feature-rich applications faster and more efficiently.
"""

pdf.set_font("DejaVu", "", 12)
for line in content.strip().split("\n"):
    pdf.multi_cell(0, 10, line.strip())
    pdf.ln(0.5)

# Save the PDF
pdf.output("C:/Users/hp/Documents/Why_Program_With_Laravel.pdf")
