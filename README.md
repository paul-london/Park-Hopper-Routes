# 🗺️ Park Hopper Routes

A collaborative project between TripleTen Data Science and Software Engineering students focused on developing an online tool to plan a vacation to United States National Parks based on their starting location. The interactive experience also includes an itinerary view, featured parks, and helpful travel tips.

## 🌐 Live Demo

https://paul-london.github.io/Park-Hopper-Routes/

## 🛠️ Methodology & Findings

[Notebook](https://github.com/paul-london/Park-Hopper-Routes/blob/main/notebooks/Notebook.ipynb)

## 🚀 Project Overview

The goal of this project is to build a lightweight, functional tool that:

- Plans a vacation through a selection of US National Parks based on the user's starting location
- Applies a route optimization algorithm to minimize travel distance (Greedy Nearest Neighbor)
- Displays the determined travel route on an interactive map
- Provide additional park information and travel tips

## 📦 Features

- Clean and modular backend structure
- Simple but interactive frontend interface
- Input support: manual entry or uploaded data (e.g., CSV, JSON)
- Route optimization algorithm (Greedy Nearest Neighbors) with performance comparison to random route
- Integrated Google Maps driving data
- Support for six starting states

## 🧠 Technologies

#### Data Science
- Python  
- Greedy Nearest Neighbor algorithm  
- `pandas`, `numpy`, `folium`, `googlemaps`, `matplotlib` libraries

#### Software Engineering
- JavaScript, React, HTML, CSS, Vite  
- Git, GitHub Pages

## 📁 Project Structure (Summary)

```text
Park-Hopper-Routes/
├── public/                      # Public static assets
│   └── vite.svg
├── scripts/                     # Python scripts (e.g., for map generation)
│   └── generate_map.py
├── src/                         # Main React app source
│   ├── assets/                  # Local image assets
│   │   ├── github.png
│   │   └── parkimages/
│   │       └── *.jpg
│   ├── components/              # Shared reusable components
│   |   ├── App.jsx              # Top-level components
│   |   ├── Main.jsx
│   │   ├── Header.jsx
│   │   ├── Footer.jsx
│   │   ├── PlanTrip.jsx         # Interactive components
│   │   ├── ExplorePage.jsx
│   │   ├── MapDisplay.jsx
│   │   ├── Itinerary.jsx        # Display components
│   │   └── ParkCards.jsx
│   └── contexts/                # Static data context (parksData.js)
├── maps/                        # Generated HTML maps from Python
│   └── *.html
├── docs/                        # GitHub Pages deployment output (via `npm run deploy`)
│   ├── assets/                  # Vite-generated assets
│   ├── images/                  # Copied images for deployment (referenced by relative paths)
│   │   └── parkimages/
│   └── *.html                   # Embedded map pages
├── .gitignore
├── index.html                   # Main HTML template
├── package.json                 # Deployment script
├── README.md                    # This file
└── vite.config.js               # Vite configuration with GitHub Pages base path
```

## 🗓️ Timeline

| Phase          | Milestone                | Target Date |
| -------------- | ------------------------ | ----------- |
| 📌 Planning    | Define scope & algorithm | 7/17/2025   |
| 🔧 Development | Build core features      | 7/20/2025   |
| 🧪 Testing     | Deployment, submission   | 7/22/2025   |
| 🚀 Launch      | Presentation             | 7/23/2025   |

## 📊 Data Sources

- National Parks: Park coordinates and data were obtained from the [National Park Service](https://www.nps.gov) API ([Documentation](https://www.nps.gov/subjects/developer/api-documentation.htm)).
- Google Maps: Travel distances and durations were obtained from [Google Maps](https://www.google.com/maps) API ([Documentation](https://developers.google.com/maps/documentation)).
- US States: Coordinates were obtained from public [Kaggle dataset](https://www.kaggle.com/datasets/tennerimaheshwar/us-state-and-territory-latitude-and-longitude-data).

## 🧭 Next Steps

- Explore more advanced and accurate route algorithms.
- Create regional roadtrips based on starting location and their distance.
- Expand starting point selection to include all states and possibly cities.
- Generate route maps in real-time.

## 📬 Contact

We appreciate feedback and collaboration opportunities, so please reach out! See links below.

## 🧑‍🤝‍🧑 Team Members

| Name    | Role                 | GitHub | LinkedIn |
| ------- | -------------------- | -------------------- | -------------------- |
| Lily Thato Anderson   | Software Engineering | [Link](https://github.com/Thato-A) | 
| Vanessa Kwiatkoski | Software Engineering | [Link](https://github.com/VanessaK21) | [Link](https://www.linkedin.com/in/vanessa-kwiatkoski/)
| Paul London   | Data Science         | [Link](https://github.com/paul-london) | [Link](https://www.linkedin.com/in/palondon/)
| Matthew Richards | Software Engineering | [Link](https://github.com/matthewrichards234) | 
| Priti Sagar  | Data Science         | [Link](https://github.com/Priti0427) | [Link](https://www.linkedin.com/in/priti-sagar04/)

---
