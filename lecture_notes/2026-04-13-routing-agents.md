# Routing Agents: Dynamic Model and Tool Selection

> **TIL** · 읽은 날짜: 2026-04-13  
> 분류: 멀티에이전트 프레임워크 & 오케스트레이션

### 링크
- [Summary Note](./2026-04-13-routing-agents.md)

---

## 한 줄 요약

Query별로 model size·tool subset·agent topology를 router가 고르는 설계.

## 배경 · 문제 정의

항상 GPT-4+full tools는 비용 폭탄이다. Router는 difficulty classifier처럼 동작한다.

## 핵심 방법

- Lightweight classifier or small LLM router
- Routes: {model_id, tool_list, agent_template}
- Fallback escalate on low confidence score
- Log routing decision for offline eval

## 실험 · 결과

- cost-latency 노트: 40% cost cut, 5% success drop
- Escalation rate 15% on hard bench
- Misroute on ambiguous queries

## 한계 · 비판적으로 본 점

Router training data sparse. Feedback loop slow.

## TIL — 내가 가져간 점

hugginggpt·parallel-agents와 cost 최적화 축.

---

*개인 공부 노트입니다.*
