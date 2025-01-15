# %% [markdown]
# # Exploration of NEON Spatial Data & Maps open data with JupyterGIS

# %%
from jupytergis_lab import GISDocument
from pathlib import Path

# %% [markdown]
# The data visualized is [National Ecological Observatory Network (NEON) shapefile open data](https://www.neonscience.org/data-samples/data/spatial-data-maps) converted into [GeoJSON](https://geojson.org/) for:
# * NEON scientific domains
# * Terrestrial field site boundaries
# * Terrestrial observation system sampling locations
# * Aquatic sites watersheds

# %% jupyter={"source_hidden": true} editable=true slideshow={"slide_type": ""}
data_path = Path.cwd() / "data"

doc = GISDocument(latitude="38.7946", longitude="-106.5348", zoom="2.8")
doc.add_raster_layer(
    url="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
    name="Google Satellite",
    attribution="Google",
    opacity=0.6,
)

# domains
doc.add_geojson_layer(path=str(data_path / "neon_domains_2024.json"))

# terrestrial field site boundaries
doc.add_geojson_layer(path=str(data_path / "terrestrial_sampling_boundaries.json"))

# terrestrial observation system sampling locations
# doc.add_geojson_layer(path=str(data_path / "neon_tos_plot_points_v11.json"))
# doc.add_geojson_layer(path=str(data_path / "neon_tos_plot_centroids_v11.json"))
doc.add_geojson_layer(path=str(data_path / "neon_tos_plot_polygons_v11.json"))
# doc.add_geojson_layer(path=str(data_path / "neon_tos_plot_subplots_v11.json"))

# aquatic sites watersheds
doc.add_geojson_layer(path=str(data_path / "neon_aquatic_watershed.json"))

doc

# %%
