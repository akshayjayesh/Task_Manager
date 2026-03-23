# from fastapi import FastAPI, Depends
# from sqlalchemy.orm import Session
# from database import SessionLocal, engine
# import models, schemas

# from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()

# # CORS (important for React)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Create Task
# @app.post("/tasks")
# def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
#     new_task = models.Task(title=task.title)
#     db.add(new_task)
#     db.commit()
#     db.refresh(new_task)
#     return new_task

# # Get Tasks
# @app.get("/tasks")
# def get_tasks(db: Session = Depends(get_db)):
#     return db.query(models.Task).all()

# # Delete Task
# @app.delete("/tasks/{task_id}")
# def delete_task(task_id: int, db: Session = Depends(get_db)):
#     task = db.query(models.Task).filter(models.Task.id == task_id).first()
#     if task:
#         db.delete(task)
#         db.commit()
#     return {"message": "Deleted"}