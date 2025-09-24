# traefik-example
This repository provides a minimal working example of integrating Traefik with a custom ForwardAuth middleware implemented in Python

It acts as a gatekeeper in front of the Google Maps API, verifying requests before forwarding them and securely attaching the API key.

/
├─ Test.ipynb # Notebook with an example of a good request/bad request 
├─ docker-compose.yml          # Orchestrates Traefik + Auth service
├─ gatekeeper/
│   └─ config/
│      ├─ traefik.yml          # Static Traefik config
│      └─ dynamic/             # Dynamic routers/middlewares/services
│         └─ dynamic.yml
└─ auth/
   ├─ Dockerfile               # Python container for auth service
   └─ app.py                   # FastAPI app providing auth-check

## How It Works
Client sends a request → https://localhost/geocode/json?...
- Traefik intercepts and calls the Auth Service.
- Auth Service checks the Authorisation header:
- ✅ If valid → responds 200 OK with X-Forwarded-Google-Api-Key: <real-key>.
- ❌ If invalid → responds 401 Unauthorised.
- Traefik forwards the request to Google Maps API, attaching the API key.

## Setup
- 1. Clone repository
  2. Replace GOOGLE_API_KEY docker-compose.yml
  3. run run.sh
  4. Open Test.ipynb and send a test request
 
  
