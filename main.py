from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Imported from GitHub successfully!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "status": "active"}

if __name__ == "__main__":
    # Replit requires 0.0.0.0 to expose the server
    uvicorn.run(app, host="0.0.0.0", port=8080)
