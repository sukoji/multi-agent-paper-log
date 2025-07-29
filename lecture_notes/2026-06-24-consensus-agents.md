# Consensus Mechanisms in Multi-Agent Systems

> **TIL** · 읽은 날짜: 2026-06-24  
> 분류: 기초 · 추론 & 액션 루프

### 링크
- [Summary Note](./2026-06-24-consensus-agents.md)

---

## 한 줄 요약

Vote, debate converge, judge pick 중 task별 consensus 전략 선택.

## 배경 · 문제 정의

multi-agent-debate 후 합의 방법이 결과를 좌우한다. Early stop 조건도 중요.

## 핵심 방법

- Majority vote on final answer
- Embedding similarity threshold for agreement
- Max rounds + stagnation detection
- Weighted vote by past agent accuracy

## 실험 · 결과

- Stagnation stop saves 30% tokens
- Weighted vote helps heterogeneous agents
- Wrong unanimous consensus still happens

## 한계 · 비판적으로 본 점

No optimal universal rule. Task-specific tuning.

## TIL — 내가 가져간 점

sympo reviewer 단계 consensus rule 설계.

---

*개인 공부 노트입니다.*
