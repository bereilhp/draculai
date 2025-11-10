.PHONY: back-dev back-prod

back-dev:
	cd backend && fastapi dev main.py

back-prod:
	cd backend && fastapi run main.py