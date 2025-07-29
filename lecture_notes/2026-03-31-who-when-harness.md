# Who & When: Detecting Which Agent Fails and When

> **TIL / MAS debugging** · 읽은 날짜: 2026-03-31  
> 분류: 벤치마크 · 평가 · 관측

### 링크
- [Summary Note](./2026-03-31-who-when-harness.md)

---

## 한 줄 요약

Multi-agent run에서 fault attribution을 자동화하는 harness 설계.

## 배경 · 문제 정의

팀 실패 시 single scalar score로는 누가 망쳤는지 모른다. Who&When은 step-level blame assignment를 목표로 한다.

## 핵심 방법

- Counterfactual replay: swap one agent output
- Shapley-inspired credit on success delta
- Timestamp alignment across agent message bus
- Output: blame vector + failure step index

## 실험 · 결과

- sympo debate에서 critic vs planner blame 분리 성공
- Counterfactual cost 3x base run
- Human agree rate 78% on sample

## 한계 · 비판적으로 본 점

Non-deterministic LLM noise. Shapley exact compute expensive.

## TIL — 내가 가져간 점

failure-modes·langsmith-traces와 삼위일체 debugging stack.

---

*개인 공부 노트입니다.*
