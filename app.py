from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_frame_options(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Frame-Options"] = "ALLOWALL"
    return response

@app.get("/")
async def root():
    return {"message": "Hello from OpenHands Runtime Container"}

if __name__ == '__main__':
    import os
    import uvicorn
    port = int(os.getenv('PORT', 54178))
    uvicorn.run(app, host="0.0.0.0", port=port)
