from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.get('/jobs'):
async def get_jobs():
    return {'jobs': ['job1', 'job2', 'job3']}