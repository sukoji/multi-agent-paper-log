# Let's Verify Step by Step

> **OpenAI / arXiv 2023** · 읽은 날짜: 2026-03-24  
> 분류: 벤치마크 · 평가 · 관측

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2305.20050)
- [Summary Note](./2026-03-24-verifiers.md)

---

## 한 줄 요약

Process verifier가 math reasoning 중간 step을 판별해 성능 향상.

## 배경 · 문제 정의

Outcome reward는 lucky guess를 강화한다. Step verifier는 각 reasoning step correctness를 분리 평가한다.

## 핵심 방법

- Train PRM on step-level labels
- Best-of-N sampling with PRM scoring
- Active learning for label efficiency
- Apply to MATH dataset

## 실험 · 결과

- MATH performance large jump with PRM reranking
- Process supervision > outcome supervision
- Label cost still high

## 한계 · 비판적으로 본 점

Math-specific. Agent tool step verification needs new PRM.

## TIL — 내가 가져간 점

process-reward·judge-agents 이론적 기반.

---

*개인 공부 노트입니다.*
