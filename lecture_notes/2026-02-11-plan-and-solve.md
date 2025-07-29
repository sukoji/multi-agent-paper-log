# Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning

> **ACL 2023** · 읽은 날짜: 2026-02-11  
> 분류: 기초 · 추론 & 액션 루프

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2305.04091)
- [Summary Note](./2026-02-11-plan-and-solve.md)

---

## 한 줄 요약

먼저 plan을 세우고 실행하는 two-phase prompting으로 CoT 오류 감소.

## 배경 · 문제 정의

Zero-shot CoT는 중간 계산 실수가 많다. Plan-and-Solve는 explicit plan phase로 reasoning path를 안정화한다.

## 핵심 방법

- Prompt: devise plan then carry out step by step
- Zero-shot without exemplars
- Compare PS+ vs standard CoT on math word problems
- Error analysis on missing step types

## 실험 · 결과

- GSM8K zero-shot accuracy 개선
- Plan quality correlates with final answer
- Simple prompt change, no fine-tuning

## 한계 · 비판적으로 본 점

Plan 자체가 틀리면 recovery 없음. Multi-agent plan merge는 다루지 않음.

## TIL — 내가 가져간 점

tree-of-thoughts·sympo planner 단계의 가벼운 대안.

---

*개인 공부 노트입니다.*
