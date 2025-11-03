@app.post("/generate")
def generate_workflow(params: dict):
    return create_workflow(params)
