import logging
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.status import HTTP_422_UNPROCESSABLE_CONTENT

logger = logging.getLogger(__name__)


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    errors = exc.errors()
    messages = [error["msg"] for error in errors]

    logger.warning(f"Validation error: {messages}")

    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_CONTENT,
        content={
            "error": messages[0] if messages else "Error de validación"
        },
    )


