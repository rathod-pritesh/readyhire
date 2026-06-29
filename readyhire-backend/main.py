import uvicorn

def main():
    """Starts the FastAPI web server."""
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    main()
