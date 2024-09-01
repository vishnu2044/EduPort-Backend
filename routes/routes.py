API_ROUTES = [
    [
        "Admin login api",
        {
            "count": "1",
            "path": "/authentication/admin-login/",
            "methods": ["POST"],
            "input": {
                "username": "string",
                "password": "string"
            },
            "return": {
                "access": "string",
                'refresh': "string",
                "is_admin": "Boolean",
                "status": 'int',
                "message": "string"
            }
        }

    ],
    [
        "Token refresh api",
        {
            "count": "2",
            "path": "/authentication/token/refresh/",
            "methods": ["POST"],
            "input": {
                "refresh": "string"
            },
            "return": {
                "access": "string",
                'refresh': "string"
            }
        },

    ],
    [
        "User signup api (For both student and teacher)",
        {
            "count": "3",
            "path": "/authentication/user-signup/",
            "methods": ["POST"],
            "input": {
                "username": "string",
                "first_name": "string",
                "email": "string",
                "last_name": "string",
                "user_type": "string",
                "password": "password"
            },
            "return": {
                "message": "string",
                "user_id": "int"
            }
        },
    ],
    [
        "User login api (For both student and teacher)",
        {
            "count": "4",
            "path": "/authentication/user-login/",
            "methods": ["POST"],
            "input": {
                "username": "vishnu",
                "password": "vishnu2044"
            },
            "return": {
                "refresh": "string",
                "access": "string",
                "user_profile": {
                    "id": "integer",
                    "user": {
                        "id": "integer",
                        "username": "string",
                        "first_name": "string",
                        "last_name": "string",
                        "email": "string",
                        "is_superuser": "boolean",
                        "is_active": "boolean",
                        "date_joined": "datetime"
                    },
                    "user_type": "string",
                    "phone": "string or null",
                    "alternate_email": "string or null",
                    "alternate_phone": "string or null",
                    "date_of_birth": "date or null",
                    "gender": "string",
                    "just_created": "boolean"
                }
            }
        },

    ],
]