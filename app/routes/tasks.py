from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_db
from app.models import Task
from app.schemas import TaskCreate, TaskUpdate, TaskOut
from app.utils.auth import get_current_user
from typing import Optional
from datetime import datetime
from sqlalchemy.sql import and_
from app.models import Task, User  # Add User to the imports

router = APIRouter()

@router.post("/", response_model=TaskOut)
async def create_task(
    task: TaskCreate, 
    db: AsyncSession = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    new_task = Task(**task.dict(), user_id=current_user.id)
    db.add(new_task)
    await db.commit()
    return new_task

@router.get("/", response_model=list[TaskOut])
async def filter_tasks(
    category: Optional[str] = Query(None),
    priority: Optional[int] = Query(None),
    due_date: Optional[datetime] = Query(None),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    filters = [Task.user_id == current_user.id]
    if category:
        filters.append(Task.category == category)
    if priority:
        filters.append(Task.priority == priority)
    if due_date:
        filters.append(Task.due_date == due_date)

    query = select(Task).where(and_(*filters))
    result = await db.execute(query)
    return result.scalars().all()

@router.put("/{task_id}", response_model=TaskOut)
async def update_task(
    task_id: int, 
    task: TaskUpdate, 
    db: AsyncSession = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    query = await db.execute(select(Task).where(Task.id == task_id, Task.user_id == current_user.id))
    db_task = query.scalar_one_or_none()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in task.dict(exclude_unset=True).items():
        setattr(db_task, key, value)
    await db.commit()
    return db_task

@router.delete("/{task_id}")
async def delete_task(
    task_id: int, 
    db: AsyncSession = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    query = await db.execute(select(Task).where(Task.id == task_id, Task.user_id == current_user.id))
    db_task = query.scalar_one_or_none()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    await db.delete(db_task)
    await db.commit()
    return {"message": "Task deleted"}
