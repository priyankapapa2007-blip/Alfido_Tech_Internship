# Flask Fundamentals Demo

A simple Flask web application that demonstrates:
- Flask routing and templates
- GET and POST form handling
- Basic CRUD using an in-memory list
- Bootstrap-based UI

## Run locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the app:
   ```bash
   python app.py
   ```
3. Open http://127.0.0.1:5000/

## Test

```bash
python -m pytest -q
```

## Publish to GitHub

```bash
git add .
git commit -m "Initial Flask demo"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

## Deploy online

This project is ready for deployment on platforms such as Render or Railway.

- Render: create a new Web Service and connect this repository.
- Railway: create a new project from this repository and use the existing Flask settings.
