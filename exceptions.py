student = {
    "name": "Mark",
    "student_id": 15977,
    "feedback": None
}

# Exception handling practice.
try:
    last_name = student ["last_name"]
except KeyError as error:
    print("Error finding last_name")
    print(error)
except Exception:
    print("Unknown Error")

    print("This code works and executes!")