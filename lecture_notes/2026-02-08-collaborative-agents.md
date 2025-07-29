# Building Cooperative Embodied Agents Modularly with Large Language Models

> **ICLR 2024** · 읽은 날짜: 2026-02-08  
> 분류: MARL · 협업 RL 기초

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2307.02485)
- [Summary Note](./2026-02-08-collaborative-agents.md)

---

## 한 줄 요약

Communicative embodied agent가 modular skill로 협력해 multi-agent housework 수행.

## 배경 · 문제 정의

Embodied multi-agent는 coordination protocol 설계가 어렵다. LLM이 자연어로 negotiation하고 low-level skill을 호출한다.

## 핵심 방법

- Per-agent LLM planner + shared environment state
- Modular skill library (pick, place, navigate)
- Communication channel for task delegation
- ThreeDWorld multi-agent domestic tasks

## 실험 · 결과

- Cooperation tasks success above independent agents
- Communication ablation hurts complex tasks
- Modular skills reduce planning hallucination

## 한계 · 비판적으로 본 점

Simulated physics only. LLM comm latency limits real-time robotics.

## TIL — 내가 가져간 점

llm-marl·commnet 계열—embodied eval은 harness 비용이 커서 샘플링 전략 필요.

---

*개인 공부 노트입니다.*
