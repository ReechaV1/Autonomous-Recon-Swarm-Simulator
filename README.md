Autonomous Recon Swarm Simulation

An asynchronous, real-time telemetry dashboard and geospatial simulation engine built with FastAPI and Leaflet.js. 
The platform simulates autonomous reconnaissance units running 60 FPS orbital flight paths, 
performing continuous Ray-Casting Point-in-Polygon geofence breach detection across dark-mode Esri map tiles.

Key Features: 
- High-performance UI rendering 60 FPS agent trajectories and status updates without canvas lag.
- Geofence Breach Detection: Implements a custom Point-in-Polygon (Ray-Casting) algorithm to detect unauthorized entry into Restricted Zone Alpha.
- Live Event Logging: Auto-scrolling terminal-style sidebar log tracking deployments, state transitions
- Asynchronous FastAPI backend server built to serve frontend assets and easily interface with object-tracking pipelines
- Includes an isolated inference module (inference_engine.py) configured with YOLOv8 and Supervision ByteTrack for optional real-world vehicle tracking integrations.

Stack: 
Back - Python3, FastAPI, Uvicorn
Frontend - JavaScript (ES6+), Leaflet.js, Esri Dark Canvas Tiles, HTML5/CSS3
Computer Vision: OpenCV, Ultralytics YOLOv8, Supervision (ByteTrack)


┌─────────────────────────────────────────────────────────────┐
│                      FastAPI Server                         │
│                       (server.py)                           │
└──────────────────────────────┬──────────────────────────────┘
                               │ Serves Static UI
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                   Leaflet.js Dashboard                      │
│                      (dashboard.html)                       │
│                                                             │
│  ┌───────────────────────┐     ┌─────────────────────────┐  │
│  │   Telemetry Sidebar   │     │  Interactive Map Canvas │  │
│  │  - Latency / Unit Stats│     │  - Esri Dark Mode Tiles │  │
│  │  - Auto-scroll Logs   │     │  - Geofence Polygon     │  │
│  └───────────────────────┘     └────────────┬────────────┘  │
│                                             │               │
│                                 Calculates 60 FPS Orbits    │
│                                             │               │
│                                             ▼               │
│                                ┌─────────────────────────┐  │
│                                │   Point-in-Polygon      │  │
│                                │   Breach Detection      │  │
│                                └─────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘

Installation: 
(Bash)
git clone https://github.com/your-username/autonomous-recon-swarm-sim.git
cd autonomous-recon-swarm-sim

python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

pip install fastapi uvicorn opencv-python numpy supervision ultralytics (on terminal)

TO RUN: uvicorn server:app --reload --port 8000 (On your terminal)
[http://127.0.0.1:8000](http://127.0.0.1:8000) <- Open this in your web browser.

Structure:
autonomous-recon-swarm-sim/
│
├── server.py             # FastAPI web server hosting dashboard
├── dashboard.html        # Leaflet.js dashboard UI & simulation engine
├── inference_engine.py   # YOLOv8 + ByteTrack object tracking module
├── .gitignore            # Git exclusion rules
└── README.md             # Project documentation
