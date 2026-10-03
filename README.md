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
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/training-dark.svg">
  <img src="assets/training-light.svg" width="100%" alt="Illustration: loss curves drawing over 50 epochs">
</picture>

- 🔭 Building **RAG_QA_System v0.3**: HTTP API, reranking and an evaluation gate
- 🎯 Heading for applied ML, coming in through MLOps
- 🛰️ At DRDO: real-time detection in PyTorch (35+ FPS on live video), NLP pipelines and a SLAM prototype
- 🐧 Daily driver: Arch Linux
- 📫 [harshitdeswal17@gmail.com](mailto:harshitdeswal17@gmail.com)

</td>
</tr>
</table>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/divider-dark.svg">
  <img src="assets/divider-light.svg" width="100%" alt="">
</picture>

## 🛠️ Tech stack

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/stack-dark.svg">
    <img src="assets/stack-light.svg" width="80%" alt="Languages: Python, Java, C, SQL. ML and vision: PyTorch, OpenCV, YOLOv8. LLMs and RAG: LangChain, Ollama, Hugging Face, FAISS. Backend: FastAPI, PostgreSQL, SQLAlchemy, Pydantic. Ship and run: Docker, AWS, GitHub Actions, Arch Linux, Git, uv, pytest.">
  </picture>
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/divider-dark.svg">
  <img src="assets/divider-light.svg" width="100%" alt="">
</picture>

## 🚀 Featured work

<table>
<tr>
<td width="50%" valign="top">

### 🔎 [RAG_QA_System](https://github.com/harshit-05/RAG_QA_System)

Local, config-driven Q&A over your own documents. Answers cite their sources and nothing leaves your machine.

`Python` `LangChain` `FAISS` `Ollama` `uv` `pytest` `mypy` `GitHub Actions`

- **Engineering:** config validated before anything loads; CI blocks on lint, types, tests (80% coverage floor) and a dependency audit
- **Honest limitation:** answers can misstate facts and faithfulness isn't measured yet (an evaluation gate is on the roadmap); on CPU, answers take minutes

</td>
<td width="50%" valign="middle">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/rag-dark.svg">
  <img src="assets/rag-light.svg" width="100%" alt="Illustration: question embedded, five nearest chunks retrieved from FAISS, cited answer generated">
</picture>
</td>
</tr>
<tr>
<td width="50%" valign="middle">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/tracking-dark.svg">
  <img src="assets/tracking-light.svg" width="100%" alt="Illustration: people tracked with boxes and IDs, one marked as suspect with a zoomed picture-in-picture view">
</picture>
</td>
<td width="50%" valign="top">

### 🎯 [suspect_tracking_system](https://github.com/harshit-05/suspect_tracking_system)

Real-time person detection and tracking on CCTV footage. Click a bounding box to follow someone in a zoomed picture-in-picture view.

`Python` `PyTorch` `OpenCV` `YOLOv8` `DeepSORT`

- **Engineering:** detector and tracker live in separate modules, with wrappers for both DeepSORT and ByteTrack
- **Honest limitation:** `main.py` can't run until a pending ByteTrack fix lands; the DeepSORT evaluation pipeline works

</td>
</tr>
</table>

<sub>Animations are illustrations of how each pipeline works, not recordings of real output.</sub>

<details>
<summary><b>RAG_QA_System pipeline</b></summary>

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

</details>

<details>
<summary><b>suspect_tracking_system pipeline</b></summary>

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

</details>

<!-- TODO(harshit): OrienterNet-Location-Predictor and AI-Nav-SLAM-Explorer have empty READMEs.
     Add a short description of each here if you want them featured. -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/divider-dark.svg">
  <img src="assets/divider-light.svg" width="100%" alt="">
</picture>

## 📊 GitHub stats

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=harshit-05&show_icons=true&hide_border=true&theme=github_dark">
    <img src="https://github-readme-stats.vercel.app/api?username=harshit-05&show_icons=true&hide_border=true&theme=default" height="165" alt="GitHub stats">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=harshit-05&layout=compact&hide_border=true&theme=github_dark">
    <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=harshit-05&layout=compact&hide_border=true&theme=default" height="165" alt="Top languages">
  </picture>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=harshit-05&theme=github-dark-blue&hide_border=true">
    <img src="https://streak-stats.demolab.com?user=harshit-05&theme=default&hide_border=true" alt="GitHub streak">
  </picture>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=harshit-05&theme=github-compact&hide_border=true">
    <img src="https://github-readme-activity-graph.vercel.app/graph?username=harshit-05&theme=minimal&hide_border=true" width="100%" alt="Contribution activity graph">
  </picture>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-profile-trophy.vercel.app/?username=harshit-05&theme=darkhub&no-frame=true&no-bg=true&margin-w=6">
    <img src="https://github-profile-trophy.vercel.app/?username=harshit-05&theme=flat&no-frame=true&no-bg=true&margin-w=6" alt="GitHub trophies">
  </picture>
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/divider-dark.svg">
  <img src="assets/divider-light.svg" width="100%" alt="">
</picture>

## 🐍 Contribution snake

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/harshit-05/harshit-05/output/github-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/harshit-05/harshit-05/output/github-snake.svg">
    <img alt="Contribution graph snake" src="https://raw.githubusercontent.com/harshit-05/harshit-05/output/github-snake.svg">
  </picture>
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/divider-dark.svg">
  <img src="assets/divider-light.svg" width="100%" alt="">
</picture>

## ⚡ Recent activity

Refreshed daily by a [workflow](.github/workflows/recent-activity.yml).

<!--START_ACTIVITY-->
- [harshit-05/RAG_QA_System](https://github.com/harshit-05/RAG_QA_System): docs(stories): close s2-1 and point the board at s2-2 (2026-10-02)
<!--END_ACTIVITY-->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/divider-dark.svg">
  <img src="assets/divider-light.svg" width="100%" alt="">
</picture>

## 🤝 Connect

<p align="center">
  <a href="mailto:harshitdeswal17@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
  <a href="https://linkedin.com/in/harshit-deswal/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://github.com/harshit-05?tab=repositories"><img src="https://img.shields.io/badge/Repositories-181717?style=for-the-badge&logo=github&logoColor=white" alt="Repositories"></a>
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/footer-dark.svg">
  <img src="assets/footer-light.svg" width="100%" alt="">
</picture>
