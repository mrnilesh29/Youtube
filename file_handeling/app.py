import streamlit as st
from pathlib import Path
import os

# ---------- Page Setup ----------
st.set_page_config(page_title="File Manager", page_icon="📁", layout="centered")

# ---------- Glass Effect Styling ----------
st.markdown("""
<style>
[data-testid="stHeader"] {
    background: transparent !important;
}

.stApp {
    background: linear-gradient(160deg, #000000 0%, #041c2c 35%, #0a3d5c 65%, #062233 100%);
    background-attachment: fixed;
}

[data-testid="stSidebar"] {
    background: rgba(5, 15, 25, 0.75);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-right: 1px solid rgba(212, 175, 55, 0.35);
}

[data-testid="stSidebar"] * {
    color: #f0c419 !important;
}

.block-container {
    padding-top: 2rem;
}

.glass-card {
    background: rgba(10, 25, 40, 0.55);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border-radius: 20px;
    border: 1px solid rgba(212, 175, 55, 0.4);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
    padding: 25px 30px;
    margin-bottom: 20px;
    color: #e6f1f8;
}

.glass-title {
    background: rgba(10, 25, 40, 0.55);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border-radius: 20px;
    border: 1px solid rgba(212, 175, 55, 0.5);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
    padding: 20px 30px;
    margin-bottom: 25px;
    text-align: center;
}

.glass-title h1 {
    color: #f0c419;
    margin: 0;
    font-size: 2.2rem;
    text-shadow: 0 0 20px rgba(240, 196, 25, 0.4);
}

.glass-title p {
    color: #7fc8e8;
    margin: 5px 0 0 0;
}

h1, h2, h3, h4 {
    color: #f0c419 !important;
}

p, label, .stMarkdown, .stCaption {
    color: #cfe8f5 !important;
}

.stTextInput input, .stTextArea textarea {
    background: rgba(0, 0, 0, 0.35) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(127, 200, 232, 0.4) !important;
    color: #f0c419 !important;
}

.stTextInput input::placeholder, .stTextArea textarea::placeholder {
    color: rgba(207, 232, 245, 0.5) !important;
}

.stButton button {
    background: linear-gradient(135deg, #b8860b, #f0c419) !important;
    backdrop-filter: blur(10px);
    border-radius: 12px !important;
    border: 1px solid rgba(240, 196, 25, 0.6) !important;
    color: #05141f !important;
    font-weight: 700 !important;
    padding: 8px 20px !important;
    transition: all 0.3s ease;
}

.stButton button:hover {
    background: linear-gradient(135deg, #f0c419, #ffe28a) !important;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(240, 196, 25, 0.4);
    color: #000 !important;
}

.stRadio > div {
    background: rgba(0, 0, 0, 0.3);
    border-radius: 12px;
    padding: 10px;
    border: 1px solid rgba(127, 200, 232, 0.25);
}

div[data-testid="stAlert"] {
    background: rgba(0, 0, 0, 0.4) !important;
    backdrop-filter: blur(10px);
    border-radius: 12px !important;
    color: #f0c419 !important;
    border: 1px solid rgba(212, 175, 55, 0.4) !important;
}

hr {
    border-color: rgba(212, 175, 55, 0.35) !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown("""
<div class="glass-title">
    <h1>📁 My File Manager</h1>
    <p>Create, Read, Update, and Delete files — all in one glassy place!</p>
</div>
""", unsafe_allow_html=True)


# ---------- Helper: show all items ----------
def show_all_items():
    p = Path('.')
    items = list(p.iterdir())
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    if not items:
        st.write("No files or folders here yet.")
    else:
        st.write("**Files & folders in this location:**")
        for i, v in enumerate(items):
            icon = "📂" if v.is_dir() else "📄"
            st.write(f"{i+1}. {icon} {v.name}")
    st.markdown('</div>', unsafe_allow_html=True)


# ---------- Sidebar ----------
st.sidebar.header("What do you want to do?")
choice = st.sidebar.radio(
    "Choose an operation:",
    ["📃 View all files", "➕ Create file", "👀 Read file", "✏️ Update file", "🗑️ Delete file"]
)

# ---------- 1) View all files ----------
if choice == "📃 View all files":
    show_all_items()

# ---------- 2) Create file ----------
elif choice == "➕ Create file":
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("Create a new file")
    st.markdown('</div>', unsafe_allow_html=True)

    show_all_items()

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    name = st.text_input("File name (e.g. test.txt)")
    data = st.text_area("What should this file contain?")

    if st.button("Create File"):
        if name.strip() == "":
            st.warning("Please enter a file name first!")
        else:
            p = Path(name)
            if not p.exists():
                with open(p, 'w') as fs:
                    fs.write(data)
                st.success(f"'{name}' created successfully! 🎉")
            else:
                st.error("This file already exists!")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- 3) Read file ----------
elif choice == "👀 Read file":
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("Read a file")
    st.markdown('</div>', unsafe_allow_html=True)

    show_all_items()

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    name = st.text_input("Which file do you want to read?")

    if st.button("Read File"):
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                content = fs.read()
            st.success("Here's the file content:")
            st.code(content)
        else:
            st.error("This file doesn't exist!")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- 4) Update file ----------
elif choice == "✏️ Update file":
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("Update a file")
    st.markdown('</div>', unsafe_allow_html=True)

    show_all_items()

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    name = st.text_input("Which file do you want to update?")

    action = st.radio(
        "What do you want to do with this file?",
        ["Rename it", "Overwrite its content", "Append new content"]
    )

    if action == "Rename it":
        new_name = st.text_input("New file name")
        if st.button("Rename"):
            p = Path(name)
            if p.exists():
                p.rename(Path(new_name))
                st.success(f"Renamed: '{name}' → '{new_name}' ✅")
            else:
                st.error("This file doesn't exist!")

    elif action == "Overwrite its content":
        new_data = st.text_area("Write the new content")
        if st.button("Overwrite"):
            p = Path(name)
            if p.exists():
                with open(p, 'w') as fs:
                    fs.write(new_data)
                st.success("File content updated! ✅")
            else:
                st.error("This file doesn't exist!")

    elif action == "Append new content":
        extra_data = st.text_area("What do you want to add?")
        if st.button("Append"):
            p = Path(name)
            if p.exists():
                with open(p, 'a') as fs:
                    fs.write(extra_data)
                st.success("Content appended! ✅")
            else:
                st.error("This file doesn't exist!")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- 5) Delete file ----------
elif choice == "🗑️ Delete file":
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("Delete a file")
    st.markdown('</div>', unsafe_allow_html=True)

    show_all_items()

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    name = st.text_input("Which file do you want to delete?")

    if st.button("Delete", type="primary"):
        p = Path(name)
        try:
            os.remove(p)
            st.success(f"'{name}' deleted successfully! 🗑️")
        except Exception as err:
            st.error(f"Error: {err}")
    st.markdown('</div>', unsafe_allow_html=True)