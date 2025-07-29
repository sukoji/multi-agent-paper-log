# OpenAI Swarm: Educational Multi-Agent Orchestration

> **OpenAI / 2024** · 읽은 날짜: 2026-05-22  
> 분류: 멀티에이전트 프레임워크 & 오케스트레이션

### 링크
- [Original Paper / Resource](https://github.com/openai/swarm)
- [Summary Note](./2026-05-22-openai-swarm.md)

---

## 한 줄 요약

Lightweight handoff-based multi-agent—Agents SDK 전신.

## 배경 · 문제 정의

Production orchestration 전에 minimal pattern 교육용 framework가 필요했다. Swarm은 function return으로 agent transfer.

## 핵심 방법

- Agent = instructions + functions + handoffs
- Client.run loop until no handoff
- Context variables passed across agents
- No built-in memory or persistence

## 실험 · 결과

- Clean handoff pattern reference
- Superseded by Agents SDK directionally
- Community examples for triage flows

## 한계 · 비판적으로 본 점

Experimental—not production maintained. Feature minimal.

## TIL — 내가 가져간 점

handoff-pattern·agents-sdk 학습 순서 1단계.

---

*개인 공부 노트입니다.*
