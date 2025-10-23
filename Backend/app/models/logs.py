from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Union
from datetime import datetime
from bson import ObjectId


# Utility to support MongoDB ObjectId
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

#chat model
class ChatMessage(BaseModel):
    message_id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    chat_id: str
    sender_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    content: Dict[str, Optional[str]] = Field(
        default_factory=lambda: {"text": None, "image": None, "audio": None}
    )
    metadata: Dict[str, Optional[Union[bool, List[str]]]] = Field(
        default_factory=lambda: {"read_status": False, "reactions": []}
    )
    attachments: Optional[List[str]] = Field(default_factory=list)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
