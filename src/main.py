from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database.database import get_db, engine
from models.base import Base
from models.llm_usage import LLMUsage

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

app = FastAPI(title="MCP API")

@app.get("/")
def read_root():
    return {"message": "Welcome to MCP API"}

@app.get("/usage")
def get_usage(db: Session = Depends(get_db)):
    usage = db.query(LLMUsage).all()
    return usage 