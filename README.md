<h1 align="center">Harshit Deswal</h1>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&duration=3000&pause=1000&color=2F81F7&center=true&vCenter=true&width=520&lines=Applied+ML+%C2%B7+MLOps+as+my+way+in;RAG+pipelines+%C2%B7+computer+vision;Tested%2C+reproducible%2C+honest+about+limits" alt="Applied ML, RAG pipelines, computer vision" />
</p>

<p align="center">
  Third-year B.Tech student in Computer Science &amp; Communication Engineering (graduating 2027).<br>
  AI/Software Engineer intern at Teemo.ai. Previously AI research at DRDO's Young Scientist Lab.
</p>

## Featured work

### [RAG_QA_System](https://github.com/harshit-05/RAG_QA_System)

Local, config-driven Q&A over your own documents. Answers cite their sources and nothing leaves your machine.
CI blocks on lint, types, tests (80% coverage floor) and a dependency audit.

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

**Focus:** RAG · config validation · CI gates · reproducible setup with uv
**Honest limitation:** answers can misstate facts and faithfulness isn't measured yet (an evaluation gate is on the roadmap). On CPU, answers take minutes.

### [suspect_tracking_system](https://github.com/harshit-05/suspect_tracking_system)

Real-time person detection and tracking on CCTV footage. Click a bounding box to follow someone, with a zoomed picture-in-picture view.

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

**Focus:** object detection · multi-object tracking · interactive OpenCV UI
**Honest limitation:** `main.py` can't run until a pending ByteTrack fix lands. The DeepSORT evaluation pipeline works.

<!-- TODO(harshit): OrienterNet-Location-Predictor and AI-Nav-SLAM-Explorer have empty READMEs.
     Add a short description of each here if you want them featured. -->

## Recent activity

Refreshed daily by a [workflow](.github/workflows/recent-activity.yml).

<!--START_ACTIVITY-->
- [harshit-05/RAG_QA_System](https://github.com/harshit-05/RAG_QA_System): docs(stories): close s2-1 and point the board at s2-2 (2026-10-02)
<!--END_ACTIVITY-->

## Stack

Python · PyTorch · OpenCV · YOLOv8 · LangChain · FAISS · Ollama · FastAPI · PostgreSQL · AWS · Docker · GitHub Actions

## Contact

- Email: [harshitdeswal17@gmail.com](mailto:harshitdeswal17@gmail.com)
- LinkedIn: [harshit-deswal](https://linkedin.com/in/harshit-deswal/)
