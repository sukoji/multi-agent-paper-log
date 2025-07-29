# OpenAI Agents SDK

> **OpenAI / 2025** · 읽은 날짜: 2026-05-24  
> 분류: 멀티에이전트 프레임워크 & 오케스트레이션

### 링크
- [Original Paper / Resource](https://openai.github.io/openai-agents-python/)
- [Summary Note](./2026-05-24-agents-sdk.md)

---

## 한 줄 요약

Handoff, guardrail, tracing을 포함한 production-oriented agent SDK.

## 배경 · 문제 정의

Swarm에서 발전—structured tracing과 builtin guardrails를 추가했다.

## 핵심 방법

- Agent with tools and handoffs list
- Runner with max turns and hooks
- Built-in tracing export
- Input/output guardrails

## 실험 · 결과

- Replacement path from Swarm
- Voice and computer use agent examples
- Tracing integrates OpenAI dashboard

## 한계 · 비판적으로 본 점

OpenAI model centric. Multi-vendor agent interop limited.

## TIL — 내가 가져간 점

openai-swarm·handoff-pattern 실무 버전.

---

*개인 공부 노트입니다.*
