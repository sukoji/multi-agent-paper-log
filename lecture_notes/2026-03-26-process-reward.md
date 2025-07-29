# Process Reward Models for Agent Trajectories

> **TIL** · 읽은 날짜: 2026-03-26  
> 분류: 벤치마크 · 평가 · 관측

### 링크
- [Summary Note](./2026-03-26-process-reward.md)

---

## 한 줄 요약

Agent step마다 PRM score를 매겨 search·rerank에 쓰는 설계 노트.

## 배경 · 문제 정의

verifiers 논문을 coding/web agent에 옮기면 step boundary 정의가 관건이다.

## 핵심 방법

- Segment trajectory by tool call boundary
- LLM judge + human spot-check for step labels
- Aggregate PRM score: min, mean, last
- Integrate with best-of-3 rerank at harness

## 실험 · 결과

- Web task rerank +12% success on small set
- Judge variance high on ambiguous steps
- Min-aggregate catches early fatal errors

## 한계 · 비판적으로 본 점

Label pipeline expensive. Judge drift over time.

## TIL — 내가 가져간 점

eval-harness-ablation에서 PRM on/off 비교 예정.

---

*개인 공부 노트입니다.*
