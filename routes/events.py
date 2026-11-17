
from fastapi import APIRouter, Body, HTTPException, status
from typing import List
from models.events import Event

event_router = APIRouter(tags=["Events"])

# Временное хранилище событий
events = []


# Получить все события
@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    return events


# Создать событие
@event_router.post("/new", status_code=status.HTTP_201_CREATED)
async def create_event(body: Event = Body(...)) -> dict:
    if any(event.id == body.id for event in events):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Event with supplied ID already exists"
        )

    events.append(body)

    return {"message": "Event created successfully"}


# Удалить все события
@event_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {"message": "Events deleted successfully"}


# Получить одно событие
@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int) -> Event:
    for event in events:
        if event.id == id:
            return event

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )


# Удалить одно событие
@event_router.delete("/{id}")
async def delete_event(id: int) -> dict:
    for event in events:
        if event.id == id:
            events.remove(event)
            return {"message": "Event deleted successfully"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )
