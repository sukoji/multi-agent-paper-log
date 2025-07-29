# HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face

> **NeurIPS 2023** · 읽은 날짜: 2025-12-15  
> 분류: 도구 사용 · API · 코드 실행

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2303.17580)
- [Summary Note](./2025-12-15-hugginggpt.md)

---

## 한 줄 요약

LLM이 controller로 HuggingFace 모델들을 task graph로 호출하는 tool orchestration.

## 배경 · 문제 정의

수많은 expert 모델이 HF에 흩어져 있어 사용자가 직접 고르기 어렵다. HuggingGPT는 language를 interface로 multimodal pipeline을 자동 조립한다.

## 핵심 방법

- Task Planning: user request를 subtask DAG로 분해
- Model Selection: HF model description과 매칭
- Task Execution: 선정 모델 inference
- Response Generation: 결과 통합 답변

## 실험 · 결과

- 이미지·음성·비디오 등 multimodal instruction 처리
- 모델 선택 정확도가 end-to-end 성공에 critical
- open-world task에 zero-shot orchestration

## 한계 · 비판적으로 본 점

모델 카드 품질에 의존하고 latency가 크다. 현대 MCP tool registry와 개념은 같지만 표준이 다름.

## TIL — 내가 가져간 점

routing-agents 노트의 선행 사례—harness에 model-card retrieval 단계를 넣을지 판단 근거.

---

*개인 공부 노트입니다.*
