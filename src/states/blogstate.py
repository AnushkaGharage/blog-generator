from typing import TypedDict
from pydantic import BaseModel, Field

class Blog(BaseModel):
    title: str = Field(description="title of the blog")
    content: str = Field(description="main content of the blog post")
    
    
class BlogState(TypedDict):
    topic:str
    blog:Blog
    current_language:str
    