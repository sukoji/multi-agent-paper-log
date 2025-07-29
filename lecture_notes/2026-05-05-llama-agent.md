# Building Agents with Llama Models

> **TIL / Meta Llama** · 읽은 날짜: 2026-05-05  
> 분류: 멀티에이전트 프레임워크 & 오케스트레이션

### 링크
- [Original Paper / Resource](https://www.llama.com/docs/)
- [Summary Note](./2026-05-05-llama-agent.md)

---

## 한 줄 요약

Llama 3.x를 backbone으로 tool call·multi-turn agent 구성한 실험.

## 배경 · 문제 정의

API cost를 줄이려면 local Llama가 필요하다. Function calling format과 prompt template이 model별로 다르다.

## 핵심 방법

- Llama 3.1 8B/70B instruct with JSON tool schema
- Quantized inference via Ollama/vLLM
- smolagents CodeAgent wrapper
- Benchmark subset: GSM8K tool, simple web

## 실험 · 결과

- 70B approaches GPT-3.5 tool use; 8B frequent schema errors
- Latency acceptable on single GPU for 8B
- Quantization hurts multi-step consistency

## 한계 · 비판적으로 본 점

Frontier gap remains on WebArena. Hardware barrier.

## TIL — 내가 가져간 점

cost-latency·map-neo와 local stack 비교.

---

*개인 공부 노트입니다.*
