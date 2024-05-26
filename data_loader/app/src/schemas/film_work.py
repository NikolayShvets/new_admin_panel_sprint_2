from typing import Literal, Annotated

from pydantic import BaseModel, Field, BeforeValidator


class FilmWork(BaseModel):
    table_name: Literal["film_work"] = Field(..., exclude=True)

    id: str
    title: str
    description: Annotated[str, BeforeValidator(lambda v: v if v else "")]
    creation_date: str | None
    rating: float | None
    type: str
    file_path: str | None
    created_at: str
    updated_at: str
