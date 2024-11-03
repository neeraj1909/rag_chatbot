import requests
import streamlit as st


def get_api_response(question, session_id, model):
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    data = {
        "question": question,
        "model": model
    }
    if session_id:
        data["session_id"] = session_id

    try:
        response = requests.post("http://localhost:8080/chat", headers=headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"API request failed with status code {response.status_code}: {response.text}")
            return None
    except Exception as e:
        st.error(f"An error occured: {str(e)}")
        return None
    

def upload_document(file):
    print(f"Uploading file {file.name}...")
    try:
        files = {"file": (file.name, file, file.type)}
        response = requests.post("http://localhost:8080/upload-doc", files=files)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"File upload failed with status code {response.status_code}: {response.text}")
            return None
    except Exception as e:
        st.error(f"An error occured while uploading file: {str(e)}")
        return None
    

def list_documents():
    try:
        response = requests.get("http://localhost:8080/list-docs")
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to list documents with status code {response.status_code}: {response.text}")
            return []
    except Exception as e:
        st.error(f"An error occured while listing documents: {str(e)}")
        return []
    

def delete_document(file_id):
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    data = {
        "file_id": file_id
    }

    try:
        response = requests.post("http://localhost:8080/delete-doc", headers=headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to delete document with status code {response.status_code}: {response.text}")
            return None
    except Exception as e:
        st.error(f"An error occured while deleting document: {str(e)}")
        return None
