# AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors

> **ICLR 2024** · 읽은 날짜: 2025-12-12  
> 분류: 멀티에이전트 프레임워크 & 오케스트레이션

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2308.10848)
- [Summary Note](./2025-12-12-agentverse.md)

---

## 한 줄 요약

Expert recruitment → collaborative decision → evaluation 단계로 agent 팀을 동적 구성.

## 배경 · 문제 정의

고정된 두 agent debate는 복잡한 task에 인력 배치가 비효율적이다. AgentVerse는 task에 맞게 expert를 뽑고 역할을 재배치한다.

## 핵심 방법

- Recruiter가 task별 expert agent pool에서 선택
- Collaborative decision-making with group discussion
- Evaluator가 산출물 검수 후 필요 시 팀 재구성
- Textual RLBench, MGSM, HumanEval 등에 적용

## 실험 · 결과

- Multi-agent가 단일 agent 대비 reasoning·code task 향상
- Emergent social phenomena (conformity, sabotage) 관찰
- Horizontal·vertical 구조 비교 실험

## 한계 · 비판적으로 본 점

Recruiter 자체가 bottleneck이고 토큰 비용이 급증한다. Evaluator bias 체계가 약함.

## TIL — 내가 가져간 점

orchestrator-workers·supervisor-pattern TIL과 삼각 비교하면 routing policy 설계가 명확해진다.

---

*개인 공부 노트입니다.*
