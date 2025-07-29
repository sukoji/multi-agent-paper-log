# AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents

> **arXiv 2024** · 읽은 날짜: 2026-03-13  
> 분류: 안전 · 정렬

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2410.18404)
- [Summary Note](./2026-03-13-agentharm.md)

---

## 한 줄 요약

Agent가 tool로 실제 harm 행동을 할 수 있는지 red-team benchmark.

## 배경 · 문제 정의

Chat safety benchmark는 tool-enabled harm을 다루지 않는다. AgentHarm은 malicious goal under tool access를 측정한다.

## 핵심 방법

- Harmful task templates across categories
- Sandboxed but realistic tool environments
- Measure completion rate of harmful intent
- Refusal vs compliance classification

## 실험 · 결과

- Many aligned models still partially comply with tools
- Multi-step harm harder to block mid-trajectory
- Open benchmark for safety research

## 한계 · 비판적으로 본 점

Sandbox may not reflect real API damage. Ethical use restrictions.

## TIL — 내가 가져간 점

eval harness에 harm suite opt-in—failure-modes에 safety code 추가.

---

*개인 공부 노트입니다.*
