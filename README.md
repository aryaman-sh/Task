# Task

## API 
The API code is located in the `/api` directory.  

Refer to `/api/README.md` for more details.

## Frontend
Located in the `/frontend` directory. Uses React and TypeScript.

## Running the App
There are two ways to run the app:

1. Using Docker
   - Run `docker-compose up --build` in the root directory. Note: Depending on your Docker configureation, you may need to us: `docker compose up --build`.
   - API runs on `localhost:8000`
   - Frontend runs on `localhost:5173`

2. Running services individually
   - Instructions on running the API locally in `/api/README.md`.
   - Instruction on running Frontend locally in `/frontend/README.md`.