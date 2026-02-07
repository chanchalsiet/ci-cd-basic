from app import greet

def test_greet():
    assert greet("CI/CD") == "Hello, CI/CD!"
