import os
 
def load_template(filename: str) -> str:
    base_path = os.path.dirname(__file__)
    with open(os.path.join(base_path, filename), encoding="utf-8") as f:
        return f.read() 