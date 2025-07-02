import streamlit as st
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os, subprocess
import re

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

st.title("Prompt-to-Manim Video Generator")

prompt = st.text_input("Describe the animation:")
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


    import re
    match = re.search(r"class\s+(\w+)\(Scene\):", code)
    scene_name = match.group(1) if match else "UnknownScene"

    subprocess.run(["manim", "-pql", "manim_scene.py", scene_name])

    st.video(f"media/videos/manim_scene/480p15/{scene_name}.mp4")
