from typing import Optional
from pydantic import BaseModel, EmailStr


class SensorBase(BaseModel):
    type: str
    actual: int
    expected: int
    controller_id: int
    last_changed: int


class SensorIdRespose(BaseModel):
    id: int


class SensorCreate(BaseModel):
    type: str
    actual: int
    expected: int


class SensorUpdate(BaseModel):
    type: Optional[str] = None
    actual: Optional[int] = None
    expected: Optional[int] = None


class Sensor(SensorBase):
    id: int
    controller_id: int

    class Config:
        orm_mode = True


class ControllerBase(BaseModel):
    force_enable: bool
    start_time: int
    end_time: int
    repeat: bool
    status: bool


class ControllerCreate(BaseModel):
    repeat: bool
    status: bool
    force_enable: bool
    email: EmailStr


class ControllerIdRespose(BaseModel):
    id: int


class ControllerUpdate(BaseModel):
    force_enable: Optional[bool] = None
    start_time: Optional[int] = None
    end_time: Optional[int] = None
    repeat: Optional[bool] = None
    status: Optional[bool] = None


class Controller(ControllerBase):
    email: EmailStr
    sensors: list[Sensor] = []

    class Config:
        orm_mode = True
