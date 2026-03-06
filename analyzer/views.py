from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .ai_engine import extract_text_from_pdf, extract_skills, calculate_score, missing_skills


def upload_resume(request):

    if request.method == "POST":

        # get uploaded resume
        resume = request.FILES["resume"]

        # save resume file
        fs = FileSystemStorage(location="media/resumes")
        filename = fs.save(resume.name, resume)
        filepath = fs.path(filename)

        # ---- AI Processing ----

        # extract text from pdf
        text = extract_text_from_pdf(filepath)

        # extract skills from resume
        skills = extract_skills(text)

        # job required skills
        job_skills = ["python", "django", "sql", "machine learning"]

        # calculate resume score
        score = calculate_score(skills, job_skills)

        # find missing skills
        missing = missing_skills(skills, job_skills)

        # send data to success page
        return render(request, "success.html", {
            "skills": skills,
            "score": score,
            "missing": missing
        })

    return render(request, "upload.html")