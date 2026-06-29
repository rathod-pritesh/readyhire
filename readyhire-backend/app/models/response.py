from pydantic import BaseModel, Field
from typing import List

class MissingSkill(BaseModel):
    name: str = Field(..., description="Name of the missing skill")
    type: str = Field(..., description="Type of skill, e.g., 'Hard Skill', 'Soft Skill'")
    importance: str = Field(..., description="Importance level, e.g., 'Critical', 'Secondary', 'Optional'")
    reason: str = Field(..., description="Short explanation of why this skill is needed based on the job description")

class MatchedSkillCategory(BaseModel):
    name: str = Field(..., description="Name of the skill category, e.g., 'Frontend Development', 'APIs & Databases'")
    skills: List[str] = Field(..., description="List of skills that matched in this category")
    rating: int = Field(..., description="Strength percentage rating in this category, from 0 to 100")

class ATSKeyword(BaseModel):
    keyword: str = Field(..., description="The keyword itself")
    status: str = Field(..., description="Status of the keyword, either 'matched' or 'missing'")

class ResumeImprovement(BaseModel):
    category: str = Field(..., description="Section of the resume, e.g., 'Experience Section', 'Summary Section'")
    title: str = Field(..., description="Brief title of the improvement")
    problem: str = Field(..., description="The original weak content from the resume")
    solution: str = Field(..., description="The suggested rewrite")
    reason: str = Field(..., description="Short explanation of why this rewrite helps")

class ChecklistItem(BaseModel):
    id: int = Field(..., description="Unique ID of the item")
    name: str = Field(..., description="Checklist item name, e.g., 'File Format', 'Contact Info', 'Quantifiable Impact'")
    status: str = Field(..., description="Status of the check, either 'pass', 'warn', or 'fail'")
    desc: str = Field(..., description="Description of the result or recommendation")

class InterviewQuestion(BaseModel):
    id: int = Field(..., description="Unique ID of the question")
    question: str = Field(..., description="The interview question")
    tip: str = Field(..., description="Suggested answer strategy tip")
    difficulty: str = Field(..., description="Difficulty level: 'Easy', 'Medium', 'Hard'")

class ApplicationReadinessReport(BaseModel):
    readiness_score: int = Field(..., description="Overall compatibility score out of 100", ge=0, le=100)
    matched_skills: List[MatchedSkillCategory] = Field(..., description="Matched skills grouped by category")
    missing_skills: List[MissingSkill] = Field(..., description="List of skills missing from the resume")
    ats_keywords: List[ATSKeyword] = Field(..., description="List of ATS keywords analyzed (both matched and missing)")
    resume_improvements: List[ResumeImprovement] = Field(..., description="Optimizations and suggested rewrites")
    cover_letter: str = Field(..., description="A full cover letter draft tailored to the job description and resume")
    interview_questions: List[InterviewQuestion] = Field(..., description="Tailored mock interview questions")
    checklist: List[ChecklistItem] = Field(..., description="Checklist for resume layout/content checks")
