# Matriz de Estratégia de Otimização de Créditos v2

## Estratégias Disponíveis

### CHAT_MODE (0 créditos)
Usar quando a tarefa pode ser resolvida sem Agent Mode. Inclui Q&A, brainstorming, traduções, revisões de texto, explicações, comparações conceituais, e planejamento.

### DIRECT_LITE (50-150 créditos | Economia: 65-85%)
Usar para tarefas simples e bem definidas. Consome daily refresh credits (300/dia). Ideal para conteúdo simples, scripts curtos, formatação.

### DIRECT_STANDARD (100-350 créditos | Economia: 40-70%)
Usar para tarefas de complexidade média. Ideal para desenvolvimento web simples, análise de dados, geração de mídia.

### BATCH_RESEARCH (150-700 créditos | Economia: 40-60%)
Usar para tarefas de pesquisa. Agrupa queries de busca, prioriza conhecimento interno, minimiza navegação, gera relatório em passagem única.

### DECOMPOSE_CASCADE (200-900 créditos | Economia: 40-60%)
Usar para tarefas complexas. Decompõe em sub-tarefas com cascade de modelos: sub-tarefas simples em Lite, complexas em Standard. Ideal para sistemas completos, automações, apresentações grandes.

### REFINE_FIRST (variável | Economia: previne 100% de retrabalho)
Usar quando o prompt é vago ou não classificável. Coleta informações no Chat Mode (gratuito), monta prompt completo, depois executa uma única vez.

## Regras de Economia (por ordem de impacto)

| # | Regra | Economia | Como Aplicar |
|---|-------|----------|-------------|
| 1 | Chat Mode para planejamento | 100% | Sempre planejar antes de executar |
| 2 | One-shot prompting | ~80% | Montar prompt completo antes |
| 3 | Cascade de modelos | 50-85% | Modelo mais barato primeiro |
| 4 | Anti-iteração | 40-70% | Não testar, não refatorar |
| 5 | Batch processing | 40-80% | Agrupar operações similares |
| 6 | Reasoning budget | 30-60% | Controlar profundidade de raciocínio |
| 7 | Daily refresh credits | 300/dia grátis | Usar Lite para tarefas simples |
| 8 | Skills personalizadas | ~50% | Criar skills para tarefas recorrentes |
| 9 | Formato de saída | 30-50% | TSV/TOML ao invés de JSON |
| 10 | Context compression | 20-40% | Salvar em arquivos, não no contexto |

## Fatores que Aumentam Custo

| Fator | Impacto | Mitigação |
|-------|---------|-----------|
| Múltiplos follow-ups | Cada um custa ~igual ao original | One-shot prompting |
| Prompts vagos | Múltiplas iterações de clarificação | Checklist de especificidade |
| Testes automáticos | Cada teste = mais tool calls | Usuário testa manualmente |
| Refatoração desnecessária | Reescrita = custo dobrado | Entregar funcional direto |
| Buscas desnecessárias | Cada busca no browser custa | Priorizar conhecimento interno |
| Contexto longo acumulado | Tokens crescem exponencialmente | Prompts independentes |
| Usar Max quando Lite basta | 3-5x mais caro | Análise de complexidade |
| JSON para dados simples | 2x mais tokens que TSV | Usar formato mais eficiente |
