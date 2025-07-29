# AgentStudio: A Toolkit for Building General Virtual Agents

> **arXiv 2024** · 읽은 날짜: 2026-03-03  
> 분류: 멀티에이전트 프레임워크 & 오케스트레이션

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2406.08629)
- [Summary Note](./2026-03-03-agentstudio.md)

---

## 한 줄 요약

Virtual environment·task·agent·benchmark를 모듈로 제공하는 general agent toolkit.

## 배경 · 문제 정의

Agent 연구 재현이 env setup에서 막힌다. AgentStudio는 standardized modules로 ablation을 쉽게 한다.

## 핵심 방법

- Modular env: web, desktop, daily tasks
- Agent lib: planning, memory, tool interfaces
- Benchmark suite with automatic grading
- Visualization and trajectory replay

## 실험 · 결과

- Multiple env unified API
- Ablation studies reproducible
- Open-source release

## 한계 · 비판적으로 본 점

Env fidelity vs WebArena gap. Community smaller than OpenHands.

## TIL — 내가 가져간 점

agentbench·tierforge env adapter 후보.

---

*개인 공부 노트입니다.*
