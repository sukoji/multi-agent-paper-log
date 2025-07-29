# Eval Harness Ablation Studies

> **TIL / tierforge** · 읽은 날짜: 2026-05-28  
> 분류: 벤치마크 · 평가 · 관측

### 링크
- [Summary Note](./2026-05-28-eval-harness-ablation.md)

---

## 한 줄 요약

동일 agent에 observation·judge·retry만 바꿔 성능 분해하는 실험 설계.

## 배경 · 문제 정의

벤치 숫자 하나로는 개선 원인을 모른다. Ablation은 harness component별 marginal value를 측정한다.

## 핵심 방법

- Factors: a11y tree vs screenshot, PRM on/off, debate rounds
- Latin square or one-at-a-time on 50 tasks
- Report success, cost, latency, failure code distribution
- Statistical bootstrap on pass rate

## 실험 · 결과

- Screenshot +20% success, +3x cost (web subset)
- PRM rerank +8% when base >30%
- Debate round 3 diminishing returns

## 한계 · 비판적으로 본 점

Small n, high variance. LLM API version drift.

## TIL — 내가 가져간 점

who-when-harness·process-reward 실험 프로토콜.

---

*개인 공부 노트입니다.*
