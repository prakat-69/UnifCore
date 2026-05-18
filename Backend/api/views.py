from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from core.core_auth.services import register_user , get_user_profile ,update_user_profile


@api_view(['POST'])
def register_api(request):
    user, error = register_user(
        request.data.get("username"),
        request.data.get("email"),
        request.data.get("password")
    )

    if error:
        return Response(
            {"message": error},
            status=status.HTTP_400_BAD_REQUEST
        )

    return Response(
        {
            "message": "User registered successfully",
            "id": user.id,
            "username": user.username,
            "email": user.email,
        },
        status=status.HTTP_201_CREATED
    )

@api_view(['GET'])
def get_user_profile_api(request,user_id):
    user , error = get_user_profile(user_id)

    if error:
        Response(
            {"message":error},
            status= status.HTTP_404_NOT_FOUND
        )
    
    return Response(
        {
            "message": "User fetched successfully",
            "id": user.id,
            "username": user.username,
            "email": user.email,
        },status=status.HTTP_200_OK
    )

@api_view(['PATCH'])
def update_user_api(request, user_id):
    user, error = update_user_profile(
        user_id,
        username=request.data.get("username"),
        email=request.data.get("email"),
        password=request.data.get("password"),
    )

    if error:
        return Response(
            {"message": error},
            status=status.HTTP_400_BAD_REQUEST
        )

    return Response(
        {
            "message": "User updated successfully",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            }
        },
        status=status.HTTP_200_OK
    )