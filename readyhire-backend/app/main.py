from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import settings
from app.routers import analyze

app = FastAPI(
    title="ReadyHire API",
    description="AI-powered Job Application Rescue backend utilizing Gemini",
    version="1.0.0",
)

# Configure CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include analysis routes
app.include_router(analyze.router, tags=["Analysis"])

@app.get("/", summary="Health Check")
def read_root():
    """Returns the service status and basic details."""
    return {
        "status": "online",
        "service": "ReadyHire API",
        "version": "1.0.0",
        "gemini_model": settings.GEMINI_MODEL
    }
