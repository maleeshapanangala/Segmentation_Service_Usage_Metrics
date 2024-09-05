import streamlit as st
import pandas as pd

# Set the title of the dashboard
st.title("BU Portal - Segmentation Service User Adoption Dashboard")

# --------------- Live Segments Section ---------------------
st.subheader("Live Segments")
live_segments_data = {
    "Segment": ["Prepaid", "Postpaid"],
    "Mobile XX": ["xx", "xx"],
    "HBB XX": ["xx", "xx"],
    "DTV XX": ["xx", "xx"]
}

live_segments_df = pd.DataFrame(live_segments_data)
st.table(live_segments_df)

# --------------- User Metrics Section -----------------------
st.subheader("User Metrics")
st.text("XX Unique users logged within the past XX days")
st.text("XX Total logins within the past XX days")

user_metrics_data = {
    "User": ["User 1", "User 2"], # Placeholder user data
    "Number of Logins": ["xx", "xx"],
    "Segment Creation": ["xx", "xx"],
    "Segment Termination": ["xx", "xx"],
    "Filtration Logic Changes": ["xx", "xx"],
    "Attribute Changes": ["xx", "xx"]
}

user_metrics_df = pd.DataFrame(user_metrics_data)
st.table(user_metrics_df)

# --------------- Segment Definition Changes Section ---------------------
st.subheader("Segment Definition Changes")
segment_definition_data = {
    "Tribe_Subtribe": ["DP_NWFDATA", "PD_UPSELL", "PD_CHURN"],
    "New Segment Creation": ["xx", "xx", ""],
    "Priority Change": ["xx", "xx", ""],
    "Filtration Logic change": ["xx", "xx", ""]
}

segment_definition_df = pd.DataFrame(segment_definition_data)
st.table(segment_definition_df)

# --------------- Segment Attribute Changes Section ---------------------
st.subheader("Segment Attribute Changes")

# Dynamic Pricing
st.write("Tribe - Dynamic Pricing")
dynamic_pricing_data = {
    "Attribute": ["MIN_ARPU_STRETCH", "MAX_ARPU_STRETCH", "OFFER_AGGRESSION"],
    "Value": ["XX", "XX", "XX"]
}
dynamic_pricing_df = pd.DataFrame(dynamic_pricing_data)
st.table(dynamic_pricing_df)

# Pack Discounting
st.write("Pack Discounting")
pack_discounting_data = {
    "Attribute": ["MIN_DISCOUNTING", "MAX_DISCOUNTING"],
    "Value": ["XX", "XX"]
}
pack_discounting_df = pd.DataFrame(pack_discounting_data)
st.table(pack_discounting_df)

# New Tribe
st.write("Tribe - <New Tribe>")
new_tribe_data = {
    "Attribute": ["Attribute 1", "Attribute 2"],
    "Value": ["XX", "XX"]
}
new_tribe_df = pd.DataFrame(new_tribe_data)
st.table(new_tribe_df)

# --------------- Detailed View Section ---------------------
st.subheader("Detailed View")
detailed_view_data = {
    "Date": ["2024-09-01", "2024-09-02"], # Placeholder dates
    "User": ["User 1", "User 2"], 
    "BU": ["BU1", "BU2"], # Placeholder BU
    "Payment Type": ["Prepaid", "Postpaid"],
    "Change Type": ["Definition", "Attribute"],
    "Segment ID": ["XX", "XX"],
    "Change/Attribute": ["XX", "XX"],
    "Previous Value": ["XX", "XX"],
    "New Value": ["XX", "XX"]
}

detailed_view_df = pd.DataFrame(detailed_view_data)
st.table(detailed_view_df)

# --------------- Footer or Additional Information ---------------
st.text("Dashboard generated using Streamlit. Data sourced from Snowflake.")
