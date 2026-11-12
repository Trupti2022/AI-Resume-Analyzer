from fastapi import FastAPI, UploadFile, File, Form, Request
import shutil

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.parser import extract_text_from_pdf
from app.skills import extract_skills
from app.analyzer import analyze_resume, get_grade
from app.similarity import calculate_similarity
from app.ai_helper import generate_feedback

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name ="index.html"
    )

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/upload")
async def upload_resume(
    request: Request,
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    print("UPLOAD ROUTE HIT")

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text_from_pdf(file_path)

    skills = extract_skills(extracted_text)

    analysis = analyze_resume(job_description, skills)

    similarity_score = calculate_similarity(extracted_text, job_description)
    resume_grade = get_grade(similarity_score)

    ai_feedback = generate_feedback(extracted_text, job_description)
    
    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "analysis": analysis,
            "similarity_score": similarity_score,
            "resume_grade": resume_grade,
            "ai_feedback": ai_feedback
        }
)