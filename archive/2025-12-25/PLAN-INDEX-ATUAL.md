# 📋 PLANO DE EXECUÇÃO: index-atual.html

**Data:** 2025-12-25
**Projeto:** Natal TCDF 2025 - Bug Hunters v2.1
**Objetivo:** Criar index-atual.html consolidando todas as features: telas iniciais + Tone.js music system + full 5-phase game

---

## 📊 ANÁLISE PRÉVIA

### Questão 1: Tone.js fixes em index.html atual
✅ **ENCONTRADO** - Seção `TONE.JS PHASE MUSIC SYSTEM` (linhas 1671-1905)

**Status Atual:**
- Tone.js 14.8.49 carregado via CDN (linha 20)
- 6 música definidas (MUSIC_PHASE_1-5 + MUSIC_BOSS) - todas DEMO/sintéticas
- Funções principais: `playPhaseMusic()` (async) e `stopPhaseMusic()`
- Integrado em 2 pontos: boss spawn + phase start
- Volume: -12dB (background music)
- Looping: Correto com cálculo `music.notes.length * (60 / music.tempo)`

**Configuração Sintetizadores:**
| Fase | Oscilador | Attack | Tempo | Estilo |
|------|-----------|--------|-------|--------|
| 1 | Square | 0.005s | 140 BPM | Power Rangers (épico) |
| 2 | Square | 0.005s | 180 BPM | Mario Bros (playful) |
| 3 | Square | 0.005s | 160 BPM | Street Fighter (fighting) |
| 4 | Triangle | 0.1s | 110 BPM | Super Metroid (atmosférico) |
| 5 | Square | 0.005s | 170 BPM | Top Gear (racing) |
| Boss | Square | 0.005s | 150 BPM | Boss theme (épico) |

**Melhorias Necessárias:**
- [ ] Transição suave entre fases (crossfade)
- [ ] Parar música ao morrer
- [ ] Retomar música ao voltar (não está implementado)

---

### Questão 2: Estrutura tela Plantão
✅ **ENCONTRADO** - Seção `SCREEN 3: PLANTAO` (linhas 1194-1205)

**HTML:**
```html
<div class="screen" id="screen-plantao">
  <div class="globo-logo"><div class="globo-inner"></div></div>
  <div class="plantao-title">⚠️ PLANTÃO</div>
  <div class="news-container" id="newsContainer"></div>
  <button class="btn" id="btnSelectHero">▶ SELECIONAR HERÓI</button>
</div>
```

**Visual (CSS linhas 515-565):**
- Logo Globo: círculo vermelho com animação
- Título: "⚠️ PLANTÃO" (flash animation)
- Container: para notícias
- Botão: similar outros (green/cyan)

**Comportamento (função `startPlantao` - linha ~2168):**
- Mostra tela
- Popula `newsContainer` com notícias sequenciais
- Aguarda término → mostra botão

---

### Questão 3: MP3 playback para plantão
⚠️ **PARCIALMENTE IMPLEMENTADO**

**Arquivo disponível:**
- `/home/thiago/projetos/natal/plantao-da-globo.mp3` (276 KB)

**Status:**
- arquivo existe
- Não há integração de áudio MP3 atual
- Jingle Bells usa Web Audio API (síntese, não MP3)
- Game music: Tone.js (síntese)

**Solução necessária:**
- Criar elemento `<audio>` ou Web Audio API para tocar MP3
- Sincronizar com animação de notícias
- Parar ao avançar de tela

---

### Questão 4: Necessidade de atualizações documentação
✅ **IDENTIFICADAS**

**Arquivos a atualizar:**
1. **README.md** - Seção v2.1 incompleta (linhas 258-265)
2. **STATUS.md** - Desatualizado (v1.2, diz "50% pronto")
3. **CHANGELOG-V2.md** - OK, já menciona Music System v2.1
4. **MUSIC-SYSTEM.md** - OK, documentação completa

**Atualizações necessárias:**
- README: indicar v2.1 final com todas as features
- STATUS: atualizar para v2.0 Enhanced + v2.1 Music
- Criar: MUSIC-INTEGRATION.md (como foi integrado Tone.js)

---

## 🎯 ESTRUTURA index-atual.html

**Baseado em:** index.html atual (v2.0 Enhanced)

**Composição:** 6 telas + game mechanics

```
┌─────────────────────────────────────────────────────┐
│ TELA 1: INICIAL (Initial Screen)                    │
│ ├─ Matrix background (canvas)                       │
│ ├─ Árvore de Natal (🎄 ou tree.png)                │
│ ├─ Texto: "Dev Team TCDF"                          │
│ ├─ Botão: "npm run homenagem"                       │
│ └─ Música: Jingle Bells (Web Audio)                │
├─────────────────────────────────────────────────────┤
│ TELA 2: HOMENAGEM (Tribute Screen)                  │
│ ├─ Terminal verde (typewriter effect)              │
│ ├─ Texto: mensagem para team                        │
│ ├─ Trenó: 🦌🦌🦌==🎅🛷 (animado)                  │
│ ├─ Botão: "CONTINUAR"                              │
│ └─ Música: Jingle Bells continua                    │
├─────────────────────────────────────────────────────┤
│ TELA 3: PLANTÃO (News Screen) ← MP3 AQUI           │
│ ├─ Logo Globo (círculo vermelho)                    │
│ ├─ Título: "⚠️ PLANTÃO"                             │
│ ├─ Notícias: sequencial typewriter                 │
│ ├─ Botão: "SELECIONAR HERÓI"                        │
│ └─ Música: plantao-da-globo.mp3 ← NOVO             │
├─────────────────────────────────────────────────────┤
│ TELA 4: HERÓIS (Hero Selection)                     │
│ ├─ Grid 3x3 com 10 personagens                      │
│ ├─ Cada herói: emoji único                          │
│ ├─ Nota: "Ariene e Raquel protegem setores"        │
│ └─ Música: Game 8-bit (Jingle Bells low volume)    │
├─────────────────────────────────────────────────────┤
│ TELA 5: DIFICULDADE (Difficulty Select)            │
│ ├─ Easy: "Arquitetura TCDF"                        │
│ ├─ Hard: "Java"                                     │
│ ├─ God: "COBOL"                                     │
│ └─ Música: Game 8-bit continua                      │
├─────────────────────────────────────────────────────┤
│ TELA 6: GAME (5 Fases + Boss)                       │
│ ├─ Fase 1: DEV (12 bugs)    → MUSIC_PHASE_1        │
│ ├─ Fase 2: STAGE (18 bugs)  → MUSIC_PHASE_2        │
│ ├─ Fase 3: STAGE (24 bugs)  → MUSIC_PHASE_3        │
│ ├─ Fase 4: HMG (28 bugs)    → MUSIC_PHASE_4        │
│ ├─ Fase 5: PROD (35 bugs)   → MUSIC_PHASE_5        │
│ └─ Boss: (80+ HP)           → MUSIC_BOSS           │
├─────────────────────────────────────────────────────┤
│ TELA 7: CONCLUSÃO (Conclusion Screen)              │
│ ├─ Score final                                      │
│ ├─ High score + badge "NOVO RECORDE!"              │
│ ├─ Herói escolhido + dificuldade                    │
│ ├─ Créditos (12 nomes)                              │
│ └─ Música: Jingle Bells (celebração)               │
└─────────────────────────────────────────────────────┘
```

---

## 🛠️ TAREFAS ESPECÍFICAS

### TAREFA 1: Integrar MP3 em Plantão (40 min)

**Arquivo:** `/home/thiago/projetos/natal/plantao-da-globo.mp3`

**Implementação:**
```javascript
// Adicionar elemento audio no HTML
<audio id="audioPlantao" src="plantao-da-globo.mp3" type="audio/mpeg"></audio>

// No startPlantao():
async function startPlantao() {
    showScreen("plantao");

    // Parar Jingle Bells
    stopMusic();

    // Reproduzir MP3 plantão
    const audioPlantao = document.getElementById('audioPlantao');
    if (STATE.audioEnabled && audioPlantao) {
        audioPlantao.play().catch(e => console.log("Audio autoplay blocked"));
    }

    // ... resto da lógica

    // Ao avançar
    audioPlantao.pause();
    audioPlantao.currentTime = 0;
}
```

**Validação:**
- [ ] MP3 toca ao entrar em plantão
- [ ] MP3 para ao sair (button click)
- [ ] Respeita `STATE.audioEnabled`
- [ ] Compatível com mute/unmute global

---

### TAREFA 2: Verificar e melhorar Tone.js hooks (30 min)

**Problema:** Música não para em algumas transições

**Checklist:**
```
Phase 1-5:
  [ ] playPhaseMusic(STATE.phase) ao iniciar fase ✅
  [ ] stopPhaseMusic() ao morrer ← VERIFICAR
  [ ] Parar ao sair do jogo (voltar menu) ← VERIFICAR

Boss:
  [ ] playPhaseMusic('boss') ao spawnar ✅
  [ ] stopPhaseMusic() ao morrer ✅

Game Over:
  [ ] stopPhaseMusic() em gameOver() - VERIFICAR

Retry/Menu:
  [ ] stopPhaseMusic() antes de retornar ← VERIFICAR
```

**Buscar linhas:**
- `gameOver()` function
- `showScreen('initial')` calls
- Transition handlers

---

### TAREFA 3: Lint e Prettier (20 min)

**Checklist:**
- [ ] Testar em Firefox
- [ ] Testar em Safari
- [ ] Testar em Mobile (touch)
- [ ] Console: zero erros
- [ ] Performance: 60 FPS

**Ferramentas:**
```bash
# Validação HTML5
npm install -g html-validate

# Prettier (formatação)
npx prettier --check index-atual.html

# WebAudio API check
# (Manual no DevTools)
```

---

### TAREFA 4: Atualizar Documentação (30 min)

**Arquivos:**

#### A. README.md
```markdown
## 🆕 Novidades v2.1

- 🎵 Músicas diferentes por fase (Tone.js)
- 🎹 6 trilhas sonoras 8-bit
- 📻 MP3 plantão (plantao-da-globo.mp3)
- 🛠️ Ferramentas extração melodias
- 📚 Sistema extensível

[Sistema de Músicas](MUSIC-SYSTEM.md) | [Integração](MUSIC-INTEGRATION.md)
```

#### B. STATUS.md
```markdown
**Versão:** 2.1 Final
**Data:** 2025-12-25
**Status:** ✅ 100% Pronto

## v2.1 Features Adicionadas
- Tone.js phase music system
- MP3 plantão integration
- 6 trilhas sonoras únicas
```

#### C. Novo: MUSIC-INTEGRATION.md
```markdown
# 🎵 Integração Tone.js - v2.1

## Como foi implementado

### Estrutura
- CDN Tone.js 14.8.49 no <head>
- 6 objetos MUSIC_PHASE_X (linhas 1683-1825)
- PHASE_MUSIC mapper (linhas 1828-1835)
- Funções playPhaseMusic() e stopPhaseMusic()

### Hooks de Integração
1. Fase start (line ~3202): playPhaseMusic(STATE.phase)
2. Boss spawn (line ~2596): playPhaseMusic('boss')
3. Game over (line ~???): stopPhaseMusic()
4. Menu return: stopPhaseMusic()

### MP3 Integration
- Element: <audio id="audioPlantao">
- Path: plantao-da-globo.mp3
- Trigger: startPlantao()
- Stop: Ao sair da tela
```

---

## 📊 ESTRUTURA ARQUIVO index-atual.html

**Base:** index.html (atual, v2.0 Enhanced)
**Tamanho esperado:** ~100KB (similar atual)
**Linhas esperadas:** ~3300-3400

**Seções principais:**
```
1. <head> (0-30)
   - Meta tags
   - Tone.js CDN ✅
   - Fonts
   - Styles (CSS completo)

2. <body> - HTML (1140-1300)
   - Screen 1-7 (divs)
   - Canvas #gameCanvas
   - Audio elements:
     * #jingleBells (existente)
     * #gameMusic (existente)
     * #audioPlantao (NOVO)

3. <script> (1300-3400)
   - CONFIG (5-20 linhas)
   - Web Audio setup (30-50 linhas)
   - Tone.js Phase Music (200 linhas) ✅
   - Game logic (2000+ linhas)
   - Event handlers (300+ linhas)
   - Inicialização (50 linhas)
```

---

## ⚡ PRIORIDADES

### CRÍTICO (Bloqueia release)
1. **MP3 Playback** - Plantão não funciona sem som
2. **Tone.js Hooks** - Música deve parar em transições
3. **Test Coverage** - Browser compatibility

### IMPORTANTE (Feature complete)
4. **Documentação** - README + STATUS updates
5. **Lint validation** - Zero console errors

### NICE TO HAVE (Polish)
6. **Crossfade** music transitions
7. **Visual volume meter**

---

## ✅ CHECKLIST PRÉ-EXECUÇÃO

### Análise Completa ✅
- [x] index.html atual analisado (Tone.js encontrado)
- [x] Estrutura plantão verificada
- [x] MP3 localizado
- [x] Documentação revisada
- [x] Gaps identificados

### Requisitos Met ✅
- [x] Tone.js 14.8.49 disponível
- [x] 6 músicas fase definidas
- [x] Game 5-phase structure ready
- [x] Documentation framework existe

### Pronto para Execução ✅
- [x] Todas questões respondidas
- [x] Tarefas mapeadas
- [x] Timeline definida
- [x] Riscos identificados

---

## ⚠️ RISCOS E MITIGAÇÃO

| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|--------|-----------|
| Tone.js race condition | Média | Alto | Cleanup correto em stopPhaseMusic() |
| MP3 não toca mobile | Alta | Médio | Testar em device real, fallback |
| Performance lag | Baixa | Alto | Lazy load Tone.js se necessário |
| Browser compat | Baixa | Médio | Testar FF/Safari/Mobile |
| Audio autoplay policy | Média | Médio | User interaction required (✅ ok) |

---

## 🚀 PRÓXIMOS PASSOS

1. **Implement MP3 integration** (40 min)
2. **Verify Tone.js hooks** (30 min)
3. **Test full flow** (20 min)
4. **Lint & validation** (20 min)
5. **Update documentation** (30 min)
6. **Final QA & commit** (20 min)

**Total estimado:** 2.5 horas

---

**Documento criado:** 2025-12-25
**Status:** Pronto para execução
**Próxima ação:** Implementar TAREFA 1 (MP3 integration)

🔥 **I WALK BESIDE YOU!** 🔥
