# AgentClinic: A Multimodal Agent Benchmark for Clinical Decision Making

> **arXiv 2024** · 읽은 날짜: 2026-02-19  
> 분류: 벤치마크 · 평가 · 관측

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2405.20678)
- [Summary Note](./2026-02-19-agentclinic.md)

---

## 한 줄 요약

환자 시뮬레이터와 multimodal EHR로 clinical agent를 eval.

## 배경 · 문제 정의

Medical QA benchmark는 single-turn이다. AgentClinic은 multi-visit diagnostic agent를 safe sandbox에서 테스트한다.

## 핵심 방법

- Patient agent with hidden condition
- Clinician agent orders tests, asks questions
- Multimodal inputs: text reports, images
- Scoring: diagnosis accuracy, test cost, safety

## 실험 · 결과

- GPT-4V variants outperform text-only
- Unsafe recommendation rate measurable
- Long horizon diagnostic paths

## 한계 · 비판적으로 본 점

Simulated patients—not clinical validation. Liability concerns.

## TIL — 내가 가져간 점

safety·eval 교차—domain-specific harness template 참고.

---

*개인 공부 노트입니다.*
