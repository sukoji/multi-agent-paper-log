# Adaptive Agents: Learning to Adapt in Dynamic Environments

> **TIL / ICLR 2024 workshop** · 읽은 날짜: 2026-02-17  
> 분류: 자기진화 · 워크플로 메모리

### 링크
- [Summary Note](./2026-02-17-adaptive-agent.md)

---

## 한 줄 요약

환경 변화 시 prompt·tool subset을 online adapt하는 agent 설계 스터디.

## 배경 · 문제 정의

Static agent config는 API deprecation·UI redesign에 취약하다. Adaptive layer가 drift signal을 감지해 policy를 조정한다.

## 핵심 방법

- Monitor success rate sliding window per tool
- Trigger adaptation when metric drops below threshold
- LLM rewrites tool selection policy from failure traces
- A/B holdout for rollback

## 실험 · 결과

- Simulated UI drift에서 recovery 2x faster than static
- False positive adaptation causes instability
- Tool subset pruning reduces cost 30%

## 한계 · 비판적으로 본 점

내부 시뮬 결과—real prod drift 데이터 부족.

## TIL — 내가 가져간 점

tierforge production failure codes와 연동해 adaptation trigger 설계.

---

*개인 공부 노트입니다.*
