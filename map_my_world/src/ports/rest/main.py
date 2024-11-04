# Genral imports
from fastapi import FastAPI, Request, status

# Finkargo
from map_my_world.config import SETUP
from map_my_world.src.ports.rest.router import router as api_router
from map_my_world.config.constants import PRODUCTION_ENV, STAGING_ENV, TESTING_ENV

# Healthcheck
from fastapi_healthcheck import HealthCheckFactory, healthCheckRoute

# Tables
from map_my_world.shared.adapters.db.sql.sessions import create_tables

# Error handling
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from typing import List

app = FastAPI()

app.include_router(api_router)


# Define el formato de error personalizado
def format_validation_error(exc: ValidationError) -> List[dict]:
    formatted_errors = []
    for error in exc.errors():
        formatted_errors.append({
            "input": error['loc'][-1],  # El nombre del campo
            "message": error['msg']  # El mensaje de error
        })
    return formatted_errors


# Registra el manejador de excepciones personalizado
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    formatted_errors = format_validation_error(exc)
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": formatted_errors},
    )


# Add Health Checks
_healthChecks = HealthCheckFactory()
app.add_api_route('/v1/healthcheck', endpoint=healthCheckRoute(factory=_healthChecks))


# Init tables
@app.get("/init_tables", status_code=status.HTTP_200_OK, name="init_tables")
async def init_tables():
    create_tables()
