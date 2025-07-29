# smolagents: Minimal Agent Framework by Hugging Face

> **Hugging Face / 2025** · 읽은 날짜: 2026-05-02  
> 분류: 멀티에이전트 프레임워크 & 오케스트레이션

### 링크
- [Original Paper / Resource](https://github.com/huggingface/smolagents)
- [Summary Note](./2026-05-02-smolagents.md)

---

## 한 줄 요약

적은 abstraction으로 code agent와 tool agent를 빠르게 만드는 lightweight framework.

## 배경 · 문제 정의

LangChain은 무겁다. smolagents는 핵심 loop만 남기고 CodeAgent를 first-class로 둔다.

## 핵심 방법

- CodeAgent: Python actions in sandbox
- ToolAgent: function calling style
- Managed agents (sub-agent delegation)
- Hub integration for models and spaces

## 실험 · 결과

- Small codebase easy to audit
- GAIA-lite reproductions reported
- Multi-agent via managed agents pattern

## 한계 · 비판적으로 본 점

Young project—production hardening immature. Ecosystem smaller.

## TIL — 내가 가져간 점

llama-agent·local model 실험용 primary framework.

---

*개인 공부 노트입니다.*
