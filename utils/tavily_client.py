from tavily import TavilyClient
import streamlit as st

client = TavilyClient(api_key=st.secrets["TAVILY_API_KEY"])

def search_web(query):
    try:
        response = client.search(query=query, search_depth="basic")
        return response.get("results", [])
    except Exception as e:
        return [{"content": f"Tavily Error: {str(e)}"}]
