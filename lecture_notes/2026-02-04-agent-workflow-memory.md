# Agent Workflow Memory

> **arXiv 2024** · 읽은 날짜: 2026-02-04  
> 분류: 메모리 · RAG

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2409.09163)
- [Summary Note](./2026-02-04-agent-workflow-memory.md)

---

## 한 줄 요약

성공한 multi-step workflow를 memory에 저장해 유사 task에 재사용.

## 배경 · 문제 정의

매번 zero-shot planning은 비효율적이다. Workflow memory는 subtask sequence와 tool choice를 episodic template으로 남긴다.

## 핵심 방법

- Extract workflow graph from successful trajectories
- Embed and retrieve similar past workflows for new task
- Adapt retrieved workflow via LLM edit step
- Evaluate on AppWorld, WebShop variants

## 실험 · 결과

- Success rate +10-20% on repeated task families
- Retrieval noise 시 negative transfer 관찰
- Workflow granularity ablation

## 한계 · 비판적으로 본 점

Workflow overfit to training task distribution. Versioning when tools change.

## TIL — 내가 가져간 점

sympo WBS output을 workflow memory entry로 serialize하는 아이디어.

---

*개인 공부 노트입니다.*
