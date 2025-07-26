# Reflexion: Language Agents with Verbal Reinforcement Learning

> **NeurIPS 2023** · 읽은 날짜: 2025-11-28  
> 분류: 기초 · 추론 & 액션 루프

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2303.11366)
- [Summary Note](./2025-11-28-reflexion.md)

---

## 한 줄 요약

실패 trajectory를 언어로 reflect해서 episodic memory에 넣고 재시도.

## 문제 정의

RL weight update 없이 trial-and-error로 agent를 개선하고 싶음.

## 방법 · 핵심 아이디어

evaluator signal → verbal self-reflection → memory buffer → 다음 episode에 주입.

## 실험 · 결과

AlfWorld, HotPotQA, HumanEval에서 pass@1 개선; weight update 없음.

## TIL — 내가 가져간 점

multi-agent에서도 '짧은 회고 메시지'를 shared memory에 남기는 패턴으로 확장 가능.

---

*개인 공부 노트입니다.*
