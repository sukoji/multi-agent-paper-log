# Constitutional AI Applied to Tool-Using Agents

> **TIL / Anthropic CAI** · 읽은 날짜: 2026-03-18  
> 분류: 안전 · 정렬

### 링크
- [Original Paper / Resource](https://www.anthropic.com/research/constitutional-ai)
- [Summary Note](./2026-03-18-constitutional-ai-agents.md)

---

## 한 줄 요약

Principle-based critique-revision loop를 agent tool 선택에 적용.

## 배경 · 문제 정의

RLHF만으로는 rare tool misuse를 막기 어렵다. CAI는 model이 principle list로 self-critique한다.

## 핵심 방법

- Define constitution: harmlessness, honesty, privacy
- Generate critique on proposed tool call
- Revise action before execution
- Compare vs single-shot refusal prompt

## 실험 · 결과

- Harmful tool proposal rate 감소 (내부 재현)
- Over-refusal on benign dev tasks 증가 trade-off
- Multi-step에서 principle conflict 발생

## 한계 · 비판적으로 본 점

Constitution drafting subjective. No public agent-specific benchmark.

## TIL — 내가 가져간 점

agent-alignment·judge-agents—critic을 별도 agent로 분리할지.

---

*개인 공부 노트입니다.*
