# Tree of Thoughts: Deliberate Problem Solving with Large Language Models

> **NeurIPS 2023** · 읽은 날짜: 2026-02-13  
> 분류: 기초 · 추론 & 액션 루프

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2305.10601)
- [Summary Note](./2026-02-13-tree-of-thoughts.md)

---

## 한 줄 요약

LLM이 thought tree를 BFS/DFS로 탐색하며 deliberate search 수행.

## 배경 · 문제 정의

Linear CoT는 local mistake에 취약하다. ToT는 여러 reasoning branch를 평가하고 backtrack한다.

## 핵심 방법

- Thought decomposition per problem type
- Generator proposes multiple next thoughts
- Evaluator scores states (LLM or heuristic)
- Search: BFS/DFS with pruning

## 실험 · 결과

- Game of 24: 74% success vs CoT 4%
- Creative writing coherence improved
- Compute scales with branch factor

## 한계 · 비판적으로 본 점

Evaluator reliability caps performance. Expensive for long horizons.

## TIL — 내가 가져간 점

agent-q MCTS와 사고 방식 유사—harness에서 search budget을 공통 hyperparam으로.

---

*개인 공부 노트입니다.*
