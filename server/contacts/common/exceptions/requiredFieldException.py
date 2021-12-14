class RequiredFieldException(Exception):
    def __init__(self, field: str):
        self.message = "Field " + field + " is required."

    def __str__(self) -> str:
        return self.message