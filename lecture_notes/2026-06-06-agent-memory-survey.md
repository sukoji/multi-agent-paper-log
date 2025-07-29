# Survey on Memory for LLM Agents

> **TIL / arXiv surveys** · 읽은 날짜: 2026-06-06  
> 분류: 메모리 · RAG

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2404.13534)
- [Summary Note](./2026-06-06-agent-memory-survey.md)

---

## 한 줄 요약

Short/long-term, episodic/semantic memory 모듈을 agent 관점에서 분류.

## 배경 · 문제 정의

RAG만으로는 agent memory를 설명 못 한다. Survey는 write·update·forget lifecycle을 강조한다.

## 핵심 방법

- Memory types: buffer, vector, graph, sql
- Operations: store, retrieve, update, forget
- Shared memory in multi-agent teams
- Benchmark: long dialog, persona, tool logs

## 실험 · 결과

- No single best memory architecture
- Graph memory emerging for relations
- Forgetting underexplored vs growth

## 한계 · 비판적으로 본 점

Rapid new systems. Eval fragmentation.

## TIL — 내가 가져간 점

memgpt·generative-agents-memory·retrieval-agents 인덱스.

---

*개인 공부 노트입니다.*
