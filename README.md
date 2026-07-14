This project demonstrates how to transform a research-grade medical Vision-Language Model into a production-ready AI service following modern software engineering best practices.

# Medical AI Serving Platform

Production-ready backend platform for deploying medical Vision-Language Models (VLMs) such as MedGemma using FastAPI, Docker, and GPU-aware inference.

---

## Motivation

Large Vision-Language Models have demonstrated remarkable capabilities in medical imaging. However, transforming a research model into a reliable production service requires much more than loading a model and calling `generate()`.

This project demonstrates how to engineer an industrial-grade AI inference platform for medical image understanding, focusing on software architecture, deployment, scalability, observability, and maintainability.

The repository is designed as an engineering portfolio project rather than a research prototype.

---

## Features

- FastAPI REST API
- MedGemma model serving
- Multi-modal inference (image + question + metadata)
- GPU-aware inference
- Batch inference support
- Streaming responses (planned)
- Docker & Docker Compose deployment
- Structured logging
- Health and readiness probes
- Model lifecycle management
- Configuration management using environment variables
- Unit and integration tests
- OpenAPI documentation
- Production-ready project structure

---

## Example Request

POST /v1/inference

Input

- Chest X-ray
- Clinical question
- Patient metadata

Output

```json
{
    "answer": "...",
    "confidence": 0.91,
    "latency_ms": 184,
    "model": "MedGemma"
}
```

---

## Architecture

                REST API
                   │
                   ▼
             FastAPI Backend
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
 Configuration          Model Manager
        │                     │
        └──────────┬──────────┘
                   ▼
             MedGemma Engine
                   │
                   ▼
             GPU Inference
                   │
                   ▼
             JSON Response

---

## Repository Structure

app/
api/
core/
models/
services/
storage/
monitoring/

tests/

docker/

docs/

---

## Technology Stack

Python 3.12

FastAPI

PyTorch

Transformers

MedGemma

Docker

Pydantic

Uvicorn

---

## Roadmap

- [x] Bootstrap
- [ ] Core Foundation
- [ ] REST API
- [ ] Model Manager
- [ ] MedGemma Integration
- [ ] Docker Deployment
- [ ] Redis Cache
- [ ] PostgreSQL
- [ ] Metrics & Monitoring
- [ ] CI/CD

---

## Disclaimer

This repository is intended for software engineering and research purposes only. It is not a medical device and should not be used for clinical diagnosis or treatment decisions.

## Engineering Highlights

- Production-ready REST API
- GPU-aware inference pipeline
- Clean Architecture
- Dependency Injection
- Dockerized deployment
- OpenAPI documentation
- Unit & Integration Testing
- Health & Readiness endpoints
- Model lifecycle management
- Configuration via environment variables
- Structured logging
- CI/CD pipeline