# Generative Agents Memory Architecture Deep Dive

> **TIL / UIST 2023 follow-up** · 읽은 날짜: 2026-01-28  
> 분류: 메모리 · RAG

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2304.03442)
- [Summary Note](./2026-01-28-generative-agents-memory.md)

---

## 한 줄 요약

Memory stream scoring과 reflection 주기를 agent harness에 재현한 학습 노트.

## 배경 · 문제 정의

원 논문은 게임 시뮬에 집중돼 있어 RAG agent로 옮기려면 retrieval formula를 분해해야 한다. importance score가 핵심 lever다.

## 핵심 방법

- Recency exponential decay on memory embeddings
- LLM-prompted importance 1-10 scoring per observation
- Relevance via query-memory cosine similarity
- Periodic reflection batches (every k actions)

## 실험 · 결과

- Smallville replay에서 top-k retrieval ablation
- Reflection off 시 장기 goal drift 관찰
- Scoring weights 민감도 실험 (개인 재현)

## 한계 · 비판적으로 본 점

Embedding model 교체 시 behavior 변동 큼. Production scale DB엔 비용 문제.

## TIL — 내가 가져간 점

retrieval-agents TIL과 짝—harness fixture로 memory scoring plug-in 만들 예정.

---

*개인 공부 노트입니다.*
