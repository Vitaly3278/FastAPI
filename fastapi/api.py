from fastapi import FastAPI, Body, status, HTTPException

app = FastAPI()
comments_db = {0: "First comment in FastAPI"}

@app.get("/comments")
async def get_comments() -> dict:
    return comments_db

@app.get("/comments/{comment_id}")
async def comment_details(comment_id: int) -> str:
    try:
        return comments_db[comment_id]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")

@app.post("/comments")
async def create_comment(comment : str =  Body(...)) -> str:
        current_index = max(comments_db) + 1 if comments_db else 0
        comments_db[current_index] = comment
        return "Comment created!"

@app.put("/comments/{comment_id}")
async def update_comment(comment_id: int, comment : str = Body(...)) -> str:
    if comment_id not in comments_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")
    comments_db[comment_id] = comment
    return "Comment updated!"

@app.delete("/comments/{comment_id}")
async def delete_comment(comment_id: int) -> str:
    if comment_id not in comments_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")
    comments_db.pop(comment_id)
    return "Comment deleted!"