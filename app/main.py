
from fastapi import FastAPI
from routers import passwords, auth


app = FastAPI(
    title="FastPass"
    )

# Connecting routers for passwords
app.include_router(passwords.router)
app.include_router(auth.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to FastPass - password manager!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8081, reload=True)