%%==========================================================
%% AI Instructional Workflow Generator - System Architecture
%%==========================================================

flowchart TB

    %% ROOT
    ROOT[🔵 ai-instructional-workflow-generator]:::root

    %% LEGACY / INTERFACE
    ROOT --> G[🟦 generator/]:::cli
    G --> Gm[🟧 main.py]:::module
    G --> Gw[🟧 workflow.py]:::module
    G --> Ge[🟧 evaluation.py]:::module
    G --> Gr[🟧 recursive_expansion.py]:::module
    G --> Gx[🟧 exporters.py]:::module
    G --> Gu[🟧 utils.py]:::module

    %% CORE LOGIC
    ROOT --> C[🟩 ai_core/]:::package
    C --> CW[🟧 workflow.py]:::module
    C --> CP[🟩 phases/]:::package
    CP --> CP1[🟧 initialization.py]:::module
    CP --> CP2[🟧 refinement.py]:::module
    CP --> CP3[🟧 modularization.py]:::module
    CP --> CP4[🟧 human_readable.py]:::module
    CP --> CP5[🟧 evaluation.py]:::module
    CP --> CP6[🟧 regeneration.py]:::module
    C --> CR[🟧 registry.py]:::module

    %% RECURSIVE ENGINE
    ROOT --> R[🟩 ai_recursive/]:::package
    R --> RE[🟧 expansion.py]:::module
    R --> RM[🟧 merging.py]:::module
    R --> RR[🟧 registry.py]:::module
    R --> RV[🟧 evaluator.py]:::module
    R --> RL[🟧 memory.py]:::module

    %% MEMORY SYSTEM
    ROOT --> M[🟩 ai_memory/]:::package
    M --> MS[🟧 store.py]:::module
    M --> ML[🟧 lineage.py]:::module
    M --> MM[🟧 metrics.py]:::module
    M --> MA[🟧 analytics.py]:::module

    %% EVALUATION
    ROOT --> E[🟩 ai_evaluation/]:::package
    E --> EB[🟧 base.py]:::module
    E --> EC[🟧 clarity.py]:::module
    E --> EE[🟧 expandability.py]:::module
    E --> ET[🟧 translatability.py]:::module
    E --> ER[🟧 registry.py]:::module

    %% SUPPORTING DATA + SCHEMAS
    ROOT --> D[🟩 data/]:::package
    D --> DT[🟩 templates/]:::package
    D --> DO[🟩 outputs/]:::package

    ROOT --> S[🟩 schemas/]:::package
    S --> SW[🟨 workflow_schema.json]:::config
    S --> SM[🟨 module_schema.json]:::config
    S --> SE[🟨 evaluation_schema.json]:::config

    %% TESTS
    ROOT --> T[🟩 tests/]:::package
    T --> TA[🟪 test_ai_core.py]:::test
    T --> TR[🟪 test_recursive.py]:::test
    T --> TM[🟪 test_memory.py]:::test
    T --> TE[🟪 test_evaluation.py]:::test
    T --> TX[🟪 test_exporters.py]:::test

    %% DOCS
    ROOT --> DOC[🟥 docs/]:::docs
    DOC --> DA[🟥 ARCHITECTURE.md]:::docs
    DOC --> DR[🟥 AI_RECURSION.md]:::docs
    DOC --> DM[🟥 METRICS_SYSTEM.md]:::docs
    DOC --> DE[🟥 EVOLUTION_LOGGING.md]:::docs
    DOC --> DG[🟥 CONTRIBUTOR_GUIDE.md]:::docs

    %% STYLING
    classDef root fill:#0096FF,stroke:#003366,color:white;
    classDef package fill:#00C957,stroke:#006400,color:white;
    classDef module fill:#FFB347,stroke:#CC7000,color:black;
    classDef config fill:#FFD700,stroke:#CCAC00,color:black;
    classDef test fill:#A020F0,stroke:#5D007A,color:white;
    classDef docs fill:#FF6B6B,stroke:#B22222,color:white;
    classDef cli fill:#00CED1,stroke:#007C80,color:black;
