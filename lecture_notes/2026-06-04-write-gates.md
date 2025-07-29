# Write Gates for Agent Tool Safety

> **TIL / production pattern** · 읽은 날짜: 2026-06-04  
> 분류: 안전 · 정렬

### 링크
- [Summary Note](./2026-06-04-write-gates.md)

---

## 한 줄 요약

Destructive tool call 전에 approval token 또는 policy check를 강제.

## 배경 · 문제 정의

misevolution에서 write gate 없을 때 misuse 증가를 봤다. Read-only default, write는 explicit gate.

## 핵심 방법

- Classify tools: read, write, network, exec
- Write gate: human OK or policy engine + risk score
- Audit log immutable append
- Rollback hook for file writes

## 실험 · 결과

- Simulated prod: critical incidents -60%
- Friction: +1 click per write op
- False block rate 5% on benign edits

## 한계 · 비판적으로 본 점

UX friction. Policy engine false sense of security.

## TIL — 내가 가져간 점

guardrails-agents·failure-modes와 prod safety stack.

---

*개인 공부 노트입니다.*
