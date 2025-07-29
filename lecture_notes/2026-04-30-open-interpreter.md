# Open Interpreter: Natural Language Interface for Code Execution

> **Open Source / 2023** · 읽은 날짜: 2026-04-30  
> 분류: 도구 사용 · API · 코드 실행

### 링크
- [Original Paper / Resource](https://github.com/OpenInterpreter/open-interpreter)
- [Summary Note](./2026-04-30-open-interpreter.md)

---

## 한 줄 요약

로컬에서 자연어로 code를 실행하는 generalist computer interface.

## 배경 · 문제 정의

Code interpreter를 local env에서 돌리면 privacy·custom package가 가능하다. Open Interpreter는 CLI agent의 early popularizer.

## 핵심 방법

- LLM emits code blocks for local execution
- Supports Python, JS, shell per config
- Human approve mode for dangerous ops
- OS-level file and app control

## 실험 · 결과

- Large GitHub star community
- Local data analysis workflows
- Foundation for many fork projects

## 한계 · 비판적으로 본 점

Security entirely on user. Not multi-agent native.

## TIL — 내가 가져간 점

codeact 이전 세대—single agent baseline for harness.

---

*개인 공부 노트입니다.*
