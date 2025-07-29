# Multi-Agent DDPG (MADDPG)

> **ICML 2017** · 읽은 날짜: 2026-05-09  
> 분류: MARL · 협업 RL 기초

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/1706.02275)
- [Summary Note](./2026-05-09-maddpg-note.md)

---

## 한 줄 요약

Centralized critic + decentralized actor for continuous multi-agent control.

## 배경 · 문제 정의

각 agent가 partial observability만 보면 학습이 불안정하다. MADDPG는 critic에 global state를 쓴다.

## 핵심 방법

- Per-agent actor network
- Centralized critic sees all obs and actions
- Target networks and experience replay
- Cooperative communication benchmarks

## 실험 · 결과

- Cooperative navigation, predator-prey success
- Scales to moderate agent counts
- Baseline for many follow-ups

## 한계 · 비판적으로 본 점

Continuous control focus. LLM action space incompatible directly.

## TIL — 내가 가져간 점

llm-marl에서 neural policy 대신 LLM policy로 analogy만.

---

*개인 공부 노트입니다.*
