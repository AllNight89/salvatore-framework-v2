import streamlit as st
import asyncio
from salvatore import SAL
import json

st.title("Salvatore Juggernaut Apex - Truth-Seeking AI Beast")

st.write("Yo, enter your query to unleash SAL! E.g., 'Analyze X post' or 'Check PubMed data for lies'.")

# User input
query = st.text_input("Enter query:")
choice = st.text_input("Enter choice (optional, default 'default'):", "default")

if st.button("Run SAL"):
    # Run the framework async in Streamlit
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    sal = SAL("JuggernautApex")
    result = loop.run_until_complete(sal.run(query, choice))
    st.write("**Results (JSON Output):**")
    st.json(result)
    st.write("Output saved to ~/salvatore_export.json or /tmp/salvatore_export.json")

