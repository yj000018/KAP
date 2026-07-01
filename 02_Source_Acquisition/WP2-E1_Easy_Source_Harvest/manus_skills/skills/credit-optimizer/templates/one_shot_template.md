# Template de One-Shot Prompt Otimizado v2

## Instruções
Preencher TODOS os campos [OBRIGATÓRIO] antes de enviar ao Agent Mode.
Campos [SE APLICÁVEL] podem ser omitidos se não relevantes.
A seção DIRETIVAS DE EFICIÊNCIA é gerada automaticamente pelo script de análise.

---

## TAREFA
[OBRIGATÓRIO] Descrever em uma frase clara e objetiva o que deve ser feito.

## CONTEXTO
[OBRIGATÓRIO] Informações de background necessárias para entender a tarefa.

## REQUISITOS TÉCNICOS
[SE APLICÁVEL] Tecnologias, frameworks, linguagens, versões.

## ESPECIFICAÇÕES DETALHADAS

### Estrutura
[OBRIGATÓRIO] Descrever a estrutura do resultado (seções, páginas, componentes).

### Conteúdo
[OBRIGATÓRIO] Todo texto literal entre aspas. Dados exatos. Referências.

### Visual
[SE APLICÁVEL] Cores (hex), fontes, espaçamentos, layout.

### Comportamento
[SE APLICÁVEL] Interações, animações, estados (hover, click, erro, sucesso, loading).

### Responsividade
[SE APLICÁVEL] Comportamento em mobile, tablet, desktop.

## FORMATO DE SAÍDA
[OBRIGATÓRIO] Tipo de arquivo, estrutura de pastas, formato de entrega.
DICA: Para dados estruturados, preferir TSV/TOML ao invés de JSON (50% menos tokens).

## RESTRIÇÕES
[SE APLICÁVEL] O que NÃO fazer. Limitações. Tecnologias a evitar.

## REFERÊNCIAS
[SE APLICÁVEL] Links, screenshots, exemplos de sites/apps similares.

## DIRETIVAS DE EFICIÊNCIA
[AUTO-GERADO] Copiar as diretivas do output do script analyze_prompt.py aqui.
Exemplo:
- Construa a solução mais simples possível
- NÃO teste automaticamente - eu testarei manualmente
- NÃO reescreva ou refatore código existente
- Antes de cada passo, verifique se há forma mais simples e barata

---

## Exemplo Preenchido (Desenvolvimento Web)

TAREFA: Criar uma landing page para o produto "CloudSync Pro".

CONTEXTO: CloudSync Pro é um serviço de sincronização de arquivos em nuvem para PMEs com 10-50 funcionários.

REQUISITOS TÉCNICOS: HTML, CSS, JavaScript. Sem frameworks. Arquivo único.

ESPECIFICAÇÕES DETALHADAS:

Estrutura:
- Hero section com headline, subtítulo e CTA
- Seção de 3 features com ícones
- Seção de pricing com 3 planos
- Footer com links e copyright

Conteúdo:
- Headline: "Sincronize seus arquivos. Simplifique seu negócio."
- Subtítulo: "CloudSync Pro mantém sua equipe conectada."
- CTA: "Comece Grátis por 14 Dias"
- Features: "Sync em Tempo Real", "Backup Automático", "Compartilhamento Seguro"
- Planos: Starter ($9/mês), Business ($29/mês), Enterprise ($79/mês)

Visual:
- Cores: Primary #2563EB, Secondary #1E40AF, Accent #10B981, Background #F8FAFC
- Fonte: Inter (Google Fonts)

Comportamento:
- CTA button: hover muda para #1D4ED8
- Pricing cards: hover eleva com box-shadow

Responsividade:
- Mobile: stack vertical, hamburger menu
- Desktop: grid 3 colunas para features e pricing

FORMATO DE SAÍDA: Arquivo HTML único com CSS e JS inline.

RESTRIÇÕES: Não usar jQuery. Não usar imagens externas. Não usar frameworks CSS.

REFERÊNCIAS: Estilo similar a stripe.com/payments.

DIRETIVAS DE EFICIÊNCIA:
- Construa a solução mais simples possível que atenda aos requisitos
- NÃO teste automaticamente - eu testarei manualmente
- NÃO reescreva ou refatore código existente
- Escreva o código completo de uma vez
- Antes de cada ação, verifique se há caminho mais curto
