# Parallel Agent Execution Patterns

> **TIL** · 읽은 날짜: 2026-06-14  
> 분류: 멀티에이전트 프레임워크 & 오케스트레이션

### 링크
- [Summary Note](./2026-06-14-parallel-agents.md)

---

## 한 줄 요약

Independent subtask를 worker에 parallel dispatch 후 merge.

## 배경 · 문제 정의

Sequential agent chain은 wall-clock이 길다. Parallelism은 conflict resolution이 핵심이다.

## 핵심 방법

- Orchestrator partitions DAG with parallelizable layers
- asyncio gather on worker LLM calls
- Merge: vote, LLM synthesize, or structured reduce
- Detect duplicate conflicting writes

## 실험 · 결과

- Research subqueries 2.5x speedup
- Merge conflicts 10% on overlapping facts
- Token use increases vs sequential

## 한계 · 비판적으로 본 점

Not all tasks parallelizable. Merge quality variable.

## TIL — 내가 가져간 점

orchestrator-workers·supervisor-pattern 성능 최적화.

---

*개인 공부 노트입니다.*
