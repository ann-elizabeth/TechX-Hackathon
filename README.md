# TechX-Hackathon
Personal Career Navigator:
AI-Based Skill Gap Analysis & Roadmap Engine
Project Summary
Personal Career Navigator is an AI-driven application that performs structured skill gap analysis by:
1)Extracting skills from GitHub repositories via REST API
2)Parsing resume PDFs for technical keywords
3)Comparing user skill sets with predefined job role requirements
4)Calculating match percentage
5)Generating a prioritized 7-day upskilling roadmap
The system demonstrates API integration, data processing, skill inference logic, and frontend visualization.

Technical Architecture
1.Data Layer (data.py)
GitHub REST API integration using requests
Resume parsing using PyPDF2
Keyword-based skill extraction
Job-role dataset loader (jobs.csv)
Error handling with fallback mechanisms
2.Intelligence Layer (agents.py)
Skill normalization & merging
Set-based skill comparison
Match score computation
Gap prioritization logic
Roadmap generation engine
Dynamic project recommendation
3.Presentation Layer (app.py)
Streamlit-based UI
Real-time analytics dashboard
Skill metrics visualization
Timeline roadmap layout

Key Algorithms Used
Set operations for skill comparison
Weighted match scoring
Priority-based roadmap allocation
Rule-based recommendation engine
 
 Example Skill Match Logic
Match % = (User Skills ∩ Required Skills) / Total Required Skills × 100

Tech Stack
Python
Streamlit
GitHub REST API
PyPDF2
Pandas
Requests

Engineering Highlights
Handles missing/partial GitHub data gracefully
Modular separation of concerns
Clean architecture design
Extendable job-role system
No hardcoded UI logic in business layer

Deployment
pip install -r requirements.txt
streamlit run app.py

Recruiter Takeaway
This project showcases:
API integration
Backend logic implementation
Data parsing & transformation
Applied problem-solving
User-focused product thinking

How It Works (Flow):
1.User enters:
GitHub username
Resume PDF
Dream role
Hours/day
Current level

2.System:
Fetches GitHub skills via API
Parses resume for technical skills
Loads job requirements
Compares skill sets
Calculates match score
Generates roadmap

3.Output:
Skill metrics
Gap analysis
7-day learning plan
Suggested resources
Project ideas

Example Output
Match Score:
Match Percentage: 60%
Missing Skills: Docker, REST APIs, Spring Boot

Roadmap:
Day 1 – Docker Basics  
Day 2 – REST API Fundamentals  
Day 3 – Spring Boot Intro  
Day 4 – Build Mini Backend Project  
Day 5 – Review + Coding Practice  
Day 6 – Portfolio Update  
Day 7 – Mock Interview Prep

Technologies Used:
Python
Streamlit
GitHub REST API
PyPDF2
Pandas
JSON-based rule engine
Custom CSS animations
