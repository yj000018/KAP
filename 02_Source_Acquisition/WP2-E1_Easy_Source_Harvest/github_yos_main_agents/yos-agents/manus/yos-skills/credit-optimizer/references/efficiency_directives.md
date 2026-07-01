# Diretivas de Eficiência v5 - ZERO Quality Loss (Audited)

## Princípio Fundamental

> Otimize o PROCESSO INTERNO (raciocínio, iterações, tokens de pensamento). O OUTPUT FINAL deve ter a qualidade e profundidade que a tarefa exige. Na dúvida, SEMPRE priorize qualidade.

## Roteamento Inteligente de Modelo

| Complexidade | Modelo | Justificativa |
|---|---|---|
| Baixa | Manus 1.6 (Standard) | Suficiente para tarefas simples |
| Média | Manus 1.6 (Standard) | Bom equilíbrio custo/qualidade |
| Alta | Manus 1.6 Max | 19.2% mais qualidade (dado oficial). Auto-selecionado. |

**Regra**: O script decide automaticamente. NUNCA bloquear Max quando recomendado.

## Chat Mode vs Agent Mode (v5 Auditado)

| Tarefa | Modo | Justificativa |
|---|---|---|
| Q&A conceitual, brainstorm | Chat Mode (gratuito) | Não precisa de ferramentas |
| Tradução simples | Chat Mode (gratuito) | Não precisa executar nada |
| Pesquisa factual/temporal | **Agent Mode** | PRECISA buscar dados atuais online |
| Qualquer tarefa com output de arquivo | **Agent Mode** | Chat Mode NÃO gera arquivos |
| Correção/debug de CÓDIGO | **Agent Mode** | PRECISA executar e testar |
| Desenvolvimento | **Agent Mode** | PRECISA de sandbox e ferramentas |
| Análise de dados | **Agent Mode** | PRECISA de Python e ferramentas |

**v5 FIX**: Detecção automática de necessidade de arquivo e dados factuais.

## Diretivas por Tipo de Tarefa

### Código/Desenvolvimento

| Diretiva | v4 (antes) | v5 (agora) | Impacto |
|----------|-----------|-----------|---------|
| Qualidade do código | "Solução mais simples possível" | "Robusto, limpo e elegante" | +qualidade |
| Refatoração | "NÃO refatore" | "Escreva limpo desde o início" | +qualidade |
| Testes (simples) | 1 teste + entregar se falhar | 1 teste + até 3 tentativas | +qualidade |
| Testes (complexo) | Modulares + integração | Modulares + integração + até 3 tentativas | +qualidade |
| Falha persistente | "Corrigir 1x e entregar" | "Até 3x, depois informar usuário" | +qualidade |
| Context (longo) | Salvar em arquivos | Checkpoints por módulo | +qualidade |

### Pesquisa

| Diretiva | v4 (antes) | v5 (agora) | Impacto |
|----------|-----------|-----------|---------|
| Dados factuais | "Priorize conhecimento interno" | "SEMPRE busque online" | +qualidade |
| Buscas | 3 queries por busca | 3 queries por busca | 0% perda |
| Relatório | "Mantenha conciso" | "Profundidade que a tarefa exige" | +qualidade |
| Q&A com dados atuais | Chat Mode | Agent Mode (auto-detectado) | +qualidade |

### Criação de Conteúdo

| Diretiva | v4 (antes) | v5 (agora) | Impacto |
|----------|-----------|-----------|---------|
| Conteúdo curto | Tudo de uma vez | Tudo de uma vez | 0% perda |
| Conteúdo longo | Seção por seção | Seção por seção | 0% perda |
| Revisão com arquivo | Chat Mode (incorreto) | Agent Mode (auto-detectado) | +qualidade |
| Extensão do output | "Mantenha conciso" | "Extensão que a tarefa exige" | +qualidade |

### Geração de Mídia (NOVO v5)

| Diretiva | v4 (antes) | v5 (agora) | Impacto |
|----------|-----------|-----------|---------|
| Prompt vago | Gerar e ver | Coletar detalhes ANTES | -custo, +qualidade |
| Especificações | Genéricas | Estilo, dimensões, cores, referências | +qualidade |
| Completude baixa | Gerar mesmo assim | REFINE_FIRST automático | -custo |

### Tarefas Mistas (NOVO v5)

| Diretiva | v4 (antes) | v5 (agora) | Impacto |
|----------|-----------|-----------|---------|
| Detecção | Classificar em UMA categoria | Detectar múltiplos componentes | +qualidade |
| Execução | Aplicar regras de 1 tipo | Decompor em fases, regras por tipo | +qualidade |

## Diretivas de Reasoning Budget

| Nível | Instrução v5 | Quando Usar |
|-------|-----------|-------------|
| Light | "Responda de forma concisa e direta, mas com a profundidade que a pergunta merece." | Q&A simples |
| Light | "Responda de forma concisa. Foque no que é relevante." | Conteúdo simples |
| Moderate | "Raciocine de forma moderada. Foque na solução." | Tarefas médias |
| Deep | "Raciocine passo a passo de forma eficiente. O output deve ter a profundidade que a tarefa exige." | Pesquisa, código complexo |

**v5 FIX**: NUNCA suprimir raciocínio completamente. "Conciso" ao invés de "sem raciocínio".

## Fontes de Economia SEGURAS (0% impacto na qualidade)

1. Chat Mode para Q&A/brainstorm/tradução (100% economia)
2. One-shot prompt completo para conteúdo curto (elimina follow-ups)
3. Batch queries (3 variants por busca, mesma cobertura)
4. Context compression (salvar em arquivos)
5. Markdown extraction (ao invés de scroll)
6. Planejamento no Chat Mode antes de executar (gratuito)
7. Raciocínio interno eficiente (menos tokens de pensamento)
8. Coletar detalhes de mídia antes de gerar (evita re-geração)

## Regra de Veto

> Se qualquer diretiva de eficiência conflitar com a qualidade do resultado final, a qualidade SEMPRE vence. Economia de créditos é secundária à entrega de um resultado excelente.
