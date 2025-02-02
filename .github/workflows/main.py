from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the CSV file
df = pd.read_csv("q-fastapi.csv")

@app.get("/api")
def get_marks(name: list[str]):
    results = df[df['Name'].isin(name)]['Marks'].tolist()
    return {"marks": results}
