# WorkArena: How Capable Are Web Agents at Solving Common Knowledge Work Tasks?

> **ICML 2024** · 읽은 날짜: 2026-03-09  
> 분류: 웹 · GUI · computer-use 에이전트

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2404.05971)
- [Summary Note](./2026-03-09-workarena.md)

---

## 한 줄 요약

ServiceNow 기반 enterprise knowledge work task benchmark.

## 배경 · 문제 정의

Consumer web benchmark는 office workflow를 반영 못 한다. WorkArena는 form·ticket·dashboard 업무를 simulates.

## 핵심 방법

- ServiceNow sandbox environments
- L2–L3 difficulty task taxonomy
- Compound tasks spanning multiple pages
- Programmatic success verification

## 실험 · 결과

- SOTA agents low success on L3 compound
- Form filling errors cascade
- Enterprise UI complexity bottleneck

## 한계 · 비판적으로 본 점

ServiceNow specific. License needed for full repro.

## TIL — 내가 가져간 점

webarena consumer vs workarena enterprise—prod eval은 후자에 가깝다.

---

*개인 공부 노트입니다.*
