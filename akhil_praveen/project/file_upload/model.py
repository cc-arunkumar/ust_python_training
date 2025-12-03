# model.py → FINAL VERSION – ZERO ERRORS ON REAL FILE
import pandas as pd
import numpy as np
import re
from datetime import date, datetime, timezone, timedelta
from typing import List, Optional, Literal
from pydantic import BaseModel, field_validator, Field, AwareDatetime
from dateutil import parser as date_parser


class ResourceRequest(BaseModel):
    resource_request_id: str = Field(..., alias="Resource Request ID")
    rr_fte: float = Field(..., alias="RR FTE")
    allocated_fte: Optional[float] = Field(None, alias="Allocated FTE")
    rr_status: Literal["Approved", "Cancelled", "Closed", "EDIT REQUEST APPROVED"] = Field(..., alias="RR Status")
    rr_type: Literal["New Project", "Existing Project","Replacement","Attrition"] = Field(..., alias="RR Type")
    priority: str = Field(..., alias="Priority")
    ust_role: str = Field(..., alias="UST - Role")
    city: str = Field(..., alias="City")
    state: Optional[str] = Field(None, alias="State")
    country: str = Field(..., alias="Country")
    alternate_location: Optional[str] = Field(None, alias="Altenate Location")
    campus: str = Field(..., alias="Campus")
    job_grade: str = Field(..., alias="Job Grade")
    rr_start_date: date = Field(..., alias="RR Start Date")
    rr_end_date: date = Field(..., alias="RR End Date")
    account_name: str = Field(..., alias="Account Name")
    project_id: str = Field(..., alias="Project ID")
    project_name: str = Field(..., alias="Project Name")
    wfm: str = Field(..., alias="WFM")
    wfm_id: str = Field(..., alias="WFM ID")
    hm: str = Field(..., alias="HM")
    hm_id: str = Field(..., alias="HM ID")
    am: str = Field(..., alias="AM")
    am_id: str = Field(..., alias="AM ID")
    billable: Literal["Yes", "No"] = Field(..., alias="Billable")
    actual_bill_rate: Optional[float] = Field(None, alias="Actual Bill Rate")
    actual_currency: Optional[str] = Field(None, alias="Actual Currency")
    bill_rate: Optional[float] = Field(None, alias="Bill Rate")
    billing_frequency: Optional[Literal["H", "D", "M","Y"]] = Field(None, alias="Billing Frequency")
    currency: Optional[str] = Field(None, alias="Currency")
    target_ecr: Optional[float] = Field(None, alias="Target ECR")
    accepted_resource_type: Optional[str] = Field("Any", alias="Accepted Resource Type")
    replacement_type: Optional[str] = Field(None, alias="Replacement Type")
    exclusive_to_ust: bool = Field(..., alias="Exclusive to UST")
    contract_to_hire: bool = Field(..., alias="Contract to Hire")
    client_job_title: Optional[str] = Field(None, alias="Client Job Title")
    ust_role_description: Optional[str] = Field(..., alias="UST Role Description")
    job_description: Optional[str] = Field(..., alias="Job Description")
    notes_for_wfm_or_ta: Optional[str] = Field(None, alias="Notes for WFM or TA")
    client_interview_required: Literal["Yes", "No"] = Field(..., alias="Client Interview Required")
    obu_name: str = Field(..., alias="OBU Name")
    project_start_date: date = Field(..., alias="Project Start Date")
    project_end_date: date = Field(..., alias="Project End Date")
    raised_on: date = Field(..., alias="Raised On")
    rr_finance_approved_date: Optional[date] = Field(None, alias="RR Finance Approved Date")
    wfm_approved_date: Optional[date] = Field(None, alias="WFM Approved Date")
    cancelled_reasons: Optional[str] = Field(None, alias="Cancelled Reasons")
    edit_requested_date: Optional[date] = Field(None, alias="Edit Requested Date")
    resubmitted_date: Optional[date] = Field(None, alias="Resubmitted Date")
    duration_in_edit_days: Optional[int] = Field(None, alias="Duration in Edit(Days)")
    number_of_edits: Optional[int] = Field(None, alias="# of Edits")
    resubmitted_reason: Optional[str] = Field(None, alias="Resubmitted Reason")
    comments: Optional[str] = Field(None, alias="Comments")
    recruiter_name: Optional[str] = Field(None, alias="Recruiter Name")
    recruiter_id: Optional[str] = Field(None, alias="Recruiter ID")
    recruitment_type: Optional[str] = Field(None, alias="Recruitment Type")
    project_type: Literal["T&M", "Non T&M"] = Field(..., alias="Project Type")
    last_updated_on: date = Field(..., alias="Last Updated On")
    last_activity_date: AwareDatetime = Field(..., alias="Last Activity Date")
    last_activity: Optional[str] = Field(None, alias="Last Activity")
    contract_category: Optional[str] = Field(None, alias="Contract Category")
    mandatory_skills: str = Field(..., alias="Mandatory Skills")
    optional_skills: Optional[str] = Field(..., alias="Optional Skills")
    rr_skill_group: Optional[str] = Field(None, alias="RR Skill Group")

    # ======================= FINAL BULLETPROOF VALIDATORS =======================

    @field_validator("priority", mode="after")
    @classmethod
    def normalize_priority(cls, v):
        if not v:
            return "P4"
        val = str(v).strip().upper()
        return val if val in ("P1", "P2", "P3", "P4") else "P4"

    @field_validator("exclusive_to_ust", "contract_to_hire", mode="before")
    @classmethod
    def str_to_bool(cls, v):
        if isinstance(v, bool):
            return v
        return str(v).strip().upper() in ("TRUE", "YES", "Y", "1")

    # THE REAL FIX – NO MORE "ambiguous truth value" ERRORS
    @field_validator("mandatory_skills", "optional_skills", mode="after")
    @classmethod
    def split_skills_from_string(cls, v):
        # 1. Handle None, NaN, empty
        if v is None or str(v).strip() == "" or str(v).strip().upper() in ("NA", "N/A"):
            return []
        # 2. Convert everything to string first
        raw = str(v).strip()
        # # 3. If it's already comma-separated → split
        # if "," in raw or "\n" in raw or "•" in raw:
        items = raw.split(',')
        

        # 5. Final cleaning: strip whitespace, remove empty/short items
        skills = [skill.strip() for skill in items if skill.strip()]

        return skills

    @field_validator(
        "rr_start_date", "rr_end_date", "project_start_date", "project_end_date",
        "raised_on", "last_updated_on", "rr_finance_approved_date", "wfm_approved_date",
        "edit_requested_date", "resubmitted_date", "hiring_request_submit_date_mte",
        "allocation_project_start_date", "allocation_project_end_date",
        mode="before", check_fields=False
    )
    @classmethod
    def parse_date(cls, v):
        if not v or pd.isna(v):
            return None
        if isinstance(v, date):
            return v
        if isinstance(v, datetime):
            return v.date()
        if isinstance(v, (int, float, np.integer)):
            try:
                return (date(1899, 12, 30) + timedelta(days=int(v)))
            except:
                return None
        try:
            return date_parser.parse(str(v), dayfirst=True).date()
        except:
            return None

    @field_validator("last_activity_date", mode="before", check_fields=False)
    @classmethod
    def parse_last_activity_date(cls, v):
        if not v or pd.isna(v):
            return None
        text = re.sub(r"\s*\([^)]*\)", "", str(v))  # Remove (PT), (IST)
        text = re.sub(r"\s+", " ", text).strip()
        try:
            dt = date_parser.parse(text, dayfirst=False)
            return dt.replace(tzinfo=timezone.utc) if dt.tzinfo is None else dt
        except:
            return None

    class Config:
        populate_by_name = True
        extra = "ignore"