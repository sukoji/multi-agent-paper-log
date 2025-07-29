# Claude + MCP Integration Patterns

> **TIL / Anthropic** · 읽은 날짜: 2026-05-26  
> 분류: 프로토콜 · SDK · 패턴

### 링크
- [Original Paper / Resource](https://modelcontextprotocol.io/docs)
- [Summary Note](./2026-05-26-claude-mcp.md)

---

## 한 줄 요약

Claude Desktop/Cursor에서 MCP server 연결 실습 노트.

## 배경 · 문제 정의

MCP spec 읽기와 실제 server 띄우기는 다르다. stdio transport와 config JSON이 삽질 포인트다.

## 핵심 방법

- mcp-server-git, filesystem, brave-search 테스트
- claude_desktop_config.json wiring
- Tool permission and sandbox boundaries
- Debug: MCP logging and timeout handling

## 실험 · 결과

- 3 servers 동시 연결 성공
- Large tool schema context bloat 관찰
- sympo에 github MCP 연동 아이디어

## 한계 · 비판적으로 본 점

Desktop only patterns. CI headless MCP immature.

## TIL — 내가 가져간 점

mcp 노트의 hands-on companion.

---

*개인 공부 노트입니다.*
