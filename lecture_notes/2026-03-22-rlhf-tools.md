# RLHF for Tool-Using Language Models

> **TIL / industry papers** · 읽은 날짜: 2026-03-22  
> 분류: 안전 · 정렬

### 링크
- [Summary Note](./2026-03-22-rlhf-tools.md)

---

## 한 줄 요약

Tool call trajectory에 human preference를 적용하는 RLHF 변형 스터디.

## 배경 · 문제 정의

Text RLHF는 tool sequence ranking을 학습하지 못한다. Preference pair는 entire trajectory 기준이어야 한다.

## 핵심 방법

- Collect pairwise trajectories on same task
- Reward model on (task, traj) correctness + safety
- PPO/DPO on policy with tool schema constraint
- KL to SFT reference prevent drift

## 실험 · 결과

- Tool success rate +5-8%p in pilot
- Reward hacking: verbose useless calls
- Preference data cost dominates

## 한계 · 비판적으로 본 점

No standard public dataset. Simulator-reality gap.

## TIL — 내가 가져간 점

agent-q DPO와 비교—offline preference from harness traces.

---

*개인 공부 노트입니다.*
