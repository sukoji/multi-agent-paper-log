# Improving Factuality and Reasoning in Language Models through Multiagent Debate

> **ICML 2024** · 읽은 날짜: 2025-12-21  
> 분류: 기초 · 추론 & 액션 루프

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2305.14325)
- [Summary Note](./2025-12-21-multi-agent-debate.md)

---

## 한 줄 요약

여러 LLM이 토론하며 서로의 오류를 수정해 factuality와 reasoning을 높임.

## 배경 · 문제 정의

단일 model self-consistency는 같은 bias를 공유한다. Independent agent가 서로 critique하면 arithmetic·biography 오류가 줄어든다.

## 핵심 방법

- 동일 질문에 여러 agent가 초안 답 생성
- 라운드마다 다른 agent 답을 읽고 수정안 제시
- 합의 또는 majority vote로 최종 답
- GSM8K, biographies, chess 등에 적용

## 실험 · 결과

- GSM8K accuracy 유의미 향상 (모델·라운드 수에 따라)
- factual biography 질문에서 hallucination 감소
- debate round 2-3이 cost 대비 효율적

## 한계 · 비판적으로 본 점

모든 agent가 틀리면 echo chamber가 강화될 수 있다. Latency와 비용이 라운드에 선형 증가.

## TIL — 내가 가져간 점

sympo PRD→WBS debate의 이론적 근거. harness에 debate round·consensus metric 필수.

---

*개인 공부 노트입니다.*
