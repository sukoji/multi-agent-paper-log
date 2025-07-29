# LangGraph: Stateful Multi-Actor Applications with LLMs

> **LangChain Docs / 2024** · 읽은 날짜: 2025-12-19  
> 분류: 멀티에이전트 프레임워크 & 오케스트레이션

### 링크
- [Original Paper / Resource](https://langchain-ai.github.io/langgraph/)
- [Summary Note](./2025-12-19-langgraph.md)

---

## 한 줄 요약

Graph state machine으로 cyclic multi-agent workflow와 human checkpoint를 표현.

## 배경 · 문제 정의

DAG-only chain은 agent 루프·분기·재시도를 표현하기 어렵다. LangGraph는 Pregel-style superstep으로 stateful agent app을 만든다.

## 핵심 방법

- StateGraph에 node(agent function)와 edge(condition) 정의
- Reducer로 state field merge policy 지정
- Checkpoint persistence로 장기 실행·human-in-the-loop
- Subgraph로 hierarchical workflow encapsulation

## 실험 · 결과

- customer support, research loop 등 production 패턴 문서화
- LangSmith와 trace 연동
- supervisor·handoff 패턴 공식 예제

## 한계 · 비판적으로 본 점

Graph 복잡도가 올라가면 디버깅이 어렵고 LangChain 생태계 lock-in. 표준 graph interchange 없음.

## TIL — 내가 가져간 점

supervisor-pattern·handoff-pattern TIL을 LangGraph 예제와 1:1 매핑해 둠.

---

*개인 공부 노트입니다.*
