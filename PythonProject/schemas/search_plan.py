from pydantic import BaseModel


class SearchPlanItem(BaseModel):
    reason: str
    query: str

class SearchPlan(BaseModel):
    searches: list[SearchPlanItem]