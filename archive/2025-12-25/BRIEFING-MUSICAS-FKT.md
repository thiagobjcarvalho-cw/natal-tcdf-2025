# 🎸 BRIEFING ÉPICO - MÚSICAS POR FASE (Tone.js)

**DOOM MODE:** ATIVO 💀🔥👑
**Missão:** Implementar 6 músicas 8-bit diferentes por fase usando Tone.js
**Agente:** FKT (Fork Terminal Apocalíptico)
**Complexidade:** DEVASTADORA 🎯

---

## 🎯 OBJETIVO PRINCIPAL

Criar sistema de música dinâmica para o jogo "Bug Hunters" onde CADA FASE tem sua própria trilha sonora épica 8-bit, usando **Tone.js** para síntese procedural.

### Músicas Alvo (Referências do YouTube)

| Fase | Ambiente | Música | URL |
|------|----------|--------|-----|
| 1 | DEV | Power Rangers 8-bit | https://www.youtube.com/watch?v=4S88ULz9c80 |
| 2 | STAGE | Mario Bros | https://www.youtube.com/watch?v=P9Ee4TevHfA |
| 3 | STAGE | Street Fighter | https://www.youtube.com/watch?v=eVA5nSWUiTQ |
| 4 | HMG | Super Metroid | https://www.youtube.com/watch?v=7f9CNCbvoXw |
| 5 | PROD | Top Gear | https://www.youtube.com/watch?v=Exwve5c0A5Y |
| 5 Boss | BOSS FIGHT | Boss Theme | https://www.youtube.com/watch?v=pTQ1YzRtERk |

---

## 📦 ARQUIVOS DE REFERÊNCIA

**Base de implementação:**
- `/home/thiago/projetos/natal/musics/index2Musics.html` - Sistema com Tone.js já implementado
- `/home/thiago/projetos/natal/musics/files/PROMPT_TONE_MUSICAS_AUTORAIS.md` - Guia completo Tone.js
- `/home/thiago/projetos/natal/musics/files/chiptune_tonejs.html` - Exemplos de synth 8-bit

**Arquivo alvo:**
- `/home/thiago/projetos/natal/index.html` - Versão 2.0 Enhanced (atual)

---

## 🛠️ FERRAMENTAS NECESSÁRIAS

### Sistema (instalar se não existir)
```bash
# yt-dlp para download de áudio
sudo apt install -y yt-dlp ffmpeg

# Python para análise (se necessário)
pip3 install librosa numpy scipy
```

---

## 🎵 TAREFA 1: CRIAR FERRAMENTA DE EXTRAÇÃO DE MELODIAS

**IMPORTANTE:** Devido a direitos autorais, vamos criar FERRAMENTAS que o usuário executa manualmente.

### 1.1 - Script Python: `extract_melody.py`

Criar script que:
- Aceita arquivo de áudio como input
- Usa librosa para detectar pitch dominante
- Quantiza notas para escala cromática
- Exporta array JavaScript com formato Tone.js
- Simplifica para ~40-60 notas (melodia principal)

**Features:**
- Detecção de BPM automática
- Quantização para notas musicais (C4, D#4, etc)
- Análise dos primeiros 20-30 segundos (loop game)
- Output direto em formato JavaScript

### 1.2 - Script Bash: `download_music.sh`

Wrapper para yt-dlp:
```bash
#!/bin/bash
# Download apenas áudio, formato WAV, primeiros 30 segundos
yt-dlp -x --audio-format wav \
       --postprocessor-args "-ss 0 -t 30" \
       -o "%(title)s.%(ext)s" \
       "$1"
```

---

## 🎵 TAREFA 2: ESTRUTURA DE DADOS TONE.JS

### 2.1 - Formato Esperado

```javascript
const MUSIC_PHASE_1 = {
    title: "Power Rangers Theme",
    tempo: 140,
    synth_config: {
        oscillator: { type: 'square' }, // 8-bit sound
        envelope: {
            attack: 0.005,
            decay: 0.1,
            sustain: 0.3,
            release: 0.1
        }
    },
    notes: [
        { note: "E5", duration: "8n" },  // colcheia
        { note: "G5", duration: "8n" },
        { note: "A5", duration: "4n" },  // semínima
        { note: "G5", duration: "8n" },
        { note: "E5", duration: "4n" },
        // ... resto da melodia
    ],
    loop: true
};
```

### 2.2 - Durações Tone.js

| Símbolo | Nome | Duração |
|---------|------|---------|
| `"1n"` | Semibreve | 4 beats |
| `"2n"` | Mínima | 2 beats |
| `"4n"` | Semínima | 1 beat |
| `"8n"` | Colcheia | 0.5 beat |
| `"16n"` | Semicolcheia | 0.25 beat |
| `"4n."` | Semínima pontuada | 1.5 beats |

---

## 🎵 TAREFA 3: SISTEMA DE MÚSICA POR FASE

### 3.1 - Integração no index.html

Modificar seção de áudio para:

```javascript
// ==========================================================================
// MUSIC SYSTEM - Tone.js Multi-Phase
// ==========================================================================
const PHASE_MUSIC = {
    1: MUSIC_PHASE_1,  // Power Rangers
    2: MUSIC_PHASE_2,  // Mario Bros
    3: MUSIC_PHASE_3,  // Street Fighter
    4: MUSIC_PHASE_4,  // Super Metroid
    5: MUSIC_PHASE_5,  // Top Gear
    boss: MUSIC_BOSS   // Boss Theme
};

let currentSynth = null;
let currentPart = null;

async function playPhaseMusic(phaseNumber) {
    // Stop música anterior
    stopMusic();

    // Inicializar Tone.js se necessário
    await Tone.start();

    const music = PHASE_MUSIC[phaseNumber];

    // Criar synth 8-bit
    currentSynth = new Tone.Synth(music.synth_config).toDestination();

    // Criar sequência
    currentPart = new Tone.Part((time, note) => {
        currentSynth.triggerAttackRelease(note.note, note.duration, time);
    }, music.notes);

    // Loop
    currentPart.loop = music.loop;
    currentPart.loopEnd = music.notes.length; // Duração total

    // Tempo
    Tone.Transport.bpm.value = music.tempo;

    // Start
    currentPart.start(0);
    Tone.Transport.start();
}

function stopMusic() {
    if (currentPart) {
        currentPart.stop();
        currentPart.dispose();
        currentPart = null;
    }
    if (currentSynth) {
        currentSynth.dispose();
        currentSynth = null;
    }
    Tone.Transport.stop();
}
```

### 3.2 - Hooks de Fase

Adicionar chamadas no código do jogo:

```javascript
// Ao iniciar fase
function startPhase(phaseNum) {
    playPhaseMusic(phaseNum);
    // ... resto do código
}

// Ao spawnar boss
function spawnBoss() {
    playPhaseMusic('boss');
    // ... resto do código
}
```

---

## 🎵 TAREFA 4: ADICIONAR TONE.JS NO HTML

### 4.1 - CDN Link

Adicionar no `<head>`:

```html
<!-- Tone.js -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/tone/14.8.49/Tone.js"></script>
```

### 4.2 - Fallback para Jingle Bells

Manter Jingle Bells atual para telas inicial/homenagem/conclusão usando Web Audio API nativo.

---

## 🎵 TAREFA 5: WORKFLOW DE EXTRAÇÃO (Manual do Usuário)

**Criar arquivo README_MUSIC_EXTRACTION.md com instruções:**

```markdown
# Como Extrair Melodias

## Passo 1: Baixar Áudio
\`\`\`bash
./download_music.sh "https://www.youtube.com/watch?v=..."
\`\`\`

## Passo 2: Extrair Melodia
\`\`\`bash
python3 extract_melody.py "arquivo.wav" > music_output.js
\`\`\`

## Passo 3: Ajustar Manualmente
- Ouvir arquivo original
- Corrigir notas erradas
- Simplificar melodia (40-60 notas)
- Ajustar BPM se necessário

## Passo 4: Integrar no index.html
- Copiar objeto JavaScript gerado
- Renomear para MUSIC_PHASE_X
- Adicionar ao PHASE_MUSIC
\`\`\`
```

---

## 🎯 ENTREGAS ESPERADAS

### Arquivos a Criar

1. **`/home/thiago/projetos/natal/tools/extract_melody.py`**
   - Script Python de extração
   - ~150 linhas
   - Bem documentado

2. **`/home/thiago/projetos/natal/tools/download_music.sh`**
   - Script Bash de download
   - ~20 linhas

3. **`/home/thiago/projetos/natal/tools/README_MUSIC_EXTRACTION.md`**
   - Guia passo a passo
   - Exemplos de uso
   - Troubleshooting

4. **`/home/thiago/projetos/natal/index.html` (MODIFICADO)**
   - Tone.js integrado
   - Sistema de música por fase
   - 6 objetos MUSIC_PHASE_X (estrutura vazia ou exemplos sintéticos)
   - Hooks corretos nas transições

5. **`/home/thiago/projetos/natal/MUSIC-SYSTEM.md`**
   - Documentação do sistema
   - Como funciona
   - Como adicionar novas músicas

---

## ⚠️ AVISOS IMPORTANTES

### Direitos Autorais
**CRÍTICO:** As melodias das músicas do YouTube são protegidas por copyright.

**Solução Legal:**
1. Ferramentas que criamos são para **análise educacional**
2. Usuário **extrai e transcreve manualmente**
3. Resultado final é **interpretação/recriação** (fair use)
4. Para uso comercial: buscar licenças ou criar melodias originais

**Alternativa Segura:**
- Criar melodias **originais inspiradas** no estilo 8-bit
- Usar progressões de acordes genéricas (não protegidas)
- Melodias de domínio público (antigas >70 anos)

### Qualidade da Extração
- Librosa NÃO é 100% preciso
- Requer ajuste manual
- Músicas complexas precisam simplificação
- Múltiplas vozes = escolher apenas melodia principal

---

## 🎸 EXEMPLOS SINTÉTICOS (Demonstração)

### Exemplo: Melodia 8-bit Genérica (Tipo Power Rangers)

```javascript
const MUSIC_PHASE_1_DEMO = {
    title: "8-bit Epic Theme (Demo)",
    tempo: 140,
    synth_config: {
        oscillator: { type: 'square' },
        envelope: { attack: 0.005, decay: 0.1, sustain: 0.3, release: 0.1 }
    },
    notes: [
        // Progressão épica genérica
        { note: "E5", duration: "8n" },
        { note: "E5", duration: "8n" },
        { note: "F5", duration: "8n" },
        { note: "G5", duration: "4n" },
        { note: "E5", duration: "8n" },
        { note: "D5", duration: "8n" },
        { note: "C5", duration: "4n" },
        { note: "C5", duration: "8n" },
        { note: "D5", duration: "8n" },
        { note: "E5", duration: "4n." },
        { note: "D5", duration: "8n" },
        { note: "D5", duration: "2n" }
        // ... repetir/variar
    ],
    loop: true
};
```

---

## 🔥 PRIORIDADES DE IMPLEMENTAÇÃO

### MUST HAVE (Obrigatório)
1. ✅ Integrar Tone.js no index.html
2. ✅ Sistema de troca de música por fase
3. ✅ Script extract_melody.py funcional
4. ✅ Pelo menos 1 música exemplo funcionando

### SHOULD HAVE (Importante)
5. ✅ 6 melodias extraídas (simplificadas)
6. ✅ Synth configs otimizados por fase
7. ✅ Documentação completa

### NICE TO HAVE (Bônus)
8. ⭐ Visualizador de forma de onda
9. ⭐ Editor de melodia in-browser
10. ⭐ Efeitos (reverb, delay) por fase

---

## 🎯 CRITÉRIOS DE SUCESSO

✅ **Sistema funciona:** Música muda a cada fase
✅ **Performance:** <5ms latência, 60 FPS mantido
✅ **Usabilidade:** Fácil adicionar novas músicas
✅ **Qualidade:** Sons 8-bit autênticos
✅ **Documentação:** Completa e clara
✅ **Legal:** Processo respeita direitos autorais

---

## 📚 REFERÊNCIAS TÉCNICAS

### Tone.js
- Docs: https://tonejs.org/docs/
- Synth Guide: https://tonejs.org/docs/14.7.77/Synth
- Part/Sequence: https://tonejs.org/docs/14.7.77/Part
- Transport: https://tonejs.org/docs/14.7.77/Transport

### Librosa
- Pitch Detection: https://librosa.org/doc/main/generated/librosa.piptrack.html
- Tempo Detection: https://librosa.org/doc/main/generated/librosa.beat.beat_track.html
- Note Conversion: https://librosa.org/doc/main/generated/librosa.hz_to_note.html

### Web Audio
- Oscillator Types: https://developer.mozilla.org/en-US/docs/Web/API/OscillatorNode/type
- ADSR Envelope: https://en.wikipedia.org/wiki/Envelope_(music)

---

## 🎸 COMANDOS PARA FKT

```bash
# Criar estrutura de pastas
mkdir -p /home/thiago/projetos/natal/tools

# Navegar para projeto
cd /home/thiago/projetos/natal

# Criar scripts
# (FKT vai criar os arquivos)

# Testar extração (após criação)
# ./tools/download_music.sh "URL"
# python3 tools/extract_melody.py "audio.wav"
```

---

## 💀 MODO DOOM ATIVADO - EXECUÇÃO DEVASTADORA

**MENTALIDADE:**
- Zero bugs
- Código limpo
- Documentação perfeita
- Performance brutal
- UX impecável

**ENERGIA:**
- ∞ KAMEHAMEHAAAA
- Ódio a bugs: -999,999,999,999
- Proatividade: MÁXIMA
- Brotherhood: ETERNAL

---

🔥 **BORA DESGRAÇAR COM MÚSICAS ÉPICAS!** 🔥

💀👑 **NEXUS PRIME - I WALK BESIDE YOU!** 👑💀
