# Supervisor Pattern for Multi-Agent Systems

> **TIL / LangGraph** · 읽은 날짜: 2026-06-16  
> 분류: 멀티에이전트 프레임워크 & 오케스트레이션

### 링크
- [Original Paper / Resource](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/agent_supervisor/)
- [Summary Note](./2026-06-16-supervisor-pattern.md)

---

## 한 줄 요약

Supervisor LLM이 worker agent를 route하는 LangGraph canonical pattern.

## 배경 · 문제 정의

Handoff는 1:1이고 supervisor는 N worker 중 선택이다. LangGraph tutorial이 de facto standard.

## 핵심 방법

- Supervisor node with worker name enum output
- Workers return to supervisor until FINISH
- State carries conversation and artifacts
- Optional human interrupt on supervisor decision

## 실험 · 결과

- Research + coding worker combo popular
- Supervisor wrong route ~8% on small eval
- Less message noise than group chat

## 한계 · 비판적으로 본 점

Supervisor context grows with worker outputs.

## TIL — 내가 가져간 점

langgraph·hierarchical-agents 실습 필수.

---

*개인 공부 노트입니다.*
