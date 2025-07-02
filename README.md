# Gen-V: Animation Generator 🎞️

Gen-V is an AI-powered animation generation tool that turns text prompts into dynamic animations using [Manim](https://docs.manim.community/). Built with [Streamlit](https://streamlit.io/), it provides an interactive UI to visualize ideas through generative animations powered by the [OpenAI API](https://openai.com/).

---

## 🧠 Features

- 📝 Input a custom text prompt
- 🤖 Generates animation code using OpenAI's GPT model
- 🎬 Renders animations using Manim
- 🌐 Clean and minimal Streamlit interface
- 🔗 Uses LangChain for prompt formatting and interaction logic

---

## 🛠️ Tech Stack

| Technology | Purpose                        |
|------------|--------------------------------|
| Python     | Core programming language      |
| Streamlit  | Web UI framework               |
| Manim      | Mathematical animation engine  |
| OpenAI API | Text-to-code generation        |
| LangChain  | Prompt handling and abstraction|
| dotenv     | Environment management         |

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/RamPrateek24/GenV.git
cd GenV

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
