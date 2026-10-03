# Harshit Deswal

**Applied ML, with MLOps as my way in.**
I like ML systems that are tested, reproducible, and upfront about where they fall short.

Third-year B.Tech student in Computer Science & Communication Engineering (graduating 2027).
AI/Software Engineer intern at Teemo.ai. Previously AI research at DRDO's Young Scientist Lab.

## Projects

Each row ends with the limitation the project's own README admits to.

| Project | What it does | Stack | Honest limitation |
| --- | --- | --- | --- |
| [**RAG_QA_System**](https://github.com/harshit-05/RAG_QA_System) | Local, config-driven Q&A over your own documents. Answers cite their sources, and nothing leaves your machine. Config is validated at load, and CI gates on lint, types, tests (80% coverage floor) and a dependency audit. | Python, LangChain, FAISS, Ollama, uv | Answers can misstate facts and faithfulness isn't measured yet (an evaluation gate is on the roadmap). On CPU, answers take minutes. |
| [**suspect_tracking_system**](https://github.com/harshit-05/suspect_tracking_system) | Real-time person detection and tracking on CCTV footage. Click a bounding box to follow someone, with a zoomed picture-in-picture view. | Python, YOLOv8, DeepSORT | `main.py` can't run until a pending ByteTrack fix lands. The DeepSORT evaluation pipeline works. |

<!-- TODO(harshit): OrienterNet-Location-Predictor and AI-Nav-SLAM-Explorer have empty READMEs.
     Add a one-line description of each here if you want them featured. -->
