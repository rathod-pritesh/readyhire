from fastapi import APIRouter, UploadFile, File, Form, HTTPException, status
from app.services.parser import parse_resume, ParsingError
from app.services.gemini import analyze_resume_and_job, GeminiUnavailableError, GeminiResponseValidationError
from app.models.response import ApplicationReadinessReport

router = APIRouter()

@router.post(
    "/analyze",
    response_model=ApplicationReadinessReport,
    status_code=status.HTTP_200_OK,
    summary="Analyze resume against job description",
    description="Extracts plain text from the uploaded PDF or DOCX resume, compares it against the provided job description using Gemini API, and returns a detailed alignment report.",
)
async def analyze(
    resume: UploadFile = File(default=None, description="The candidate's resume (PDF or DOCX format)"),
    job_description: str = Form(default=None, description="The plain text job description to analyze against"),
):
    # Debug print statements
    print(f"[DEBUG] resume type: {type(resume)}")
    if resume is not None:
        print(f"[DEBUG] resume filename: {resume.filename}")
        print(f"[DEBUG] resume content_type: {resume.content_type}")
    print(f"[DEBUG] job_description: {repr(job_description)}")

    # 1. Validate Job Description presence
    if job_description is None or not job_description.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Missing job description."
        )

    # 2. Validate Resume File presence
    if resume is None or not resume.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Missing resume."
        )

    # 3. Read Resume File Bytes
    try:
        resume_bytes = await resume.read()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to read the resume file: {str(e)}"
        )

    if not resume_bytes or len(resume_bytes) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The uploaded resume file is empty."
        )

    # 4. Parse Resume Content
    try:
        resume_text = parse_resume(resume_bytes, resume.filename, resume.content_type)
    except ParsingError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected parsing error occurred: {str(e)}"
        )

    # 5. Perform Gemini analysis and response schema validation
    try:
        report = analyze_resume_and_job(resume_text, job_description)
        return report
    except GeminiUnavailableError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(e)
        )
    except GeminiResponseValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected server error occurred during analysis: {str(e)}"
        )
