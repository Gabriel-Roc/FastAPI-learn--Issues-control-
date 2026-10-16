from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional

class IssueStatus(str, Enum):
    open = "open"
    in_progress = "in_progress"
    closed = "closed"

class IssuePriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

'''
the two above are enums used to be chosen as on the following models
'''

class IssueCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=5, max_length=1000)
    priority: IssuePriority = IssuePriority.medium #sets it as "medium" by default
    # there is no status because it will be hard coded into it

class IssueUpdate(BaseModel):
    title: Optional[str] = Field(default=None, max_length=100)
    description: Optional[str] = Field(default=None, max_length=1000)
    priority: Optional[IssuePriority] = None
    status: Optional[IssueStatus] = None

class IssueOut(BaseModel):
    id: str
    title: str
    description: str
    priority: IssuePriority
    status: IssueStatus