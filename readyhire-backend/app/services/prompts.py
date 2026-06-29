def build_analysis_prompt(resume_text: str, job_description: str) -> str:
    """
    Builds the analysis prompt instructing Gemini to compare the parsed resume
    against the target job description.
    """
    return f"""
You are an expert ATS (Applicant Tracking System) optimizer and professional career consultant.
Your task is to analyze the candidate's Resume against the target Job Description and produce a detailed, high-quality Application Readiness Report.

RESUME CONTENT:
---
{resume_text}
---

JOB DESCRIPTION:
---
{job_description}
---

INSTRUCTIONS:
1. Compare the candidate's Resume against the target Job Description.
2. Evaluate and generate:
   - `readiness_score`: A score between 0 and 100 representing overall compatibility/alignment.
   - `matched_skills`: Group the skills that the candidate has in their resume which match the job requirements into logical categories (e.g., "Frontend Development", "APIs & Databases", etc.). For each category, list the matched skills and a rating (0 to 100) representing strength of coverage.
   - `missing_skills`: Identify skills, tools, or qualifications explicitly or implicitly requested in the job description that are missing from the resume. For each missing skill, provide:
     * name: the skill name
     * type: "Hard Skill" or "Soft Skill"
     * importance: "Critical" (for core requirements), "Secondary" (for nice-to-haves), or "Optional"
     * reason: brief explanation of why this skill is needed based on the job description
   - `ats_keywords`: Extract key phrases, technologies, and terms from the job description and determine if they are present ("matched") or absent ("missing") in the resume. Return them as a list of keyword objects.
   - `resume_improvements`: Actionable suggestions for optimizing the resume content. For each improvement, provide:
     * category: the section (e.g., "Experience Section", "Summary Section", "Skills Section")
     * title: a brief optimization title
     * problem: the original weak phrasing or section from the resume
     * solution: a suggested professional rewrite (quantify impact where possible)
     * reason: why this improvement matters for ATS or hiring managers
   - `cover_letter`: Generate a highly tailored, compelling, professional cover letter draft (approx. 250-450 words) using the candidate's experience to pitch them for the job. Use professional spacing and language.
   - `interview_questions`: Tailor 3 mock interview questions the candidate is likely to face. For each, provide:
     * id: unique integer ID (1, 2, or 3)
     * question: the question text
     * tip: suggested answering strategy based on their profile
     * difficulty: "Easy", "Medium", or "Hard"
   - `checklist`: Create exactly 6 checklist items evaluating resume structure and content quality (e.g., "File Format", "Contact Info", "Page Count", "Action Verbs", "Section Headers", "Quantifiable Impact"). For each item, provide:
     * id: unique integer ID from 1 to 6
     * name: the checklist category name
     * status: "pass", "warn", or "fail"
     * desc: details of why it passed/warned/failed and recommendations
"""
