# Reflexion: Language Agents with Verbal Reinforcement Learning

> **NeurIPS 2023** · 읽은 날짜: 2025-11-28  
> 분류: 자기진화 · 워크플로 메모리

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2303.11366)
- [Summary Note](./2025-11-28-reflexion.md)

---

## 한 줄 요약

실패 trajectory를 언어로 reflect해 다음 trial의 system memory에 넣는 verbal RL.

## 배경 · 문제 정의

Weight update 없이 trial 간 학습하려면 scalar reward만으로는 signal이 부족하다. Reflexion은 agent가 스스로 critique를 쓰고 episodic memory에 저장해 self-evolution의 초기 형태를 제시한다.

## 핵심 방법

- Actor가 task 수행 후 Evaluator가 success/fail 판정
- 실패 시 Self-Reflection 모듈이 구체적 개선 문장 생성
- Reflection을 sliding window memory에 append 후 재시도
- AlfWorld, HotPotQA, HumanEval, WebShop에 적용

## 실험 · 결과

- AlfWorld에서 success 91%까지 상승 (baseline 대비 +22%p)
- HumanEval pass@1 91% (GPT-4 기반 설정)
- weight fine-tuning 없이 multi-trial gain 입증

## 한계 · 비판적으로 본 점

Reflection 품질이 모델에 의존하고 memory가 길어지면 이전 교훈이 희석된다. Multi-agent에서는 누가 reflect할지 역할 분리가 필요.

## TIL — 내가 가져간 점

eval harness에 trial loop + reflection slot을 넣으면 벤치 한 번 돌릴 때 self-evolving axis를 같이 측정할 수 있다.

---

*개인 공부 노트입니다.*
