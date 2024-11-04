from fastapi import (HTTPException, status)


class MicroserviceException(HTTPException):
    def __init__(self, *args: object, **kwargs: object) -> None:
        detail = kwargs.pop('detail', 'Microservice exception')
        if 'url' in kwargs:
            detail = f'{detail} - {kwargs.pop("url")}'
        status_code = kwargs.pop('status_code', status.HTTP_500_INTERNAL_SERVER_ERROR)
        super().__init__(status_code=status_code, detail=detail)


class UnProcessableMicroservice(MicroserviceException):
    def __init__(self, *args: object, **kwargs: object) -> None:
        message = kwargs.pop('message', 'Unprocessable in microservice')
        super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=message)


class BadRequestMicroservice(MicroserviceException):
    def __init__(self, *args: object, **kwargs: object) -> None:
        message = kwargs.pop('message', 'Bad request in microservice')
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=message)


class ErrorMicroservice(MicroserviceException):
    def __init__(self, *args: object, **kwargs: object) -> None:
        message = kwargs.pop('message', 'Error in microservice')
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=message)


class NotFoundInMicroservice(MicroserviceException):
    def __init__(self, *args: object, **kwargs: object) -> None:
        message = kwargs.pop('message', 'Not found in microservice')
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=message)


class NotAllowedMicroservice(MicroserviceException):
    def __init__(self, *args: object, **kwargs: object) -> None:
        message = kwargs.pop('message', 'Method not allowed in microservice')
        super().__init__(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail=message)


class DataRequired(HTTPException):
    def __init__(self, *args: object, **kwargs: object) -> None:
        message = kwargs.pop('message', 'Data required')
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail={
            'message': message,
        } | kwargs)


class EntityDoesNotExist(HTTPException):
    def __init__(self, *args: object, **kwargs: object) -> None:
        message = kwargs.pop('message', 'Entity does not exist')
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=message)


class NotSupported(HTTPException):
    def __init__(self, *args: object, **kwargs: object) -> None:
        message = kwargs.pop('message', 'Proccess not supported')
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=message)
