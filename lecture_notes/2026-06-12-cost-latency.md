# Cost and Latency Tradeoffs in Multi-Agent Systems

> **TIL** · 읽은 날짜: 2026-06-12  
> 분류: 벤치마크 · 평가 · 관측

### 링크
- [Summary Note](./2026-06-12-cost-latency.md)

---

## 한 줄 요약

Agent 수·model tier·debate round별 $/task와 p95 latency 측정.

## 배경 · 문제 정의

Multi-agent success rate만 보면 bankruptcy다. Production은 Pareto frontier가 필요하다.

## 핵심 방법

- Sweep: {1,3,5} agents × {small, large} model
- Metrics: USD per success, p50/p95 latency
- Plot Pareto frontier (awesome-agents plot)
- Early exit on consensus

## 실험 · 결과

- 5-agent debate 4x cost, +10% success on logic set
- Router (routing-agents) shifts frontier outward
- p95 dominated by slowest worker

## 한계 · 비판적으로 본 점

API price changes. Success definition varies.

## TIL — 내가 가져간 점

awesome-agents pareto plot 데이터 소스.

---

*개인 공부 노트입니다.*
