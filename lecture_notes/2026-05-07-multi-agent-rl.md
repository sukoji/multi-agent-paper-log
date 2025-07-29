# Multi-Agent Reinforcement Learning: Foundations and Modern Approaches

> **TIL / MARL textbook** · 읽은 날짜: 2026-05-07  
> 분류: MARL · 협업 RL 기초

### 링크
- [Summary Note](./2026-05-07-multi-agent-rl.md)

---

## 한 줄 요약

LLM agent 이전 classical MARL 개념—joint policy, CTDE, non-stationarity.

## 배경 · 문제 정의

LLM multi-agent는 RL formalism 없이 heuristic이다. MARL 기초는 credit assignment와 equilibrium 이해에 필요.

## 핵심 방법

- Independent Q-learning baseline
- Centralized training decentralized execution (CTDE)
- Cooperative vs competitive reward shaping
- Map to LLM team reward design

## 실험 · 결과

- Non-stationarity breaks naive IQL
- CTDE (QMIX 등) improves cooperative sims
- LLM agent rarely uses formal MARL training

## 한계 · 비판적으로 본 점

Sim-to-real gap. LLM discrete action space differs.

## TIL — 내가 가져간 점

maddpg-note·qmix·commnet으로 구체 알고리즘 연결.

---

*개인 공부 노트입니다.*
