# Orchestrator-Workers Multi-Agent Pattern

> **TIL / Anthropic patterns** · 읽은 날짜: 2026-04-10  
> 분류: 멀티에이전트 프레임워크 & 오케스트레이션

### 링크
- [Original Paper / Resource](https://docs.anthropic.com/en/docs/build-with-claude/agentic-patterns)
- [Summary Note](./2026-04-10-orchestrator-workers.md)

---

## 한 줄 요약

Lead agent가 subtask를 worker에 dispatch하고 결과를 synthesize하는 패턴.

## 배경 · 문제 정의

Flat group chat은 비효율적이다. Orchestrator-workers는 명확한 command hierarchy로 parallelism을 살린다.

## 핵심 방법

- Orchestrator maintains task ledger
- Workers stateless, specialized prompts/tools
- Map-reduce style result aggregation
- Re-plan on worker failure

## 실험 · 결과

- magentic-one·CrewAI hierarchical과 구조 유사
- Parallel worker 2-4x wall-clock cut on research tasks
- Orchestrator context bottleneck at scale

## 한계 · 비판적으로 본 점

Orchestrator hallucinate subtasks. Worker error propagation.

## TIL — 내가 가져간 점

sympo planner가 orchestrator—WBS item이 worker task.

---

*개인 공부 노트입니다.*
