from pydantic import BaseModel


class Summary(BaseModel):
    summary: str

class FinalReport(BaseModel):
    short_summary: str
    markdown_report: str
    follow_up_questions: list[str]