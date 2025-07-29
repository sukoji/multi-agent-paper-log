# AgentBench: Evaluating LLMs as Agents

> **ICLR 2024** · 읽은 날짜: 2026-01-11  
> 분류: 벤치마크 · 평가 · 관측

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2308.03688)
- [Summary Note](./2026-01-11-agentbench.md)

---

## 한 줄 요약

8종 환경(OS, DB, KG, web 등)에서 LLM agent 능력을 multi-dimensional으로 측정.

## 배경 · 문제 정의

MMLU는 agent skill을 반영하지 못한다. AgentBench는 diverse interactive environment로 planning·tool use·self-correction을 격리 측정한다.

## 핵심 방법

- 8 environments: OS, DB, KG, digital card game, lateral thinking, house-holding, web shopping, web browsing
- Unified HTTP evaluation server
- Success rate + partial progress metrics
- 20+ LLM cross-eval

## 실험 · 결과

- GPT-4가 aggregate에서 선두지만 환경별 격차 큼
- 오픈모델은 OS·DB에서 특히 약함
- Environment difficulty hierarchy 제시

## 한계 · 비판적으로 본 점

Simulated env와 real prod gap. Maintenance burden으로 일부 env outdated.

## TIL — 내가 가져간 점

agent-eval-survey·tierforge 벤치 선택의 1차 필터로 사용.

---

*개인 공부 노트입니다.*
