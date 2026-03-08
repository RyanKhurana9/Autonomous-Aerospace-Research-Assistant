# Autonomous-Aerospace-Research-Assistant
# 🚀 Aerospace AI Agent

An autonomous AI agent built with LangChain and Ollama that can search aerospace research papers, retrieve NASA data with images, and perform rocket engineering calculations — all running **completely free and locally** on your machine.

---

## Features

- 🔭 **arXiv Search** — Search the latest aerospace and rocket propulsion research papers
- 🛸 **NASA Data** — Retrieve NASA mission information and image URLs from the NASA Image API
- 🧮 **Rocket Calculator** — Calculate rocket exhaust velocity from specific impulse (Isp)
- 🧠 **Memory** — Remembers your conversation history across multiple questions
- 💻 **Fully Local** — Powered by Ollama and LLaMA 3.1, no API keys or internet needed after setup

---

## Project Structure

```
aerospace-agent/
├── tools.py          # Tool definitions (arXiv, NASA, calculator)
├── agent.py          # Agent and model setup
├── main.py           # Entry point with conversation loop
├── requirements.txt  # Python dependencies
└── .env              # Environment variables (no keys needed for Ollama)
```

---

## Prerequisites

- Python 3.10+
- [Ollama](https://ollama.com/download) installed and running

---

## Setup

**1. Clone the repository**
```bash
git clone <your-repo-url>
cd aerospace-agent
```

**2. Create and activate a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Pull the LLaMA model via Ollama**
```bash
ollama pull llama3.1:8b
```

**5. Run the agent**
```bash
python3 main.py
```

---

## Usage

Once running, you can ask the agent questions like:

```
You: What are the latest research papers on rocket propulsion?
You: Show me NASA data about the Apollo 11 mission
You: What is the exhaust velocity for an Isp of 450?
You: Tell me about SpaceX Starship research
```

Type `exit` or `quit` to stop the agent.

---

## Tools

| Tool | Description | Source |
|------|-------------|--------|
| `search_arxiv` | Search aerospace research papers | arXiv API |
| `get_nasa_data` | Get NASA mission info and image URLs | NASA Images API |
| `rocket_exhaust_velocity` | Calculate exhaust velocity from Isp | Physics formula |

---

## Tech Stack

- [LangChain](https://github.com/langchain-ai/langchain) — Agent framework
- [Ollama](https://ollama.com) — Local LLM runner
- [LLaMA 3.1 8B](https://ollama.com/library/llama3.1) — Language model by Meta
- [arXiv API](https://arxiv.org/help/api) — Research paper search
- [NASA Images API](https://images.nasa.gov/docs/images.nasa.gov_api_docs.pdf) — NASA media

---

## Why Ollama?

- ✅ Completely free — no API keys, no billing
- ✅ No rate limits ever
- ✅ Your data stays on your machine
- ✅ Works great on Apple Silicon (M1/M2/M3/M4) Macs

---

## License

MIT
