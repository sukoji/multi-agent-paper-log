# Retrieval-Augmented Generation for Agents

> **TIL / Lewis et al. extension** · 읽은 날짜: 2026-04-19  
> 분류: 메모리 · RAG

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2005.11401)
- [Summary Note](./2026-04-19-rag-agents.md)

---

## 한 줄 요약

Agent가 매 step마다 external KB를 retrieve해 hallucination을 줄이는 패턴.

## 배경 · 문제 정의

Parametric memory는 stale하고 citation이 없다. RAG agent는 retrieve→reason→act loop를 반복한다.

## 핵심 방법

- Chunk docs, embed, top-k retrieval per turn
- Inject context into planner prompt
- Optional reranker cross-encoder
- Citation in final user response

## 실험 · 결과

- Domain QA accuracy +15-25%p vs no RAG
- Retrieval miss = wrong action chain
- Latency +200-500ms per step

## 한계 · 비판적으로 본 점

Chunk boundary breaks tables. Agent multi-hop retrieval underexplored.

## TIL — 내가 가져간 점

self-rag·retrieval-agents로 발전 단계 정리.

---

*개인 공부 노트입니다.*
