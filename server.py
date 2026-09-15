from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Standard FastAPI app setup
app = FastAPI()

# Route to serve our Leaflet map dashboard
@app.get("/", response_class=HTMLResponse)
async def serve_dashboard():
    # Read the HTML file directly and return it
    with open("dashboard.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return html_content

if __name__ == "__main__":
    import uvicorn
    # Run server locally on port 8000
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)