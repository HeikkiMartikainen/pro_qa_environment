from pydantic import BaseModel, Field
from typing import List

class Credentials(BaseModel):
    """A set of user credentials with the expected error message."""
    username: str = Field(description="The username to test.")
    password: str = Field(description="The password to test.")
    expected_error: str = Field(description="The exact error message the application should display.")

class CredentialList(BaseModel):
    """A list of user credentials."""
    credentials: List[Credentials]
