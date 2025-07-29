# Agent Protocol: Open Standard for Agent Communication

> **TIL / community specs** · 읽은 날짜: 2026-05-18  
> 분류: 프로토콜 · SDK · 패턴

### 링크
- [Summary Note](./2026-05-18-agent-protocol.md)

---

## 한 줄 요약

HTTP/WebSocket 기반 agent message envelope 초안 비교 노트.

## 배경 · 문제 정의

MCP, A2A, FIPA ACL legacy가 혼재한다. 통합 envelope가 없으면 harness interoperability가 어렵다.

## 핵심 방법

- Compare MCP tools vs A2A tasks vs custom JSON-RPC
- Propose minimal envelope: {from, to, intent, payload, trace_id}
- Auth: OAuth vs API key per hop
- Versioning strategy sketch

## 실험 · 결과

- MCP wins tool layer; A2A wins agent delegation
- trace_id 필수 합의
- No single winner—layered stack likely

## 한계 · 비판적으로 본 점

Spec churn. Political adoption barriers.

## TIL — 내가 가져간 점

mcp·a2a 노트 상위 레이어.

---

*개인 공부 노트입니다.*
