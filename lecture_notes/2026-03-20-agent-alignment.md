# Alignment for Agentic Systems

> **TIL / alignment survey** · 읽은 날짜: 2026-03-20  
> 분류: 안전 · 정렬

### 링크
- [Summary Note](./2026-03-20-agent-alignment.md)

---

## 한 줄 요약

Single-turn alignment이 multi-step agent에 왜 부족한지 정리한 노트.

## 배경 · 문제 정의

Chat alignment은 최종 답만 본다. Agent는 중간 tool call이 누적 harm을 일으킬 수 있다.

## 핵심 방법

- Decompose alignment: intent, process, outcome
- Map RLHF, CAI, overseer, sandbox on each layer
- Case study: permission escalation via file tools
- Propose process-level reward sketch

## 실험 · 결과

- Outcome-only RLHF misses 40% harmful trajectories (예시 로그)
- Overseer every-k-steps cost model
- Open research gaps listed

## 한계 · 비판적으로 본 점

Conceptual note—quantitative sweep 부족.

## TIL — 내가 가져간 점

process-reward·verifiers와 직결—harness reward를 step-wise로.

---

*개인 공부 노트입니다.*
