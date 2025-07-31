import streamlit as st
from map import plot_route_on_map
import os

# Set paths
repo_root = os.path.abspath(os.path.dirname(__file__))
states_file = os.path.join(repo_root, 'data', 'states_master.csv')
parks_file = os.path.join(repo_root, 'data', 'parks_subset.csv')
api_key = 'API_KEY'  # Use a free or restricted key

# UI: Title and input
st.title("🗺️ National Parks Roadtrip Planner")
home_state = st.selectbox("Choose your starting state:", [
    'CA', 'NY', 'TX', 'FL', 'PA', 'OH', 'IL', 'AZ', 'WA', 'CO', 'UT', 'SD', 'ND', 'NM'
])

if st.button("Generate Route"):
    st.info("Generating route... This might take a few seconds.")
    route_map = plot_route_on_map(parks_file, states_file, home_state, api_key)
    route_map.save("route.html")
    with open("route.html", "r", encoding="utf-8") as f:
        html = f.read()
    st.components.v1.html(html, height=700, scrolling=True)
