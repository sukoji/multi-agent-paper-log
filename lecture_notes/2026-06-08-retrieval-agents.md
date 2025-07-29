# Advanced Retrieval Patterns for Agents

> **TIL** · 읽은 날짜: 2026-06-08  
> 분류: 메모리 · RAG

### 링크
- [Summary Note](./2026-06-08-retrieval-agents.md)

---

## 한 줄 요약

Hybrid search, HyDE, parent-child chunking을 agent loop에 적용.

## 배경 · 문제 정의

Naive top-k RAG는 agent multi-step에 부족하다. Query transformation과 hierarchical index가 필요.

## 핵심 방법

- HyDE: hypothetical doc embed for query
- Parent-child: retrieve small, expand context
- BM25 + dense hybrid with RRF
- Per-step re-retrieve vs cache

## 실험 · 결과

- Hybrid +12% recall on internal doc QA
- Re-retrieve each step costly but helps planning
- HyDE hurts on factual numeric queries

## 한계 · 비판적으로 본 점

Tuning heavy. Agent-specific retrieval eval rare.

## TIL — 내가 가져간 점

rag-agents·self-rag 실무 레이어.

---

*개인 공부 노트입니다.*
