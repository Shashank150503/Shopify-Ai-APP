from fastapi import APIRouter
from agent.agent import AnalyticsAgent

router = APIRouter()

@router.post("/ask")
def ask_question(payload: dict):
    agent = AnalyticsAgent(payload["store_id"])
    return agent.run(payload["question"])
