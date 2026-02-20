"""
Application classes for FastAPI.
"""
from typing import Any, Dict, Optional, Sequence, Tuple, Type, Union

from fastapi.routing import APIRouter


class FastAPI:
    """
    The main FastAPI application class.
    """

    def __init__(
        self,
        *,
        debug: bool = False,
        routes: Optional[Sequence[Any]] = None,
        title: str = "FastAPI",
        description: str = "",
        version: str = "0.1.0",
        openapi_url: Optional[str] = "/openapi.json",
        openapi_tags: Optional[Sequence[Dict[str, Any]]] = None,
        servers: Optional[Sequence[Dict[str, Union[str, Any]]]] = None,
        **kwargs: Any,
    ) -> None:
        self.debug = debug
        self.title = title
        self.description = description
        self.version = version
        self.openapi_url = openapi_url
        self.openapi_tags = openapi_tags
        self.servers = servers
        self.routes = list(routes) if routes else []
        self.router = APIRouter()

    def include_router(
        self,
        router: APIRouter,
        *,
        prefix: str = "",
        tags: Optional[Sequence[str]] = None,
        dependencies: Optional[Sequence[Any]] = None,
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        **kwargs: Any,
    ) -> None:
        """
        Include a router in the application.
        """
        self.router.include_router(
            router,
            prefix=prefix,
            tags=tags,
            dependencies=dependencies,
            responses=responses,
            **kwargs,
        )
