class HttpErrors:
    """Class to define errors in http"""

    @staticmethod
    def error_422():
        """HTTP 422 error"""

        return {
            "status_code": 422,
            "body": {
                "error": "Unprocessable Entity",
            },
        }

    @staticmethod
    def error_400():
        """HTTP 400 error"""

        return {
            "status_code": 400,
            "body": {
                "error": "Bad Request",
            },
        }

    @staticmethod
    def error_409():
        """HTTP 409 error"""

        return {
            "status_code": 409,
            "body": {
                "error": "Conflict",
            },
        }

    @staticmethod
    def error_500():
        """HTTP 500 error"""

        return {
            "status_code": 500,
            "body": {
                "error": "Internal Server Error",
            },
        }
