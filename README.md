<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img src="assets/header-light.svg" width="100%" alt="Harshit Deswal: Applied ML, MLOps, Computer Vision">
</picture>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=harshit-05&label=profile%20views&color=58a6ff&style=flat-square" alt="profile views">
</p>

## 👨‍💻 About me

<table>
<tr>
<td width="55%" valign="top">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/terminal-dark.svg">
  <img src="assets/terminal-light.svg" width="100%" alt="whoami: Harshit Deswal, B.Tech CS and Communication Engineering, class of 2027. Now: AI/Software Engineer intern at Teemo.ai. Before: AI/ML research intern at DRDO Young Scientist Lab.">
</picture>
</td>
<td width="45%" valign="top">

- 🔭 Building **RAG_QA_System v0.3**: HTTP API, reranking and an evaluation gate
- 🎯 Heading for applied ML, coming in through MLOps
- 🛰️ At DRDO: real-time detection in PyTorch (35+ FPS on live video), NLP pipelines and a SLAM prototype
- 🐧 Daily driver: Arch Linux
- 📫 [harshitdeswal17@gmail.com](mailto:harshitdeswal17@gmail.com)

</td>
</tr>
</table>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/harshit-05/harshit-05/output/github-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/harshit-05/harshit-05/output/github-snake.svg">
    <img alt="Contribution graph snake" src="https://raw.githubusercontent.com/harshit-05/harshit-05/output/github-snake.svg">
  </picture>
</p>

## 🚀 Featured work

### 🔎 [RAG_QA_System](https://github.com/harshit-05/RAG_QA_System)

Local, config-driven Q&A over your own documents. Answers cite their sources and nothing leaves your machine.

`Python` `LangChain` `FAISS` `Ollama` `uv` `pytest` `mypy` `GitHub Actions`

```mermaid
flowchart LR
    D[PDF / DOCX / TXT / MD] --> C[Chunks<br/>1000 chars, 150 overlap]
    C --> E[MiniLM embeddings]
    E --> F[(FAISS index)]
    Q[Question] --> R[Top 5 chunks]
    F --> R
    R --> L[Local LLM via Ollama]
    L --> A[Streamed answer + sources]
```

- **Engineering:** config validated before anything loads; CI blocks on lint, types, tests (80% coverage floor) and a dependency audit
- **Honest limitation:** answers can misstate facts and faithfulness isn't measured yet (an evaluation gate is on the roadmap); on CPU, answers take minutes

### 🎯 [suspect_tracking_system](https://github.com/harshit-05/suspect_tracking_system)

Real-time person detection and tracking on CCTV footage. Click a bounding box to follow someone in a zoomed picture-in-picture view.

`Python` `PyTorch` `OpenCV` `YOLOv8` `DeepSORT`

```mermaid
flowchart LR
    V[Video frame] --> Y[YOLOv8 detector]
    Y --> P[Keep persons only]
    P --> T[DeepSORT tracker]
    T --> D[Boxes + track IDs]
    D --> S{Suspect clicked?}
    S -- yes --> Z[Highlight + zoomed PiP view]
    S -- no --> O[Output video]
    Z --> O
```

- **Engineering:** detector and tracker are separate modules, with DeepSORT and ByteTrack wrappers behind one interface
- **Honest limitation:** `main.py` can't run until a pending ByteTrack fix lands; the DeepSORT evaluation pipeline works

<!-- TODO(harshit): OrienterNet-Location-Predictor and AI-Nav-SLAM-Explorer have empty READMEs.
     Add a short description of each here if you want them featured. -->

## Recent activity

Refreshed daily by a [workflow](.github/workflows/recent-activity.yml).

<!--START_ACTIVITY-->
- [harshit-05/RAG_QA_System](https://github.com/harshit-05/RAG_QA_System): docs(stories): close s2-1 and point the board at s2-2 (2026-10-02)
<!--END_ACTIVITY-->

## 🛠️ Tech stack

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/stack-dark.svg">
    <img src="assets/stack-light.svg" width="80%" alt="Languages: Python, Java, C, SQL. ML and vision: PyTorch, OpenCV, YOLOv8. LLMs and RAG: LangChain, Ollama, Hugging Face, FAISS. Backend: FastAPI, PostgreSQL, SQLAlchemy, Pydantic. Ship and run: Docker, AWS, GitHub Actions, Arch Linux, Git, uv, pytest.">
  </picture>
</p>

## Contact

<p>
  <a href="mailto:harshitdeswal17@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>
  <a href="https://linkedin.com/in/harshit-deswal/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
</p>
