from django.db import models

class SiteProfile(models.Model):
    name = models.CharField(max_length=100, default='Vignesh')
    title = models.CharField(max_length=200, default='Final-Year ECE Engineer & Full-Stack Developer')
    bio = models.TextField(default='Electronics & Communication Engineering student passionate about bridging robust hardware systems with modern full-stack web architectures and SQL databases.')
    email = models.EmailField(default='vigneshvicky24092005@gmail.com')
    github_url = models.URLField(default='https://github.com/vigneshvicky24092005-ai')
    linkedin_url = models.URLField(default='https://linkedin.com', blank=True)
    location = models.CharField(max_length=100, default='India')

    class Meta:
        verbose_name = 'Site Profile'
        verbose_name_plural = 'Site Profiles'

    def __str__(self):
        return f"{self.name} Profile"


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('software', 'Software & Web Development'),
        ('database', 'Database & SQL'),
        ('ece', 'ECE, Embedded & IoT'),
        ('tools', 'Tools & Workflow'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='software')
    proficiency = models.CharField(max_length=50, default='Proficient')
    icon_class = models.CharField(max_length=100, default='fas fa-code', help_text='FontAwesome class, e.g. fab fa-js')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend & JavaScript'),
        ('web', 'Web Applications'),
        ('database', 'Database & SQL Systems'),
        ('iot', 'IoT & Embedded Systems'),
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='web')
    description = models.TextField()
    tech_stack = models.CharField(max_length=300, help_text='Comma-separated tech tags, e.g., JavaScript, HTML5, CSS3')
    github_link = models.URLField(max_length=300)
    live_demo_link = models.URLField(max_length=300, blank=True, null=True)
    featured = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title

    def get_tech_list(self):
        return [tag.strip() for tag in self.tech_stack.split(',') if tag.strip()]


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=250)
    duration = models.CharField(max_length=100, help_text='e.g. 2021 - 2025')
    grade = models.CharField(max_length=100, blank=True, null=True, help_text='e.g. CGPA: 8.75 / 10.0')
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']
        verbose_name = 'Education'
        verbose_name_plural = 'Education'

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    issue_date = models.CharField(max_length=100)
    credential_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']
        verbose_name = 'Certification'
        verbose_name_plural = 'Certifications'

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f"Message from {self.name}: {self.subject}"
