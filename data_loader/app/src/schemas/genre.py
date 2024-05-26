from typing import Literal, Annotated

from pydantic import BaseModel, Field, BeforeValidator


class Genre(BaseModel):
    table_name: Literal["genre"] = Field(..., exclude=True)

    id: str
    name: str
    description: Annotated[str, BeforeValidator(lambda v: v if v else "")]
    created_at: str
    updated_at: str
