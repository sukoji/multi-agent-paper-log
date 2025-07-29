# LLM-as-Judge for Multi-Agent Outputs

> **TIL** · 읽은 날짜: 2026-06-22  
> 분류: 벤치마크 · 평가 · 관측

### 링크
- [Summary Note](./2026-06-22-judge-agents.md)

---

## 한 줄 요약

별도 judge agent가 worker 산출물을 rubric으로 채점.

## 배경 · 문제 정의

Human eval은 느리다. Judge agent는 position bias와 leniency 문제가 있다.

## 핵심 방법

- Rubric dimensions: correctness, completeness, safety
- Swap position debiasing for pairwise
- Judge model ≠ worker model
- Calibrate against human gold on 50 samples

## 실험 · 결과

- Pearson 0.72 vs human on code review task
- Self-judge inflates scores +15%
- Multi-dimensional beats single score

## 한계 · 비판적으로 본 점

Judge drift on new domains. Adversarial worker can game.

## TIL — 내가 가져간 점

consensus-agents·process-reward—harness judge slot.

---

*개인 공부 노트입니다.*
