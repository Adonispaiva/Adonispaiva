# ADR-001: Arquitetura Base do Backend RAG Inovexa

## Contexto
O GPT Inovexa 2.0 exige um backend RAG com governança documental, memória operacional separada do corpus normativo, observabilidade e capacidade de evolução sem quebra de contrato.

## Decisão
Adotar arquitetura modular em camadas (`domain`, `application`, `infrastructure`, `api`, `schemas`, `workers`) com portas explícitas para indexação vetorial/lexical, geração e auditoria. A precedência documental será tratada no domínio por serviço dedicado de autoridade.

## Alternativas rejeitadas
1. **Monólito sem camadas**: reduz acoplamento inicial, porém inviabiliza governança e evolução.
2. **Lógica em scripts ad-hoc**: acelera protótipo, mas quebra rastreabilidade e testabilidade.
3. **Memória e corpus unificados**: simplifica busca no curto prazo, mas viola regra de fonte normativa primária.

## Consequências
- Maior clareza de responsabilidade por módulo.
- Base pronta para integração com PostgreSQL + pgvector e indexador lexical real.
- Introduz overhead inicial de estrutura, compensado por robustez e anti-regressão.

## Próximos ADRs necessários
- ADR-002: Estratégia de versionamento documental e supersessão.
- ADR-003: Política de retenção e quarentena por sensibilidade.
- ADR-004: Estratégia de avaliação contínua de recuperação e resposta.
