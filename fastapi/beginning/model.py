from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/users/{username}")
async def login(username : Annotated[str, Path(min_length=3, max_length=15,
                                      description="Enter your name", example="Vitaly")],
                                      first_name : Annotated[str | None, Query(max_length=10)] = "FIRST") -> dict:
    return {"user": username, "age": first_name}
