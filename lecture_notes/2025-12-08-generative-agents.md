# Generative Agents: Interactive Simulacra of Human Behavior

> **UIST 2023** · 읽은 날짜: 2025-12-08  
> 분류: 메모리 · RAG

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2304.03442)
- [Summary Note](./2025-12-08-generative-agents.md)

---

## 한 줄 요약

기억·반성·계획을 갖춘 25명의 Sims 마을 agent가 emergent social behavior를 보임.

## 배경 · 문제 정의

LLM NPC는 단기 대화엔 그럴듯하지만 장기 일관성이 없다. Stanford 팀은 memory stream + reflection + planning으로 하루 단위 생활 패턴을 시뮬레이션한다.

## 핵심 방법

- Observation을 embedding해 memory stream에 저장
- Recency·importance·relevance로 retrieval
- Reflection으로 고수준 insight 생성
- Plan을 시간 단위로 분해해 action 선택

## 실험 · 결과

- Valentine's Day party 등 emergent 이벤트 관찰
- ablation에서 memory·reflection 각각이 believability에 기여
- Smallville 인터랙티브 데모 공개

## 한계 · 비판적으로 본 점

시뮬레이션 비용이 크고 eval이 주관적이다. Real-world tool agent로 직접 이식은 어렵다.

## TIL — 내가 가져간 점

generative-agents-memory 노트와 연결—retrieval scoring을 harness fixture로 재현할 가치가 있다.

---

*개인 공부 노트입니다.*
