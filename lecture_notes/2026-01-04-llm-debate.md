# Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate

> **arXiv 2023** · 읽은 날짜: 2026-01-04  
> 분류: 기초 · 추론 & 액션 루프

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2305.19118)
- [Summary Note](./2026-01-04-llm-debate.md)

---

## 한 줄 요약

Debate가 mode collapse를 깨고 diverse reasoning path를 유도한다는 실증.

## 배경 · 문제 정의

CoT는 단일 reasoning chain에 갇힌다. Multi-agent debate는 서로 다른 perspective를 강제해 creative·logical task 모두에 이득을 준다.

## 핵심 방법

- Multiple debater agents with temperature diversity
- Moderator aggregates or selects best chain
- Tasks: creative writing, logic, translation quality
- Compare vs self-consistency and single CoT

## 실험 · 결과

- Creative task human eval score 향상
- Logic puzzle accuracy gain
- Diversity metric (distinct n-gram) 증가

## 한계 · 비판적으로 본 점

Moderator bias와 debater 수 scaling law 불명확. Production에서는 수렴 조건 정의 필요.

## TIL — 내가 가져간 점

consensus-agents·judge-agents 노트의 선행—moderator를 별도 eval model로 둘지 결정.

---

*개인 공부 노트입니다.*
