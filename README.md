# PaperMind — Multi-Agent Academic Paper Analysis System

A multi-agent system built with GLM API that automates academic paper reading and analysis. Three specialized agents collaborate to process papers in under 5 minutes.

## 🧠 System Architecture

```
Input Paper
    │
    ├──► [Summary Agent]   → Extracts core contributions
    ├──► [Critic Agent]    → Identifies limitations & weaknesses  
    └──► [Relation Agent]  → Finds connections to existing literature
              │
              ▼
       [Integration Layer]
              │
              ▼
      Structured Report
```

## ✨ Features

- **Multi-agent collaboration**: 3 specialized agents + 1 integration layer
- **Long-chain reasoning**: Each agent uses role-specific prompts for deep analysis
- **Automatic relation discovery**: Finds research connections across papers
- **Structured output**: Clean, actionable reading reports
- **Fast**: Processes a full paper in ~5 minutes vs 40 minutes manually
- **No VPN required**: Powered by Zhipu AI GLM, accessible from mainland China

## 🚀 Quick Start

### 1. Get your API Key

Go to [open.bigmodel.cn](https://open.bigmodel.cn) → Sign up → API Keys → Create API Key

### 2. Set environment variable and run

```bash
set ZHIPU_API_KEY=your_api_key_here
python paper_agent.py
```

## 📋 Usage

```python
from paper_agent import analyze_paper

paper_text = """
Title: Your Paper Title
Abstract: ...
Key Results: ...
"""

existing_papers = """
Paper 1: "Related Work" (Author, Year)
- Brief description
"""

results = analyze_paper(paper_text, existing_papers)
print(results["final_report"])
```

## 🔍 Agent Details

| Agent | Role | Output |
|-------|------|--------|
| Summary Agent | Extracts core contributions | Research problem, innovations, results |
| Critic Agent | Simulates peer review | Experimental flaws, limitations, open questions |
| Relation Agent | Semantic comparison | Citation relationships, research lineage |
| Integration Layer | Synthesizes all outputs | Structured final report |

## 📊 Performance

- Papers processed: 200+
- Average processing time: ~5 min/paper (vs 40 min manual)
- Domains covered: Machine Learning, Systems Architecture, NLP
- Daily token consumption: ~800K tokens

## 🛠 Tech Stack

- **LLM**: Zhipu AI GLM-4-Flash
- **Language**: Python 3.8+
- **Library**: `requests` (built-in, no extra install needed)

## 📁 Project Structure

```
PaperMind/
├── paper_agent.py      # Main system
└── README.md           # This file
```

## 🔮 Future Work

- Add vector database for semantic search across paper library
- Support PDF direct input
- Web UI for easier interaction
- Export reports to Notion/Obsidian
