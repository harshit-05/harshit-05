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

## Experience

**AI/Software Engineer Intern, Teemo.ai** (remote) <!-- TODO(harshit): resume says Feb 2026 - Aug 2026; confirm whether this is ongoing -->
- Built the backend for a multi-tenant school platform: 230+ REST endpoints across 26 FastAPI domain modules on PostgreSQL (async SQLAlchemy, 72 Alembic migrations), with JWT and Google sign-in and tenant-scoped access control.
- Implemented AI grading for photographed student work: a background job sends images to a vision LLM (provider chosen by config), and a teacher reviews the score and rubric breakdown before any grade is released.
- Put email, push notifications, background jobs and the AI provider behind swappable interfaces, so the same code runs on local mocks or real providers.
- Wrote 1,100+ pytest tests plus AWS CDK stacks (ECS Fargate, RDS, S3, CloudFront) and GitHub Actions workflows that deploy the API and web apps.

**AI/ML Research Intern, DRDO Young Scientist Laboratory (AI)**, Bangalore
- Built real-time object detection pipelines in PyTorch that ran at 35+ FPS on live video.
- Optimized NLP pipelines for domain-specific text analysis, benchmarking accuracy and latency before and after each change.
- Prototyped a real-time SLAM system on multi-sensor data and measured trajectory accuracy and end-to-end latency.

## Recent activity

Refreshed daily by a [workflow](.github/workflows/recent-activity.yml).

<!--START_ACTIVITY-->
_No recent public activity._
<!--END_ACTIVITY-->

## Stack

Python · PyTorch · OpenCV · YOLOv8 · LangChain · FAISS · Ollama · FastAPI · PostgreSQL · AWS · Docker · GitHub Actions

## Contact

- Email: [harshitdeswal17@gmail.com](mailto:harshitdeswal17@gmail.com)
- LinkedIn: [harshit-deswal](https://linkedin.com/in/harshit-deswal/)
