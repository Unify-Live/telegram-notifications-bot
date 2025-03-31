from pydantic import BaseModel, Field


class NewNotification(BaseModel):
    tg_chat_id: int = Field(..., description="Telegram chat ID")
    content: str = Field(..., description="Message content")
