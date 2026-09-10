from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.influencer_campaign_manager.schemas import AgenticInfluencerCampaignManagerSessionCreate, AgenticInfluencerCampaignManagerSessionResponse
from app.domain.influencer_campaign_manager.service import AgenticInfluencerCampaignManagerService

router = APIRouter(prefix="/api/v1/influencer_campaign_manager", tags=["Agentic Influencer Campaign Manager Domain"])

@router.post("/sessions", response_model=AgenticInfluencerCampaignManagerSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticInfluencerCampaignManagerSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Influencer Campaign Manager.
    """
    return AgenticInfluencerCampaignManagerService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticInfluencerCampaignManagerSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticInfluencerCampaignManagerService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
