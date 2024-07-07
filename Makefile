run: 
	@uvicorn workout_api.main:app --reload

create-migrations:
	set PYTHONPATH=%PYTHONPATH%;%CD% && alembic revision --autogenerate -m $(d)

run-migrations:
	set PYTHONPATH=%PYTHONPATH%;%CD% && alembic upgrade head