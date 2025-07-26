### 꼼꼼한 멀티에이전트 논문 TIL · Multi-Agent Paper Log

- **멀티에이전트 LLM** (orchestration, tools, memory, eval) 공부하면서 읽은 논문·프레임워크·벤치마크 정리 저장소입니다.
- 형식 참고: [SukoJim/Deep-Learning-Paper-Review-and-Practice](https://github.com/SukoJim/Deep-Learning-Paper-Review-and-Practice) — Original Paper / Reading Note 구조.
- 2025년 말부터 하루에 한 편(가끔 TIL 메모) 페이스로 기록 중입니다.
- 질문·오타는 **Issues**에 남겨주세요.

| 폴더 | 설명 |
|------|------|
| [`lecture_notes/`](lecture_notes/) | 논문 리뷰 · TIL 마크다운 |
| [`code_practices/`](code_practices/) | (선택) reproduce 스크립트 · 실험 노트 |

#### 기초 · 추론 & 액션 루프

* **ReAct: Synergizing Reasoning and Acting in Language Models** (ICLR 2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2210.03629) / [Reading Note](lecture_notes/2025-11-26-react.md)

* **Reflexion: Language Agents with Verbal Reinforcement Learning** (NeurIPS 2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2303.11366) / [Reading Note](lecture_notes/2025-11-28-reflexion.md)

* **Self-Consistency Improves Chain of Thought Reasoning in Language Models** (ICLR 2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2203.11171) / [Reading Note](lecture_notes/2025-12-23-mad.md)

* **Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents** (2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2408.07199) / [Reading Note](lecture_notes/2026-01-06-agent-q.md)

* **Plan-and-Solve Prompting** (ACL 2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2309.06179) / [Reading Note](lecture_notes/2026-02-11-plan-and-solve.md)

* **Tree of Thoughts: Deliberate Problem Solving with Large Language Models** (NeurIPS 2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2305.10601) / [Reading Note](lecture_notes/2026-02-13-tree-of-thoughts.md)

* **Language Agent Tree Search (LATS)** (2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2310.04406) / [Reading Note](lecture_notes/2026-02-15-lass.md)

* **ADAPT: As-Needed Decomposition and Planning with Language Models** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=ADAPT:+As-Needed+Decomposition+and+Planning+with+Language+Models) / [Reading Note](lecture_notes/2026-02-17-adaptive-agent.md)

* **OpenAgents: An Open Platform for Language Agents** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=OpenAgents:+An+Open+Platform+for+Language+Agents) / [Reading Note](lecture_notes/2026-02-28-openagents.md)

* **Hierarchical multi-agent control** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Hierarchical+multi-agent+control) / [Reading Note](lecture_notes/2026-04-15-hierarchical-agents.md)

* **FreshLLMs: Refreshing LLMs with search-augmented agents** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=FreshLLMs:+Refreshing+LLMs+with+search-augmented+agents) / [Reading Note](lecture_notes/2026-04-23-freshllms.md)

* **Search-in-the-loop agents (Perplexity-style architectures)** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Search-in-the-loop+agents+(Perplexity-style+architectures)) / [Reading Note](lecture_notes/2026-04-25-search-agents.md)


#### 멀티에이전트 프레임워크 & 오케스트레이션

* **CAMEL: Communicative Agents for Mind Exploration of Large Language Model Society** (NeurIPS 2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2303.17760) / [Reading Note](lecture_notes/2025-12-02-camel.md)

* **MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework** (ICLR 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2308.00352) / [Reading Note](lecture_notes/2025-12-04-metagpt.md)

* **AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation** (COLM 2024 / framework)
  * [Original Paper / Resource](https://arxiv.org/abs/2308.08155) / [Reading Note](lecture_notes/2025-12-06-autogen.md)

* **AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors** (ICLR 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2308.10848) / [Reading Note](lecture_notes/2025-12-12-agentverse.md)

* **HuggingGPT: Solving AI Tasks with ChatGPT and Its Friends in Hugging Face** (2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2303.17580) / [Reading Note](lecture_notes/2025-12-15-hugginggpt.md)

* **LangGraph: Stateful Multi-Actor Applications with LLMs** (framework docs)
  * [Original Paper / Resource](https://langchain-ai.github.io/langgraph/) / [Reading Note](lecture_notes/2025-12-19-langgraph.md)

* **Improving Factuality and Reasoning in Language Models through Multiagent Debate** (ICML 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2305.14325) / [Reading Note](lecture_notes/2025-12-21-multi-agent-debate.md)

* **Magentic-One: A Generalist Multi-Agent System for Solving Complex Tasks** (2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2411.04468) / [Reading Note](lecture_notes/2025-12-30-magentic-one.md)

* **Encouraging Divergent Thinking in LLMs through Multi-Agent Debate** (2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2305.19118) / [Reading Note](lecture_notes/2026-01-04-llm-debate.md)

* **Multi-Agent Collaboration via Evolving Orchestration** (2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2409.07497) / [Reading Note](lecture_notes/2026-01-08-map-neo.md)


#### 생성형 · embodied 에이전트

* **Generative Agents: Interactive Simulacra of Human Behavior** (UIST 2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2304.03442) / [Reading Note](lecture_notes/2025-12-08-generative-agents.md)

* **Voyager: An Open-Ended Embodied Agent with Large Language Models** (TMLR 2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2305.16291) / [Reading Note](lecture_notes/2025-12-10-voyager.md)


#### 웹 · GUI · computer-use 에이전트

* **WebArena: A Realistic Web Environment for Building Autonomous Agents** (ICLR 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2307.13854) / [Reading Note](lecture_notes/2026-01-13-webarena.md)

* **Mind2Web: Towards a Generalist Agent for the Web** (NeurIPS 2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2306.06070) / [Reading Note](lecture_notes/2026-01-15-mind2web.md)

* **Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Mobile-Agent:+Autonomous+Multi-Modal+Mobile+Device+Agent) / [Reading Note](lecture_notes/2026-02-22-mobile-agent.md)

* **Cradle: Generalist Computer Control Agent** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Cradle:+Generalist+Computer+Control+Agent) / [Reading Note](lecture_notes/2026-02-24-cradle.md)

* **AppAgent: Multimodal Agents as Smartphone Users** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=AppAgent:+Multimodal+Agents+as+Smartphone+Users) / [Reading Note](lecture_notes/2026-02-26-appagent.md)

* **Agent-E: Hierarchical planning for web agents** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Agent-E:+Hierarchical+planning+for+web+agents) / [Reading Note](lecture_notes/2026-03-05-agent-e.md)

* **SeeAct: GPT-4V for Web Grounding** (2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2401.01614) / [Reading Note](lecture_notes/2026-03-07-seeact.md)

* **WorkArena: How Capable Are Web Agents at Solving Work Tasks?** (2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2403.07718) / [Reading Note](lecture_notes/2026-03-09-workarena.md)

* **VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks** (ICLR 2025)
  * [Original Paper / Resource](https://arxiv.org/abs/2404.05967) / [Reading Note](lecture_notes/2026-03-11-visualwebarena.md)


#### 도구 사용 · API · 코드 실행

* **Toolformer: Language Models Can Teach Themselves to Use Tools** (NeurIPS 2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2302.04761) / [Reading Note](lecture_notes/2025-11-30-toolformer.md)

* **SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering** (NeurIPS 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2405.15793) / [Reading Note](lecture_notes/2025-12-17-swe-agent.md)

* **OpenHands: An Open Platform for AI Software Developers** (2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2407.16741) / [Reading Note](lecture_notes/2025-12-26-openhands.md)

* **Gorilla: Large Language Model Connected with Massive APIs** (NeurIPS 2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2305.15334) / [Reading Note](lecture_notes/2026-01-19-gorilla.md)

* **ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs** (2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2307.16789) / [Reading Note](lecture_notes/2026-01-22-toolllm.md)

* **AnyTool: Self-Reflective Tool Use for Agents** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=AnyTool:+Self-Reflective+Tool+Use+for+Agents) / [Reading Note](lecture_notes/2026-01-24-anytool.md)

* **AutoAct: Automatic Agent Learning from Tool Use** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=AutoAct:+Automatic+Agent+Learning+from+Tool+Use) / [Reading Note](lecture_notes/2026-02-06-autoact.md)

* **AgentStudio: A Toolkit for Building General Virtual Agents** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=AgentStudio:+A+Toolkit+for+Building+General+Virtual+Agents) / [Reading Note](lecture_notes/2026-03-03-agentstudio.md)

* **Executable Code Actions Elicit Better LLM Agents** (ICML 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2402.01030) / [Reading Note](lecture_notes/2026-04-28-codeact.md)


#### 메모리 · RAG

* **MemGPT: Towards LLMs as Operating Systems** (2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2310.08560) / [Reading Note](lecture_notes/2026-01-26-memgpt.md)

* **Memory stream + retrieval in generative agents (follow-up)** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Memory+stream+++retrieval+in+generative+agents+(follow-up)) / [Reading Note](lecture_notes/2026-01-28-generative-agents-memory.md)

* **Corrective RAG / agentic RAG for tool loops** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Corrective+RAG+/+agentic+RAG+for+tool+loops) / [Reading Note](lecture_notes/2026-04-19-rag-agents.md)

* **Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection** (ICLR 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2310.11511) / [Reading Note](lecture_notes/2026-04-21-self-rag.md)

* **Memory for LLM-based agents (survey)** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Memory+for+LLM-based+agents+(survey)) / [Reading Note](lecture_notes/2026-06-06-agent-memory-survey.md)

* **Retrieval-augmented generation in agent loops** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Retrieval-augmented+generation+in+agent+loops) / [Reading Note](lecture_notes/2026-06-08-retrieval-agents.md)


#### 벤치마크 · 평가 · 관측

* **AgentBench: Evaluating LLMs as Agents** (ICLR 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2308.03688) / [Reading Note](lecture_notes/2026-01-11-agentbench.md)

* **τ-bench: A Benchmark for Tool-Agent-User Interaction** (2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2406.12027) / [Reading Note](lecture_notes/2026-01-17-tau-bench.md)

* **Multi-Agent Collaboration: Harnessing Inter-Agent Debate** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Multi-Agent+Collaboration:+Harnessing+Inter-Agent+Debate) / [Reading Note](lecture_notes/2026-02-08-collaborative-agents.md)

* **AgentClinic: Multimodal agent benchmark** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=AgentClinic:+Multimodal+agent+benchmark) / [Reading Note](lecture_notes/2026-02-19-agentclinic.md)

* **Training Verifiers to Solve Math Word Problems (process supervision)** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Training+Verifiers+to+Solve+Math+Word+Problems+(process+supervision)) / [Reading Note](lecture_notes/2026-03-24-verifiers.md)

* **Let's Verify Step by Step** (ICLR 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2305.20050) / [Reading Note](lecture_notes/2026-03-26-process-reward.md)

* **Evaluation of LLM-based Agents (survey sections)** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Evaluation+of+LLM-based+Agents+(survey+sections)) / [Reading Note](lecture_notes/2026-03-28-agent-eval-survey.md)

* **Which Agent Causes Task Failures — and When?** (2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2409.13474) / [Reading Note](lecture_notes/2026-03-31-who-when-harness.md)


#### 안전 · 정렬

* **AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents** (2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2409.03766) / [Reading Note](lecture_notes/2026-03-13-agentharm.md)

* **Constitutional AI applied to agent loops** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Constitutional+AI+applied+to+agent+loops) / [Reading Note](lecture_notes/2026-03-18-constitutional-ai-agents.md)

* **Aligning LLM Agents via Reinforcement Learning from Human Feedback** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Aligning+LLM+Agents+via+Reinforcement+Learning+from+Human+Feedback) / [Reading Note](lecture_notes/2026-03-20-agent-alignment.md)

* **Tool-augmented RLHF for agents** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Tool-augmented+RLHF+for+agents) / [Reading Note](lecture_notes/2026-03-22-rlhf-tools.md)


#### 자기진화 · 워크플로 메모리

* **The Agent Laboratory: Advancing Autonomous Research** (2025)
  * [Original Paper / Resource](https://arxiv.org/abs/2501.04227) / [Reading Note](lecture_notes/2025-12-28-agent-laboratory.md)

* **A Survey on Self-Evolving Agents** (2025 survey)
  * [Original Paper / Resource](https://arxiv.org/abs/2501.07452) / [Reading Note](lecture_notes/2026-01-30-self-evolving-agents.md)

* **Misevolution: Model Evolution Inspired by Natural Selection** (2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2409.07428) / [Reading Note](lecture_notes/2026-02-02-misevolution.md)

* **Agent Workflow Memory** (2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2408.07122) / [Reading Note](lecture_notes/2026-02-04-agent-workflow-memory.md)


#### MARL · 협업 RL 기초

* **Multi-Agent Reinforcement Learning basics for LLM teams** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Multi-Agent+Reinforcement+Learning+basics+for+LLM+teams) / [Reading Note](lecture_notes/2026-05-07-multi-agent-rl.md)

* **MADDPG intuition for cooperative agents** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=MADDPG+intuition+for+cooperative+agents) / [Reading Note](lecture_notes/2026-05-09-maddpg-note.md)

* **Communication networks in multi-agent RL** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Communication+networks+in+multi-agent+RL) / [Reading Note](lecture_notes/2026-05-11-commnet.md)

* **QMIX monotonic value factorization (reference)** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=QMIX+monotonic+value+factorization+(reference)) / [Reading Note](lecture_notes/2026-05-13-qmix.md)

* **LLM-based MARL hybrids (2024 papers skim)** (see paper)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=LLM-based+MARL+hybrids+(2024+papers+skim)) / [Reading Note](lecture_notes/2026-05-15-llm-marl.md)


#### 프로토콜 · SDK · 패턴

* **Model Context Protocol (MCP)** (Anthropic spec)
  * [Original Paper / Resource](https://modelcontextprotocol.io/) / [Reading Note](lecture_notes/2026-04-06-mcp.md)


#### TIL · 프로젝트 메모

* **CrewAI — role-based agent crews** (framework docs)
  * [Original Paper / Resource](https://docs.crewai.com/) / [Reading Note](lecture_notes/2026-01-02-crewai.md)

* **Safety / guardrails for tool-using agents (survey chunk)** (TIL / reading note)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Safety+/+guardrails+for+tool-using+agents+(survey+chunk)) / [Reading Note](lecture_notes/2026-03-16-guardrails-agents.md)

* **AgentOps / observability for multi-agent runs** (TIL / reading note)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=AgentOps+/+observability+for+multi-agent+runs) / [Reading Note](lecture_notes/2026-04-02-agentops.md)

* **Tracing multi-agent graphs in production (LangSmith-style)** (TIL / reading note)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Tracing+multi-agent+graphs+in+production+(LangSmith-style)) / [Reading Note](lecture_notes/2026-04-04-langsmith-traces.md)

* **Agent-to-Agent (A2A) protocol notes** (TIL / reading note)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Agent-to-Agent+(A2A)+protocol+notes) / [Reading Note](lecture_notes/2026-04-08-a2a.md)

* **Orchestrator-Workers pattern (Anthropic cookbook)** (TIL / reading note)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Orchestrator-Workers+pattern+(Anthropic+cookbook)) / [Reading Note](lecture_notes/2026-04-10-orchestrator-workers.md)

* **Routing: dispatch sub-agents by intent** (TIL / reading note)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Routing:+dispatch+sub-agents+by+intent) / [Reading Note](lecture_notes/2026-04-13-routing-agents.md)

* **sympo — multi-agent PRD→WBS debate** (own project)
  * [Original Paper / Resource](https://github.com/sukoji/sympo) / [Reading Note](lecture_notes/2026-04-17-sympo-notes.md)

* **Open Interpreter / local code-execution agents** (TIL / reading note)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Open+Interpreter+/+local+code-execution+agents) / [Reading Note](lecture_notes/2026-04-30-open-interpreter.md)

* **smolagents: minimal agent framework (HF)** (TIL / reading note)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=smolagents:+minimal+agent+framework+(HF)) / [Reading Note](lecture_notes/2026-05-02-smolagents.md)

* **Llama agents / function calling patterns** (TIL / reading note)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Llama+agents+/+function+calling+patterns) / [Reading Note](lecture_notes/2026-05-05-llama-agent.md)

* **Agent Protocol interoperability draft** (TIL / reading note)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Agent+Protocol+interoperability+draft) / [Reading Note](lecture_notes/2026-05-18-agent-protocol.md)

* **Computer Use API agents** (TIL / reading note)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Computer+Use+API+agents) / [Reading Note](lecture_notes/2026-05-20-anthropic-computer-use.md)

* **OpenAI Swarm: lightweight orchestration** (TIL / reading note)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=OpenAI+Swarm:+lightweight+orchestration) / [Reading Note](lecture_notes/2026-05-22-openai-swarm.md)

* **OpenAI Agents SDK tracing + handoffs** (TIL / reading note)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=OpenAI+Agents+SDK+tracing+++handoffs) / [Reading Note](lecture_notes/2026-05-24-agents-sdk.md)

* **Claude + MCP tool ecosystem notes** (TIL / reading note)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Claude+++MCP+tool+ecosystem+notes) / [Reading Note](lecture_notes/2026-05-26-claude-mcp.md)

* **Ablation design for agent eval harnesses** (TIL / reading note)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Ablation+design+for+agent+eval+harnesses) / [Reading Note](lecture_notes/2026-05-28-eval-harness-ablation.md)

* **Human eval protocols for agent outputs** (TIL / reading note)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Human+eval+protocols+for+agent+outputs) / [Reading Note](lecture_notes/2026-05-30-human-study-agents.md)

* **awesome-self-evolving-agents curation notes** (own repo)
  * [Original Paper / Resource](https://github.com/sukoji/awesome-self-evolving-agents) / [Reading Note](lecture_notes/2026-06-02-awesome-agents.md)

* **Write-gates / re-anchoring for evolving agents** (TIL / reading note)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Write-gates+/+re-anchoring+for+evolving+agents) / [Reading Note](lecture_notes/2026-06-04-write-gates.md)

* **When to use long context vs retrieval in agents** (TIL / reading note)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=When+to+use+long+context+vs+retrieval+in+agents) / [Reading Note](lecture_notes/2026-06-10-long-context-agents.md)

* **Cost/latency tradeoffs in multi-agent fan-out** (TIL / reading note)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Cost/latency+tradeoffs+in+multi-agent+fan-out) / [Reading Note](lecture_notes/2026-06-12-cost-latency.md)

* **Parallel tool calls & branch-merge patterns** (TIL / reading note)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Parallel+tool+calls+&+branch-merge+patterns) / [Reading Note](lecture_notes/2026-06-14-parallel-agents.md)

* **Supervisor multi-agent pattern (LangGraph)** (TIL / reading note)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Supervisor+multi-agent+pattern+(LangGraph)) / [Reading Note](lecture_notes/2026-06-16-supervisor-pattern.md)

* **Agent handoffs and state machines** (TIL / reading note)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Agent+handoffs+and+state+machines) / [Reading Note](lecture_notes/2026-06-18-handoff-pattern.md)

* **Common failure modes in production agents** (TIL)
  * [Original Paper / Resource](https://github.com/sukoji/tierforge) / [Reading Note](lecture_notes/2026-06-20-failure-modes.md)

* **LLM-as-judge for multi-agent outputs** (TIL / reading note)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=LLM-as-judge+for+multi-agent+outputs) / [Reading Note](lecture_notes/2026-06-22-judge-agents.md)

* **Voting / consensus across agent opinions** (TIL / reading note)
  * [Original Paper / Resource](https://scholar.google.com/scholar?q=Voting+/+consensus+across+agent+opinions) / [Reading Note](lecture_notes/2026-06-24-consensus-agents.md)

* **Q3 reading queue — embodied + web agents** (TIL)
  * [Reading Note](lecture_notes/2026-06-26-reading-queue.md)


<details>
<summary>날짜순 전체 인덱스</summary>

| Date | Note |
|------|------|
| 2025-11-26 | [ReAct: Synergizing Reasoning and Acting in Language Models](lecture_notes/2025-11-26-react.md) |
| 2025-11-28 | [Reflexion: Language Agents with Verbal Reinforcement Learning](lecture_notes/2025-11-28-reflexion.md) |
| 2025-11-30 | [Toolformer: Language Models Can Teach Themselves to Use Tools](lecture_notes/2025-11-30-toolformer.md) |
| 2025-12-02 | [CAMEL: Communicative Agents for Mind Exploration of Large Language Model Society](lecture_notes/2025-12-02-camel.md) |
| 2025-12-04 | [MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework](lecture_notes/2025-12-04-metagpt.md) |
| 2025-12-06 | [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](lecture_notes/2025-12-06-autogen.md) |
| 2025-12-08 | [Generative Agents: Interactive Simulacra of Human Behavior](lecture_notes/2025-12-08-generative-agents.md) |
| 2025-12-10 | [Voyager: An Open-Ended Embodied Agent with Large Language Models](lecture_notes/2025-12-10-voyager.md) |
| 2025-12-12 | [AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors](lecture_notes/2025-12-12-agentverse.md) |
| 2025-12-15 | [HuggingGPT: Solving AI Tasks with ChatGPT and Its Friends in Hugging Face](lecture_notes/2025-12-15-hugginggpt.md) |
| 2025-12-17 | [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](lecture_notes/2025-12-17-swe-agent.md) |
| 2025-12-19 | [LangGraph: Stateful Multi-Actor Applications with LLMs](lecture_notes/2025-12-19-langgraph.md) |
| 2025-12-21 | [Improving Factuality and Reasoning in Language Models through Multiagent Debate](lecture_notes/2025-12-21-multi-agent-debate.md) |
| 2025-12-23 | [Self-Consistency Improves Chain of Thought Reasoning in Language Models](lecture_notes/2025-12-23-mad.md) |
| 2025-12-26 | [OpenHands: An Open Platform for AI Software Developers](lecture_notes/2025-12-26-openhands.md) |
| 2025-12-28 | [The Agent Laboratory: Advancing Autonomous Research](lecture_notes/2025-12-28-agent-laboratory.md) |
| 2025-12-30 | [Magentic-One: A Generalist Multi-Agent System for Solving Complex Tasks](lecture_notes/2025-12-30-magentic-one.md) |
| 2026-01-02 | [CrewAI — role-based agent crews](lecture_notes/2026-01-02-crewai.md) |
| 2026-01-04 | [Encouraging Divergent Thinking in LLMs through Multi-Agent Debate](lecture_notes/2026-01-04-llm-debate.md) |
| 2026-01-06 | [Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents](lecture_notes/2026-01-06-agent-q.md) |
| 2026-01-08 | [Multi-Agent Collaboration via Evolving Orchestration](lecture_notes/2026-01-08-map-neo.md) |
| 2026-01-11 | [AgentBench: Evaluating LLMs as Agents](lecture_notes/2026-01-11-agentbench.md) |
| 2026-01-13 | [WebArena: A Realistic Web Environment for Building Autonomous Agents](lecture_notes/2026-01-13-webarena.md) |
| 2026-01-15 | [Mind2Web: Towards a Generalist Agent for the Web](lecture_notes/2026-01-15-mind2web.md) |
| 2026-01-17 | [τ-bench: A Benchmark for Tool-Agent-User Interaction](lecture_notes/2026-01-17-tau-bench.md) |
| 2026-01-19 | [Gorilla: Large Language Model Connected with Massive APIs](lecture_notes/2026-01-19-gorilla.md) |
| 2026-01-22 | [ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs](lecture_notes/2026-01-22-toolllm.md) |
| 2026-01-24 | [AnyTool: Self-Reflective Tool Use for Agents](lecture_notes/2026-01-24-anytool.md) |
| 2026-01-26 | [MemGPT: Towards LLMs as Operating Systems](lecture_notes/2026-01-26-memgpt.md) |
| 2026-01-28 | [Memory stream + retrieval in generative agents (follow-up)](lecture_notes/2026-01-28-generative-agents-memory.md) |
| 2026-01-30 | [A Survey on Self-Evolving Agents](lecture_notes/2026-01-30-self-evolving-agents.md) |
| 2026-02-02 | [Misevolution: Model Evolution Inspired by Natural Selection](lecture_notes/2026-02-02-misevolution.md) |
| 2026-02-04 | [Agent Workflow Memory](lecture_notes/2026-02-04-agent-workflow-memory.md) |
| 2026-02-06 | [AutoAct: Automatic Agent Learning from Tool Use](lecture_notes/2026-02-06-autoact.md) |
| 2026-02-08 | [Multi-Agent Collaboration: Harnessing Inter-Agent Debate](lecture_notes/2026-02-08-collaborative-agents.md) |
| 2026-02-11 | [Plan-and-Solve Prompting](lecture_notes/2026-02-11-plan-and-solve.md) |
| 2026-02-13 | [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](lecture_notes/2026-02-13-tree-of-thoughts.md) |
| 2026-02-15 | [Language Agent Tree Search (LATS)](lecture_notes/2026-02-15-lass.md) |
| 2026-02-17 | [ADAPT: As-Needed Decomposition and Planning with Language Models](lecture_notes/2026-02-17-adaptive-agent.md) |
| 2026-02-19 | [AgentClinic: Multimodal agent benchmark](lecture_notes/2026-02-19-agentclinic.md) |
| 2026-02-22 | [Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent](lecture_notes/2026-02-22-mobile-agent.md) |
| 2026-02-24 | [Cradle: Generalist Computer Control Agent](lecture_notes/2026-02-24-cradle.md) |
| 2026-02-26 | [AppAgent: Multimodal Agents as Smartphone Users](lecture_notes/2026-02-26-appagent.md) |
| 2026-02-28 | [OpenAgents: An Open Platform for Language Agents](lecture_notes/2026-02-28-openagents.md) |
| 2026-03-03 | [AgentStudio: A Toolkit for Building General Virtual Agents](lecture_notes/2026-03-03-agentstudio.md) |
| 2026-03-05 | [Agent-E: Hierarchical planning for web agents](lecture_notes/2026-03-05-agent-e.md) |
| 2026-03-07 | [SeeAct: GPT-4V for Web Grounding](lecture_notes/2026-03-07-seeact.md) |
| 2026-03-09 | [WorkArena: How Capable Are Web Agents at Solving Work Tasks?](lecture_notes/2026-03-09-workarena.md) |
| 2026-03-11 | [VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks](lecture_notes/2026-03-11-visualwebarena.md) |
| 2026-03-13 | [AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents](lecture_notes/2026-03-13-agentharm.md) |
| 2026-03-16 | [Safety / guardrails for tool-using agents (survey chunk)](lecture_notes/2026-03-16-guardrails-agents.md) |
| 2026-03-18 | [Constitutional AI applied to agent loops](lecture_notes/2026-03-18-constitutional-ai-agents.md) |
| 2026-03-20 | [Aligning LLM Agents via Reinforcement Learning from Human Feedback](lecture_notes/2026-03-20-agent-alignment.md) |
| 2026-03-22 | [Tool-augmented RLHF for agents](lecture_notes/2026-03-22-rlhf-tools.md) |
| 2026-03-24 | [Training Verifiers to Solve Math Word Problems (process supervision)](lecture_notes/2026-03-24-verifiers.md) |
| 2026-03-26 | [Let's Verify Step by Step](lecture_notes/2026-03-26-process-reward.md) |
| 2026-03-28 | [Evaluation of LLM-based Agents (survey sections)](lecture_notes/2026-03-28-agent-eval-survey.md) |
| 2026-03-31 | [Which Agent Causes Task Failures — and When?](lecture_notes/2026-03-31-who-when-harness.md) |
| 2026-04-02 | [AgentOps / observability for multi-agent runs](lecture_notes/2026-04-02-agentops.md) |
| 2026-04-04 | [Tracing multi-agent graphs in production (LangSmith-style)](lecture_notes/2026-04-04-langsmith-traces.md) |
| 2026-04-06 | [Model Context Protocol (MCP)](lecture_notes/2026-04-06-mcp.md) |
| 2026-04-08 | [Agent-to-Agent (A2A) protocol notes](lecture_notes/2026-04-08-a2a.md) |
| 2026-04-10 | [Orchestrator-Workers pattern (Anthropic cookbook)](lecture_notes/2026-04-10-orchestrator-workers.md) |
| 2026-04-13 | [Routing: dispatch sub-agents by intent](lecture_notes/2026-04-13-routing-agents.md) |
| 2026-04-15 | [Hierarchical multi-agent control](lecture_notes/2026-04-15-hierarchical-agents.md) |
| 2026-04-17 | [sympo — multi-agent PRD→WBS debate](lecture_notes/2026-04-17-sympo-notes.md) |
| 2026-04-19 | [Corrective RAG / agentic RAG for tool loops](lecture_notes/2026-04-19-rag-agents.md) |
| 2026-04-21 | [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](lecture_notes/2026-04-21-self-rag.md) |
| 2026-04-23 | [FreshLLMs: Refreshing LLMs with search-augmented agents](lecture_notes/2026-04-23-freshllms.md) |
| 2026-04-25 | [Search-in-the-loop agents (Perplexity-style architectures)](lecture_notes/2026-04-25-search-agents.md) |
| 2026-04-28 | [Executable Code Actions Elicit Better LLM Agents](lecture_notes/2026-04-28-codeact.md) |
| 2026-04-30 | [Open Interpreter / local code-execution agents](lecture_notes/2026-04-30-open-interpreter.md) |
| 2026-05-02 | [smolagents: minimal agent framework (HF)](lecture_notes/2026-05-02-smolagents.md) |
| 2026-05-05 | [Llama agents / function calling patterns](lecture_notes/2026-05-05-llama-agent.md) |
| 2026-05-07 | [Multi-Agent Reinforcement Learning basics for LLM teams](lecture_notes/2026-05-07-multi-agent-rl.md) |
| 2026-05-09 | [MADDPG intuition for cooperative agents](lecture_notes/2026-05-09-maddpg-note.md) |
| 2026-05-11 | [Communication networks in multi-agent RL](lecture_notes/2026-05-11-commnet.md) |
| 2026-05-13 | [QMIX monotonic value factorization (reference)](lecture_notes/2026-05-13-qmix.md) |
| 2026-05-15 | [LLM-based MARL hybrids (2024 papers skim)](lecture_notes/2026-05-15-llm-marl.md) |
| 2026-05-18 | [Agent Protocol interoperability draft](lecture_notes/2026-05-18-agent-protocol.md) |
| 2026-05-20 | [Computer Use API agents](lecture_notes/2026-05-20-anthropic-computer-use.md) |
| 2026-05-22 | [OpenAI Swarm: lightweight orchestration](lecture_notes/2026-05-22-openai-swarm.md) |
| 2026-05-24 | [OpenAI Agents SDK tracing + handoffs](lecture_notes/2026-05-24-agents-sdk.md) |
| 2026-05-26 | [Claude + MCP tool ecosystem notes](lecture_notes/2026-05-26-claude-mcp.md) |
| 2026-05-28 | [Ablation design for agent eval harnesses](lecture_notes/2026-05-28-eval-harness-ablation.md) |
| 2026-05-30 | [Human eval protocols for agent outputs](lecture_notes/2026-05-30-human-study-agents.md) |
| 2026-06-02 | [awesome-self-evolving-agents curation notes](lecture_notes/2026-06-02-awesome-agents.md) |
| 2026-06-04 | [Write-gates / re-anchoring for evolving agents](lecture_notes/2026-06-04-write-gates.md) |
| 2026-06-06 | [Memory for LLM-based agents (survey)](lecture_notes/2026-06-06-agent-memory-survey.md) |
| 2026-06-08 | [Retrieval-augmented generation in agent loops](lecture_notes/2026-06-08-retrieval-agents.md) |
| 2026-06-10 | [When to use long context vs retrieval in agents](lecture_notes/2026-06-10-long-context-agents.md) |
| 2026-06-12 | [Cost/latency tradeoffs in multi-agent fan-out](lecture_notes/2026-06-12-cost-latency.md) |
| 2026-06-14 | [Parallel tool calls & branch-merge patterns](lecture_notes/2026-06-14-parallel-agents.md) |
| 2026-06-16 | [Supervisor multi-agent pattern (LangGraph)](lecture_notes/2026-06-16-supervisor-pattern.md) |
| 2026-06-18 | [Agent handoffs and state machines](lecture_notes/2026-06-18-handoff-pattern.md) |
| 2026-06-20 | [Common failure modes in production agents](lecture_notes/2026-06-20-failure-modes.md) |
| 2026-06-22 | [LLM-as-judge for multi-agent outputs](lecture_notes/2026-06-22-judge-agents.md) |
| 2026-06-24 | [Voting / consensus across agent opinions](lecture_notes/2026-06-24-consensus-agents.md) |
| 2026-06-26 | [Q3 reading queue — embodied + web agents](lecture_notes/2026-06-26-reading-queue.md) |

</details>
