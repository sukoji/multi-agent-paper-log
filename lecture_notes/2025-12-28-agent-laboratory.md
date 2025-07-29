# Agent Laboratory: Using LLM Agents as Research Assistants

> **arXiv 2025** · 읽은 날짜: 2025-12-28  
> 분류: 멀티에이전트 프레임워크 & 오케스트레이션

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2501.04227)
- [Summary Note](./2025-12-28-agent-laboratory.md)

---

## 한 줄 요약

PhD·Postdoc·PI role agent가 literature review부터 experiment·writeup까지 연구 파이프라인 수행.

## 배경 · 문제 정의

연구 workflow는 단계가 길고 artifact 종류가 다양하다. Agent Laboratory는 ML 연구를 end-to-end 자동화하는 multi-stage agent system이다.

## 핵심 방법

- ml-Agent, paper-Agent 등 역할별 specialization
- Literature review → plan → experiment → report chain
- Human feedback gate at critical milestones
- GPU experiment execution integration

## 실험 · 결과

- 자동 생성 논문 초안이 인간 작성 대비 reviewer score 근접 (주장)
- End-to-end 시간 단축
- 오픈소스 코드 공개

## 한계 · 비판적으로 본 점

실험 무결성·재현성 검증이 약하고 novelty claim이 과장될 수 있음. Ethics review 없음.

## TIL — 내가 가져간 점

paper-log 자체가 이 파이프라인의 축소판—eval은 artifact quality rubric이 핵심.

---

*개인 공부 노트입니다.*
