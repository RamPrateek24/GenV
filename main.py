import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os, subprocess, re

st.set_page_config(page_title="GenV", layout="wide")

st.title("Welcome to GenV")

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(model="gpt-4o-mini")

st.title("Gen-V: Generative Visuals")

prompt = st.text_input("Give your thoughts:")
if st.button("Generate Animation") and prompt:
    instruction = (
        "Write only the Python code using Manim. "
        "Do not include any explanations or comments. "
        "Only include a single Scene class. "
        "Start directly with the import and class definition."
    )

    response = model.invoke(f"{instruction}\n{prompt}")
    matches = re.findall(r"```(?:python)?\n(.*?)```", response.content, re.DOTALL)
    code = matches[0] if matches else response.content

    with open("manim_scene.py", "w") as f:
        f.write(code)

    match = re.search(r"class\s+(\w+)\(Scene\):", code)
    scene_name = match.group(1) if match else "UnknownScene"

    output_dir = "media/videos/manim_scene/480p15"
    os.makedirs(output_dir, exist_ok=True)

    try:
        subprocess.run(["manim", "-ql", "manim_scene.py", scene_name], check=True)
    except subprocess.CalledProcessError as e:
        st.error("Manim rendering failed.")
        st.code(e.stderr or str(e), language="bash")
    else:
        video_path = f"{output_dir}/{scene_name}.mp4"
        if os.path.exists(video_path):
            st.video(video_path)
        else:
            st.error(f"⚠️ Video not found at: {video_path}")
