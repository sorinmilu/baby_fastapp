from fastapi import FastAPI

app = FastAPI()

# Define static strings
greeting_message = "Hello, welcome to baby api app! About and contact are the other endpoints and docs shows API docs"
about_message = "This is a very simple fastapi app with three GET endpoints"
contact_message = "Contact us at contact@example.com."

@app.get("/")
def read_root():
    return {"message": greeting_message}

@app.get("/about")
def read_about():
    return {"message": about_message}

@app.get("/contact")
def read_contact():
    return {"message": contact_message}
