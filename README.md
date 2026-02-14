Personal Career Navigator
AI-Powered Skill Gap Analysis & Career Roadmap Generator


1. Project Overview
   
Personal Career Navigator is an intelligent career analysis tool designed to help aspiring professionals understand where they stand and how to improve.
The system analyzes a user's existing technical skills from their GitHub profile and resume, compares them against industry job role requirements, identifies missing competencies, and generates a personalized learning roadmap.
Rather than guessing what to learn next, users receive data-driven guidance tailored to their target role.


2. Problem Statement
   
Many students and early-career developers struggle with:
Not knowing which skills are required for specific roles
Unclear understanding of their current skill level
Lack of structured learning direction
Overwhelming career advice without personalization
There is a gap between where learners are and where industry expects them to be.
This project bridges that gap.


3. Core Objective

The main objective of Personal Career Navigator is to:
Evaluate a candidate’s current skill set
Compare it with industry job role requirements
Identify skill gaps
Calculate compatibility percentage
Generate a short-term structured learning roadmap
The system transforms raw information into actionable insights.


4. System Workflow

The application follows a structured pipeline:

Step 1: Data Collection
Extract technical keywords from uploaded resume (PDF)
Fetch repository data from GitHub using API
Parse programming languages and technologies used

Step 2: Skill Standardization
Normalize extracted skills
Remove duplicates
Map skills to standardized job role datasets

Step 3: Skill Gap Analysis
Compare user skills with required role skills
Compute:
Matched skills
Missing skills
Match percentage

Step 4: Roadmap Generation
Prioritize missing skills
Distribute learning plan over 7 days
Suggest mini-project ideas


5. Key Features

   
GitHub profile skill extraction
Resume PDF parsing
Role-based skill comparison
Match percentage scoring
Missing skills identification
Personalized 7-day roadmap
Clean and modular architecture


6. Technical Architecture


The project is divided into modular components:
Frontend Layer
Streamlit-based interactive UI
Data Layer
GitHub REST API integration
Resume parsing module
Job role dataset (CSV)
Logic Layer
Skill comparison engine
Match scoring algorithm
Roadmap generation module
This separation improves scalability and maintainability.


7. Skill Matching Logic


The system calculates compatibility using:

Match Percentage = (Number of Matching Skills / Total Required Skills) × 100

Missing skills are ranked and prioritized to create a focused improvement plan.


8. Design Philosophy


This project is built on three principles:
Practicality – Focus on real-world applicability
Clarity – Provide clear, structured output
Actionability – Always provide next steps
The goal is not just analysis, but direction.


9. Potential Impact
   
Personal Career Navigator can be extended for:
University career guidance systems
Coding bootcamps
Placement preparation tools
Professional upskilling platforms
It demonstrates how structured data analysis can solve real educational problems.


10. Future Enhancements
    
Planned improvements include:
AI-based resume feedback scoring
Interview question generation
ATS compatibility analysis
OAuth GitHub authentication
Deployment as a cloud-hosted SaaS tool

Conclusion

Personal Career Navigator transforms career uncertainty into a structured improvement plan. By combining data extraction, skill analysis, and roadmap generation, it empowers users to move strategically toward their desired roles.

It is a demonstration of applied problem-solving using APIs, data processing, and intelligent logic design.
