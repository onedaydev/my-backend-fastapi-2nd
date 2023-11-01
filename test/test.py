from fastapi import FastAPI, Path, Body
from typing import Annotated

from pydantic import Field, BaseModel

app = FastAPI()


class Item(BaseModel):
    description: str | None = Field(default='abc', title='abcdfef', max_length=10)




@app.put("/{num}")
async def test(
    num: Annotated[int, Path(ge = 3, le=10)],
    description: Annotated[Item, Body(embed=True)]
):
    return num 
