import uvicorn 

if __name__ == "__main__":
    uvicorn.run('app.api.routes:app',port=8000,reload=True)