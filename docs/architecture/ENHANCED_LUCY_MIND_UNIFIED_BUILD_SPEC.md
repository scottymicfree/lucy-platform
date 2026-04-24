# EnhancedLucyMind — Unified Build Specification

Below is a consolidated **one-build EnhancedLucyMind architecture** that updates the folder diagram and turns your notes into a single implementation-ready spec.

This spec keeps the existing structure intact, adds the missing runtime links, and makes the flow executable end to end.

> Note: Credentials must be rotated and stored in environment variables or a secrets manager. Do not embed passwords or sensitive tokens in build instructions.

## 1) Build goal

Implement **one connected machine-mind architecture** that runs locally and can later expand to Cloud Run + Firebase Hosting without changing the core module boundaries.

### Required live flow

**Input → Perception → Memory retrieval → EmmaPrime routing → LittleLucys parallel reasoning → EmmaPrime merge/safety/audit → LucyPrime synthesis → Outputs → Logs → TrainingPipeline → MobileAPI response**

### Core operating rules

- Do not recreate folders.
- Do not rename directories.
- Do not bypass EmmaPrime.
- Do not let Little Lucys speak externally.
- LucyPrime is the only external response layer.
- All major steps must log structured traces.
- Training data must be captured for future fine-tuning.
- Node communication should be modeled as EventBus-driven, even if first implementation uses an in-process bus.

---

## 2) Updated folder diagram

```text
EnhancedLucyMind/
│
├── main.py                         # top-level system bootstrap
├── orchestrator.py                 # high-level request coordinator
├── requirements.txt
├── .env.example
├── README.md
│
├── core/
│   ├── __init__.py
│   ├── models.py                   # shared dataclasses / pydantic models
│   ├── config.py                   # env/config loader
│   ├── message_schema.py           # strict node/event message schema
│   └── utils.py
│
├── LucyPrime/
│   ├── __init__.py
│   ├── synthesis_engine.py         # final synthesis from merged package
│   ├── identity_core.py            # Lucy identity rules
│   ├── prime_state.py              # idle/thinking/responding/self-state
│   ├── long_term_memory.py         # only LucyPrime may persist durable memory
│   └── output_formatter.py         # final response shaping
│
├── LittleLucys/
│   ├── __init__.py
│   ├── base_agent.py               # common reasoning contract
│   ├── lucy3_base.py               # analytical lane
│   ├── lucy_3_eve.py               # reflective lane
│   ├── lucy3_ai_os.py              # strategic / systems lane
│   ├── lucy3_3.py                  # creative / synthesis lane
│   └── agent_registry.py           # maps tasks → agent classes
│
├── EmmaPrime/
│   ├── __init__.py
│   ├── router.py                   # choose agents + execution plan
│   ├── merge_engine.py             # score and merge candidate outputs
│   ├── safety_gate.py              # policy / consistency / risk checks
│   ├── audit_engine.py             # decision trace + explainability
│   └── memory_promotion.py         # trigger memory write requests to Prime
│
├── LilEmmas/
│   ├── __init__.py
│   ├── emma_router.py              # optional helper logic
│   ├── emma_watch.py               # timing / retry / health helper
│   ├── emma_guard.py               # helper safety checks
│   ├── emma_merge.py               # helper merge transforms
│   ├── emma_memory.py              # helper memory scoring
│   └── emma_audit.py               # helper trace packaging
│
├── NodeMesh/
│   ├── __init__.py
│   ├── node.py                     # generic node definition
│   ├── node_manager.py             # registry / health / activation
│   ├── event_bus.py                # async pub/sub core
│   ├── dag_builder.py              # build request DAGs
│   ├── scheduler.py                # async task scheduling
│   ├── attention_weights.py        # weighting helpers
│   ├── shared_nodes.py             # common mesh utilities
│   └── clusters/
│       ├── lucy3_base_cluster.py
│       ├── eve_cluster.py
│       ├── ai_os_cluster.py
│       ├── lucy3_3_cluster.py
│       └── emma_cluster.py
│
├── Memory/
│   ├── __init__.py
│   ├── vector_store.py             # placeholder embeddings / similarity
│   ├── graph_store.py              # relationship storage placeholder
│   ├── episodic.py                 # per-session memory logging
│   ├── persona_memory.py           # Lucy identity facts/preferences
│   ├── sync.py                     # memory sync hooks
│   ├── retriever.py                # RAG retrieval interface
│   └── memory_manager.py           # unified memory facade
│
├── Perception/
│   ├── __init__.py
│   ├── input_processor.py          # raw input → structured query
│   ├── classifier.py               # intent/domain/urgency classification
│   ├── embedding.py                # embedding adapter placeholder
│   └── normalizer.py               # input cleanup / validation / metadata
│
├── Outputs/
│   ├── __init__.py
│   ├── text_output.py              # response packaging
│   ├── voice_output.py             # TTS stub / adapter
│   ├── action_dispatcher.py        # downstream system actions
│   ├── stream_output.py            # streaming/websocket output hooks
│   └── mobile_adapter.py           # response shaping for MobileAPI
│
├── Domains/
│   ├── __init__.py
│   ├── fivem/
│   │   ├── __init__.py
│   │   └── fivem_adapter.py        # FiveM task adapter
│   ├── system/
│   │   ├── __init__.py
│   │   └── system_control.py
│   └── external/
│       ├── __init__.py
│       └── api_adapter.py
│
├── Safety/
│   ├── __init__.py
│   ├── rules.py                    # policy and constraints
│   ├── monitor.py                  # safety monitoring
│   └── risk.py                     # scoring helpers
│
├── Logs/
│   ├── __init__.py
│   ├── logger.py                   # structured JSON logger
│   ├── trace_logger.py             # node/event traces
│   └── error_logger.py             # exceptions / failures
│
├── MobileAPI/
│   ├── __init__.py
│   ├── app.py                      # FastAPI app
│   ├── routes.py                   # /input /response /state /ws
│   ├── schemas.py                  # request/response models
│   └── session_state.py            # latest response/system state cache
│
└── TrainingPipeline/
    ├── __init__.py
    ├── recorder.py                 # JSONL training record writer
    ├── dataset_schema.py           # future FT schema
    └── export.py                   # export sessions for tuning
```

---

## 3) Layer responsibilities (summary)

### `main.py`
- load config
- initialize logger
- initialize EventBus
- initialize Memory manager
- initialize Perception
- initialize EmmaPrime
- initialize Little Lucy registry
- initialize LucyPrime
- initialize TrainingPipeline
- expose system object to MobileAPI

### `orchestrator.py`
Top-level request controller:
- accept request from API
- assign request/session IDs
- emit entry event
- run Perception
- run Memory retrieval
- Emma routing
- run Little Lucys concurrently
- Emma merge/safety/audit
- LucyPrime synthesis
- write logs
- write training record
- update response cache for MobileAPI

---

## 4) Strict node message format (canonical)

This must be centralized in `core/message_schema.py` and used everywhere.

```json
{
  "id": "uuid",
  "source": "node_id",
  "target": "node_id",
  "type": "request|response|event",
  "payload": {},
  "confidence": 0.0,
  "trace": [],
  "timestamp": 0
}
```

---

## 5) Emma merge scoring (canonical)

```text
final_score = confidence*0.4 + relevance*0.3 + consistency*0.2 + novelty*0.1
```

---

## 6) One-build implementation order

### Phase 1 — Runtime spine
- `core/models.py`
- `core/message_schema.py`
- `NodeMesh/event_bus.py`
- `NodeMesh/node_manager.py`
- `NodeMesh/dag_builder.py`
- `Logs/logger.py`

### Phase 2 — Input + memory + basic reasoning
- `Perception/input_processor.py`
- `Perception/classifier.py`
- `Perception/normalizer.py`
- `Memory/memory_manager.py`
- `Memory/retriever.py`
- `Memory/episodic.py`
- first 4 Little Lucy agents

### Phase 3 — Emma supervisory control
- `EmmaPrime/router.py`
- `EmmaPrime/merge_engine.py`
- `EmmaPrime/safety_gate.py`
- `EmmaPrime/audit_engine.py`

### Phase 4 — LucyPrime synthesis
- `LucyPrime/identity_core.py`
- `LucyPrime/prime_state.py`
- `LucyPrime/synthesis_engine.py`
- `LucyPrime/output_formatter.py`
- `LucyPrime/long_term_memory.py`

### Phase 5 — API + outputs + training
- `Outputs/mobile_adapter.py`
- `Outputs/text_output.py`
- `TrainingPipeline/recorder.py`
- `MobileAPI/app.py`
- `MobileAPI/routes.py`
- `MobileAPI/session_state.py`

### Phase 6 — visual stream + mobile twin hooks
- WebSocket `/ws/visual-stream`
- event broadcasting
- state diffs
- command queue support stubs
- voice hooks
