# Improving Factuality and Reasoning in Language Models through Multiagent Debate

> **ICML 2024** · 읽은 날짜: 2025-12-21  
> 분류: 멀티에이전트 프레임워크 & 오케스트레이션

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2305.14325)
- [Summary Note](./2025-12-21-multi-agent-debate.md)

---

## 한 줄 요약

여러 LM instance가 debate하며 factuality 개선.

## 문제 정의

single-shot CoT는 hallucination.

## 방법 · 핵심 아이디어

동일 prompt 여러 agent → round-robin critique → final answer.

## 실험 · 결과

arithmetics, biography, GSM 등에서 accuracy 상승.

## TIL — 내가 가져간 점

sympo의 PRD debate와 직접 연결; judge agent 비용 tradeoff 존재.

---

*개인 공부 노트입니다. [Deep-Learning-Paper-Review-and-Practice](https://github.com/SukoJim/Deep-Learning-Paper-Review-and-Practice) 형식을 참고했습니다.*
