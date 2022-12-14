from drf_yasg import openapi

request_body_login = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "username": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="username",
        ),
        "password": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="password",
        ),
    },
)