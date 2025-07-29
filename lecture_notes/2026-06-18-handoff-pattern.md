# Handoff Pattern Between Agents

> **TIL / OpenAI Swarm** · 읽은 날짜: 2026-06-18  
> 분류: 멀티에이전트 프레임워크 & 오케스트레이션

### 링크
- [Original Paper / Resource](https://github.com/openai/swarm)
- [Summary Note](./2026-06-18-handoff-pattern.md)

---

## 한 줄 요약

Agent가 function return으로 다음 담당 agent를 지정하는 control transfer.

## 배경 · 문제 정의

Explicit handoff는 customer support tier escalation과 같다. State는 shared thread에 유지.

## 핵심 방법

- transfer_to_sales_agent() style tool returns
- Receiving agent gets full prior messages
- Guardrails per agent role
- Max handoffs limit infinite bounce

## 실험 · 결과

- Triage → specialist flows clean
- tau-bench CS scenarios에 자연스러움
- Bounce between agents without progress 가능

## 한계 · 비판적으로 본 점

Handoff reason often opaque. Debugging needs trace.

## TIL — 내가 가져간 점

agents-sdk·tau-bench prod CS 아키텍처.

---

*개인 공부 노트입니다.*
