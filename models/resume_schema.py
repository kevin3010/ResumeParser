from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional


class PersonalInfo(BaseModel):
    name: str = Field(..., description="Full name of the candidate.")
    email: str = Field(..., description="Email address of the candidate.")
    phone: str = Field(..., description="Phone number of the candidate.")
    address: str = Field(..., description="Home address of the candidate.")


class EducationItem(BaseModel):
    degree: str = Field(..., description="Degree obtained by the candidate.")
    institution: str = Field(..., description="Name of the institution where the degree was obtained.")
    year: str = Field(..., description="Year of graduation.")


class ExperienceItem(BaseModel):
    job_title: str = Field(..., description="Title of the job held by the candidate.")
    company: str = Field(..., description="Name of the company where the candidate worked.")
    start_date: str = Field(..., description="Start date of the employment.")
    end_date: str = Field(..., description="End date of the employment.")
    responsibilities: List[str] = Field(..., description="A list of job responsibilities.")


class ProjectItem(BaseModel):
    name: str = Field(..., description="Name of the project.")
    project_description: List[str] = Field(..., description="A list of project description.")
    tools: List[str] = Field(..., description="A list of tools used in the project.")


class CertificationItem(BaseModel):
    name: str = Field(..., description="Name of the certification.")
    issuing_organization: str = Field(..., description="Organization that issued the certification.")
    year: str = Field(..., description="Year when the certification was obtained.")


class Resume(BaseModel):
    personal_info: PersonalInfo = Field(..., description="Contains the personal details of the candidate.")
    education: List[EducationItem] = Field(..., description="Educational qualifications of the candidate.")
    experience: List[ExperienceItem] = Field(..., description="Work experience of the candidate.")
    projects: Optional[List[ProjectItem]] = Field(None, description="Projects done by the candidate.")
    skills: List[str] = Field(..., description="Skills possessed by the candidate.")
    certifications: List[CertificationItem] = Field(..., description="Certifications held by the candidate.")
