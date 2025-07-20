# LangGraph: Stateful Multi-Actor Applications with LLMs

> **framework docs** · 읽은 날짜: 2025-12-19  
> 분류: 멀티에이전트 프레임워크 & 오케스트레이션

### 링크
- [Original Paper / Resource](https://langchain-ai.github.io/langgraph/)
- [Summary Note](./2025-12-19-langgraph.md)

---

## 한 줄 요약

graph/state machine으로 agent workflow 표현.

## 문제 정의

stateless chain은 분기·재시도·human gate 표현이 어려움.

## 방법 · 핵심 아이디어

nodes=actors, edges=transitions, checkpointing, cyclic graph.

## 실험 · 결과

production agent에서 supervisor/handoff 패턴 표준화.

## TIL — 내가 가져간 점

내 eval harness를 graph로 모델링하면 attribution이 쉬움.

---

*개인 공부 노트입니다. [Deep-Learning-Paper-Review-and-Practice](https://github.com/SukoJim/Deep-Learning-Paper-Review-and-Practice) 형식을 참고했습니다.*
