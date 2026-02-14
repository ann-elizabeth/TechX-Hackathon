# 🚀 PERSON B: Career Navigator - Enhanced Data Layer (REAL IMPLEMENTATION)
# Profile: B.Tech CSE (AI & ML), Bengaluru

"""
INSTALLATION REQUIRED:
Before running, install these packages in your terminal:

pip install PyPDF2 requests

OR if using pip3:

pip3 install PyPDF2 requests
"""

import pandas as pd
import re

# Try importing optional dependencies
try:
    import PyPDF2
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False
    print("⚠️  PyPDF2 not installed. Resume parsing will use mock data.")
    print("   Install with: pip install PyPDF2")

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    print("⚠️  requests not installed. GitHub API will use mock data.")
    print("   Install with: pip install requests")


# -------------------------------
# 📦 GitHub Profile Extractor (REAL API)
# -------------------------------

def get_github_skills(github_user):
    """
    Extract skills from GitHub profile using GitHub API
    
    Args:
        github_user: GitHub username
        
    Returns:
        Dict with GitHub data including skills
    """
    
    if not github_user or not github_user.strip():
        return None
    
    # If requests is not available, use mock data
    if not REQUESTS_AVAILABLE:
        print(f"🔍 Using mock data for GitHub: {github_user}")
        return _get_mock_github_skills(github_user)
    
    try:
        print(f"🔍 Fetching real GitHub data for: {github_user}")
        
        # GitHub API endpoints
        user_url = f"https://api.github.com/users/{github_user}"
        repos_url = f"https://api.github.com/users/{github_user}/repos?per_page=100"
        
        # Fetch user data
        user_response = requests.get(user_url, timeout=10)
        
        if user_response.status_code == 404:
            print(f"❌ GitHub user '{github_user}' not found")
            return None
        
        if user_response.status_code != 200:
            print(f"⚠️  GitHub API error. Using mock data.")
            return _get_mock_github_skills(github_user)
        
        user_data = user_response.json()
        
        # Fetch repositories
        repos_response = requests.get(repos_url, timeout=10)
        repos = repos_response.json() if repos_response.status_code == 200 else []
        
        # Extract languages from repos
        languages = {}
        for repo in repos:
            if repo.get('language'):
                lang = repo['language']
                languages[lang] = languages.get(lang, 0) + 1
        
        # Calculate percentages
        total = sum(languages.values())
        top_languages = {}
        if total > 0:
            # Get top 4 languages
            sorted_langs = sorted(languages.items(), key=lambda x: x[1], reverse=True)[:4]
            for lang, count in sorted_langs:
                percentage = (count / total) * 100
                top_languages[lang] = f"{percentage:.0f}%"
        
        # Extract skills from languages and common tools
        skills = list(languages.keys())
        
        # Add common tools/frameworks based on languages
        skill_mappings = {
            'JavaScript': ['HTML', 'CSS', 'Node.js'],
            'Python': ['Data Structures', 'Algorithms'],
            'Java': ['Data Structures', 'Algorithms'],
            'TypeScript': ['JavaScript', 'HTML', 'CSS'],
            'C++': ['Data Structures', 'Algorithms'],
            'C': ['Data Structures', 'Algorithms']
        }
        
        for lang in languages.keys():
            if lang in skill_mappings:
                skills.extend(skill_mappings[lang])
        
        # Always add Git
        skills.append('Git')
        
        # Remove duplicates
        skills = list(set(skills))
        
        # Determine experience level based on repos and activity
        repos_count = user_data.get('public_repos', 0)
        if repos_count >= 20:
            experience_level = "intermediate-advanced"
        elif repos_count >= 10:
            experience_level = "beginner-intermediate"
        else:
            experience_level = "beginner"
        
        return {
            "username": github_user,
            "repos_count": repos_count,
            "experience_level": experience_level,
            "top_languages": top_languages,
            "skills": skills,
            "activity_level": "consistent" if repos_count >= 5 else "moderate"
        }
        
    except requests.exceptions.Timeout:
        print("⚠️  GitHub API timeout. Using mock data.")
        return _get_mock_github_skills(github_user)
    except requests.exceptions.RequestException as e:
        print(f"⚠️  GitHub API error: {e}. Using mock data.")
        return _get_mock_github_skills(github_user)
    except Exception as e:
        print(f"⚠️  Unexpected error: {e}. Using mock data.")
        return _get_mock_github_skills(github_user)


def _get_mock_github_skills(github_user):
    """Fallback mock data when API is unavailable"""
    return {
        "username": github_user,
        "repos_count": 8,
        "experience_level": "beginner-intermediate",
        "top_languages": {
            "Java": "35%",
            "C": "25%",
            "Python": "20%",
            "JavaScript": "20%"
        },
        "skills": [
            "Java",
            "C",
            "Python",
            "HTML",
            "CSS",
            "Data Structures",
            "Git",
            "Algorithms"
        ],
        "activity_level": "consistent"
    }


# -------------------------------
# 📄 Resume Parser (REAL PDF PARSING)
# -------------------------------

def extract_resume_skills(resume_file):
    """
    Extract skills from uploaded resume PDF
    
    Args:
        resume_file: Streamlit uploaded file object
        
    Returns:
        Dict with resume data including skills
    """
    
    if resume_file is None:
        return None
    
    # If PyPDF2 is not available, use mock data
    if not PDF_AVAILABLE:
        print("📄 Using mock resume data (PyPDF2 not installed)")
        return _get_mock_resume_data()
    
    try:
        print("📄 Parsing resume PDF...")
        
        # Read PDF content
        pdf_reader = PyPDF2.PdfReader(resume_file)
        
        # Extract text from all pages
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        # Normalize text
        text = text.lower()
        
        # Define skill keywords to search for
        programming_languages = [
            'python', 'java', 'javascript', 'c++', 'c', 'c#', 'ruby', 'go', 
            'rust', 'kotlin', 'swift', 'typescript', 'php', 'r', 'matlab'
        ]
        
        web_technologies = [
            'html', 'css', 'react', 'angular', 'vue', 'node.js', 'express',
            'django', 'flask', 'spring boot', 'bootstrap', 'tailwind'
        ]
        
        databases = [
            'sql', 'mysql', 'postgresql', 'mongodb', 'oracle', 'redis',
            'sqlite', 'cassandra', 'dynamodb'
        ]
        
        tools_frameworks = [
            'git', 'docker', 'kubernetes', 'aws', 'azure', 'gcp',
            'jenkins', 'ci/cd', 'linux', 'vs code', 'junit', 'maven', 'gradle'
        ]
        
        ai_ml = [
            'machine learning', 'deep learning', 'tensorflow', 'pytorch',
            'scikit-learn', 'keras', 'nlp', 'computer vision', 'pandas',
            'numpy', 'matplotlib'
        ]
        
        core_cs = [
            'data structures', 'algorithms', 'dbms', 'operating systems',
            'computer networks', 'oops', 'system design'
        ]
        
        # Extract skills found in resume
        found_languages = [lang for lang in programming_languages if lang in text]
        found_web = [tech for tech in web_technologies if tech in text]
        found_db = [db for db in databases if db in text]
        found_tools = [tool for tool in tools_frameworks if tool in text]
        found_ai = [ai for ai in ai_ml if ai in text]
        found_cs = [cs for cs in core_cs if cs in text]
        
        # Try to extract name (simple heuristic - first line might be name)
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        name = lines[0].title() if lines else "CS Student"
        
        # Try to extract CGPA/GPA
        cgpa_match = re.search(r'(?:cgpa|gpa)[:\s]+(\d+\.?\d*)', text)
        cgpa = float(cgpa_match.group(1)) if cgpa_match else 8.0
        
        # Try to extract degree
        degree = "B.Tech Computer Science"
        if 'b.tech' in text or 'bachelor' in text:
            if 'ai' in text and 'ml' in text:
                degree = "B.Tech Computer Science (AI & ML)"
            elif 'data science' in text:
                degree = "B.Tech Computer Science (Data Science)"
        
        return {
            "name": name,
            "education": {
                "degree": degree,
                "institution": "Engineering College",
                "year": "Current Student",
                "cgpa": cgpa
            },
            "technical_skills": {
                "languages": [lang.title() for lang in found_languages],
                "web": [tech.title() for tech in found_web],
                "databases": [db.upper() if db == 'sql' else db.title() for db in found_db],
                "ai_ml": [ai.title() for ai in found_ai],
                "core_cs": [cs.title() for cs in found_cs],
                "tools": [tool.title() for tool in found_tools]
            },
            "projects": [],  # Would need more sophisticated parsing
            "interests": ["Technology", "Problem Solving"],
            "strengths": ["Quick Learner", "Analytical Thinking"]
        }
        
    except Exception as e:
        print(f"⚠️  Error parsing PDF: {e}. Using mock data.")
        return _get_mock_resume_data()


def _get_mock_resume_data():
    """Fallback mock data when PDF parsing is unavailable"""
    return {
        "name": "CS Student",
        "education": {
            "degree": "B.Tech Computer Science (AI & ML)",
            "institution": "Bengaluru Engineering College",
            "year": "1st Year",
            "cgpa": 8.2
        },
        "technical_skills": {
            "languages": ["Java", "C", "Python"],
            "web": ["HTML", "CSS", "Basic JavaScript"],
            "core_cs": ["Data Structures", "Algorithms", "DBMS", "Operating Systems"],
            "tools": ["Git", "VS Code"]
        },
        "projects": [
            {
                "title": "Page Replacement Algorithm Simulator",
                "tech": ["Python"],
                "type": "Operating Systems Mini Project"
            },
            {
                "title": "Boutique Management DBMS System",
                "tech": ["SQL", "ER Diagram", "Oracle/MySQL"],
                "type": "Database Mini Project"
            }
        ],
        "interests": [
            "AI/ML",
            "Backend Development",
            "Problem Solving",
            "Hackathons"
        ],
        "strengths": [
            "Quick Learner",
            "Strong Logical Thinking",
            "Team Collaboration"
        ]
    }


# -------------------------------
# 📊 Job Requirements Loader
# -------------------------------

def load_job_requirements(role=None):
    """Load job requirements - returns dict or filters by role"""
    
    job_data = {
        "Software Engineer": {
            "required_skills": ["Java", "Python", "React", "Docker", "SQL", "Git", "REST APIs", "Data Structures", "Algorithms", "Communication"],
            "nice_to_have": ["Spring Boot", "Microservices", "AWS", "CI/CD"],
            "experience": "0-2 years"
        },
        "Data Scientist": {
            "required_skills": ["Python", "Pandas", "NumPy", "Machine Learning", "SQL", "Statistics", "Data Visualization", "Jupyter", "TensorFlow", "Communication"],
            "nice_to_have": ["Deep Learning", "NLP", "Big Data", "Spark"],
            "experience": "0-2 years"
        },
        "Fullstack Developer": {
            "required_skills": ["React", "Node.js", "JavaScript", "MongoDB", "Express.js", "Git", "REST APIs", "HTML", "CSS", "Docker"],
            "nice_to_have": ["TypeScript", "GraphQL", "AWS", "Next.js"],
            "experience": "0-2 years"
        },
        "Backend Developer": {
            "required_skills": ["Java", "Spring Boot", "SQL", "Git", "Data Structures", "REST APIs", "Microservices"],
            "nice_to_have": ["Docker", "Kubernetes", "Redis", "PostgreSQL"],
            "experience": "0-2 years"
        },
        "AI Engineer": {
            "required_skills": ["Python", "TensorFlow", "Statistics", "Machine Learning", "Deep Learning", "PyTorch", "NumPy"],
            "nice_to_have": ["MLOps", "Computer Vision", "NLP", "Model Deployment"],
            "experience": "0-2 years"
        }
    }
    
    if role:
        return job_data.get(role, job_data["Software Engineer"])
    return job_data


# -------------------------------
# 🧪 TEST HARNESS
# -------------------------------

if __name__ == "__main__":
    
    print("🧪 PERSON B: ENHANCED DATA TEST (REAL IMPLEMENTATION)\n")
    print("=" * 60)
    
    # Test GitHub (will use real API if requests is installed)
    github_data = get_github_skills("torvalds")  # Test with a real username
    print("\n📊 GitHub Data:")
    print(f"Username: {github_data['username']}")
    print(f"Repos: {github_data['repos_count']}")
    print(f"Skills: {github_data['skills'][:5]}...")
    
    # Test Resume (will use mock if no file provided)
    resume_data = extract_resume_skills(None)
    print("\n📄 Resume Data:")
    print(f"Name: {resume_data['name']}")
    print(f"Degree: {resume_data['education']['degree']}")
    print(f"Languages: {resume_data['technical_skills']['languages']}")
    
    # Test Job Requirements
    print("\n📋 Job Requirements:")
    jobs = load_job_requirements()
    for role in ['Software Engineer', 'Data Scientist']:
        print(f"\n{role}:")
        print(f"  Required: {jobs[role]['required_skills'][:3]}...")
    
    print("\n" + "=" * 60)
    print("🎉 DATA MODULE READY!")
    print("\n⚠️  INSTALLATION REMINDER:")
    print("   pip install PyPDF2 requests")
    print("=" * 60)