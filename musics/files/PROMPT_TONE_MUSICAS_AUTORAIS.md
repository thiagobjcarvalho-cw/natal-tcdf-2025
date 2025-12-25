# PROMPT: Convertendo Suas Músicas Autorais para Tone.js

## Instrução Principal

Você tem **[N] músicas autorais** que quer transformar em **síntese Web Audio com Tone.js**. Este prompt orienta o processo completo.

---

## PASSO 1: ANÁLISE DA MÚSICA ORIGINAL

### 1.1 Extraia a estrutura básica:
- **Tonalidade**: Qual é? (Ex: C maior, Em menor, G7)
- **Tempo (BPM)**: Quantos beats por minuto?
- **Compasso**: 4/4, 3/4, 6/8?
- **Duração total**: Quantos segundos/minutos?
- **Seções**: Intro, verso, pré-refrão, refrão, bridge, outro?

### 1.2 Transcreva a MELODIA PRINCIPAL:
Nota por nota (use nomenclatura: C4, D4, E4, F#4, etc):
```
VERSO 1: C4 (1 beat) → E4 (1 beat) → G4 (2 beats) → A4 (1 beat) → G4 (1 beat)
REFRÃO: G4 (0.5) → A4 (0.5) → B4 (1) → C5 (2) → [pausa 1 beat]
```

### 1.3 Identifique:
- **Harmonia base** (progressão de acordes)
- **Ritmo/padrão** (síncopas, pausas características)
- **Dinâmica** (partes altas, baixas, crescendos)
- **Timbre desejado** (lead brilhante, baixo grave, percussão)

---

## PASSO 2: ESTRUTURE OS DADOS EM JSON

Organize suas músicas num formato reutilizável:

```javascript
const MINHAS_MUSICAS = {
  "musica_1": {
    title: "Nome da Música",
    tonalidade: "C maior",
    tempo: 120,
    duracao_segundos: 95,
    sections: {
      intro: {
        tempo_inicio: 0,
        tempo_fim: 8,
        descricao: "Intro com pad atmosférico"
      },
      verso: {
        tempo_inicio: 8,
        tempo_fim: 24,
        descricao: "Verso principal"
      },
      refrão: {
        tempo_inicio: 24,
        tempo_fim: 40,
        descricao: "Refrão energético"
      }
    },
    
    melodia_principal: [
      { nota: "C4", duracao: 1, tempo_inicio: 0 },
      { nota: "E4", duracao: 1, tempo_inicio: 1 },
      { nota: "G4", duracao: 2, tempo_inicio: 2 },
      { nota: "A4", duracao: 1, tempo_inicio: 4 },
      { nota: "G4", duracao: 1, tempo_inicio: 5 },
      // ... todas as notas
    ],
    
    harmonia: [
      { acordes: "C", tempo_inicio: 0, duracao: 4 },
      { acordes: "Am", tempo_inicio: 4, duracao: 4 },
      { acordes: "F", tempo_inicio: 8, duracao: 4 },
      { acordes: "G", tempo_inicio: 12, duracao: 4 }
    ],
    
    ritmo: {
      padrao: "4/4",
      caracteristicas: "Swing leve, pontuação no 2 e 4"
    }
  }
}
```

---

## PASSO 3: IMPLEMENTAR EM TONE.JS

### 3.1 Setup básico:

```javascript
// Inicializar Tone.js
async function initTone() {
  await Tone.start();
  Tone.Master.volume.value = -8;
  
  // Seu synth personalizado
  const synth = new Tone.PolySynth(Tone.Synth, {
    oscillator: { type: 'triangle' }, // ou 'square', 'sawtooth', 'sine'
    envelope: {
      attack: 0.005,
      decay: 0.1,
      sustain: 0.3,
      release: 0.1
    }
  }).toDestination();
  
  return synth;
}
```

### 3.2 Converter durações para beat:

```javascript
function calcularDuracao(notaObj, bpm) {
  const beatMs = (60 / bpm) * 1000;
  const durationSec = (notaObj.duracao * beatMs) / 1000;
  return durationSec;
}

// Exemplo: nota com duracao 1 (uma semínima) em 120 BPM
// beatMs = (60/120)*1000 = 500ms
// durationSec = 1 * (500/1000) = 0.5 segundos
```

### 3.3 Tocar a melodia:

```javascript
async function tocarMusica(musica, synth) {
  const beatMs = (60 / musica.tempo) * 1000;
  const startTime = Date.now();
  
  for (const nota of musica.melodia_principal) {
    // Aguarde até o tempo correto
    const delayMs = (nota.tempo_inicio * beatMs) - (Date.now() - startTime);
    if (delayMs > 0) await new Promise(r => setTimeout(r, delayMs));
    
    // Toque a nota
    const durationSec = (nota.duracao * beatMs) / 1000;
    synth.triggerAttackRelease(nota.nota, durationSec);
  }
}
```

---

## PASSO 4: OTIMIZAÇÕES E EFEITOS

### 4.1 Adicionar seções com diferentes synths:

```javascript
const synth_lead = new Tone.Synth({
  oscillator: { type: 'square' },
  envelope: { attack: 0.01, decay: 0.15, sustain: 0.2, release: 0.1 }
}).toDestination();

const synth_pad = new Tone.Synth({
  oscillator: { type: 'triangle' },
  envelope: { attack: 0.2, decay: 0.3, sustain: 0.5, release: 0.3 }
}).toDestination();

const bass = new Tone.Synth({
  oscillator: { type: 'sine' },
  envelope: { attack: 0.01, decay: 0.2, sustain: 0.1, release: 0.15 }
}).toDestination();

// Usar conforme seção:
if (section === 'intro') {
  synth_pad.triggerAttackRelease(nota, dur);
} else if (section === 'verso') {
  synth_lead.triggerAttackRelease(nota, dur);
}
```

### 4.2 Adicionar reverb/efeitos:

```javascript
const reverb = new Tone.Reverb({
  decay: 2.5,
  wet: 0.3
}).toDestination();

synth_lead.connect(reverb);

// Ou usar Convolver para impulse response
const convolver = new Tone.Convolver({
  url: "seu-impulse-response.wav",
  wet: 0.5
}).toDestination();
```

### 4.3 Adicionar volume/dinâmica:

```javascript
const gainNode = new Tone.Gain(0.8).toDestination();
synth_lead.connect(gainNode);

// Crescendo automático
gainNode.gain.linearRampToValueAtTime(0.3, Tone.now() + 10);
```

---

## PASSO 5: ESTRUTURA FINAL DO ARQUIVO HTML

```html
<!DOCTYPE html>
<html>
<head>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/tone/14.8.49/Tone.js"></script>
</head>
<body>
  <button onclick="tocarMusica('musica_1')">Tocar Música 1</button>
  <button onclick="pararMusica()">Parar</button>

  <script>
    // 1. Seus dados de música
    const MINHAS_MUSICAS = { /* seu JSON aqui */ };
    
    // 2. Setup
    let synth;
    async function init() {
      await Tone.start();
      synth = new Tone.PolySynth(Tone.Synth, {
        oscillator: { type: 'triangle' },
        envelope: { attack: 0.005, decay: 0.1, sustain: 0.3, release: 0.1 }
      }).toDestination();
    }
    
    // 3. Função tocar
    async function tocarMusica(musicaId) {
      if (!synth) await init();
      const musica = MINHAS_MUSICAS[musicaId];
      // ... seu código de playback
    }
    
    // 4. Função parar
    function pararMusica() {
      synth.triggerRelease();
    }
  </script>
</body>
</html>
```

---

## PASSO 6: DICAS IMPORTANTES

### Conversão de durações (usa símbolos musicais):
```
'w' (whole) = 4 beats
'h' (half) = 2 beats
'qd' (quarter dotted) = 1.5 beats
'q' (quarter) = 1 beat
'e' (eighth) = 0.5 beats
's' (sixteenth) = 0.25 beats
```

### Frequências de referência (Hz):
```
C4=261.63, D4=293.66, E4=329.63, F4=349.23, G4=392.00, A4=440.00, B4=493.88
C5=523.25, D5=587.33, E5=659.25, F5=698.46, G5=783.99, A5=880.00, B5=987.77
```

### Troubleshooting:
- **Som muito silencioso?** → Aumentar `Tone.Master.volume.value` (ex: -6)
- **Notas cortadas?** → Aumentar `release` no envelope
- **Latência?** → Usar `Tone.now()` em vez de `Date.now()`
- **Não toca?** → Verificar se `await Tone.start()` foi chamado

---

## TEMPLATE PRONTO PARA COPIAR:

```javascript
const minha_musica_autorais = {
  "musica_original_1": {
    title: "Título",
    tempo: 120,
    melodia: [
      { nota: "C4", duracao: 1 },
      { nota: "D4", duracao: 1 },
      { nota: "E4", duracao: 2 },
      // ADICIONE TODAS AS SUAS NOTAS
    ]
  }
};

async function tocarMinhaMusica() {
  await Tone.start();
  const synth = new Tone.Synth({
    oscillator: { type: 'triangle' },
    envelope: { attack: 0.01, decay: 0.1, sustain: 0.3, release: 0.1 }
  }).toDestination();
  
  const musica = minha_musica_autorais["musica_original_1"];
  const beatMs = (60 / musica.tempo) * 1000;
  
  for (const nota of musica.melodia) {
    const durationSec = (nota.duracao * beatMs) / 1000;
    synth.triggerAttackRelease(nota.nota, durationSec);
    await new Promise(r => setTimeout(r, nota.duracao * beatMs));
  }
}
```

---

## PRÓXIMOS PASSOS

1. **Transcreva suas músicas** em formato JSON
2. **Teste com uma música simples** primeiro (Ex: 30 segundos)
3. **Ajuste envelopes** até soar bom
4. **Adicione efeitos** (reverb, delay, distortion)
5. **Implemente UI** (botões, progress bar, visualizador)
6. **Optimize** para browser (cache, web workers se necessário)

---

## RECURSOS OFICIAIS

- Tone.js Docs: https://tonejs.org/docs/
- Synth API: https://tonejs.org/docs/source/Synth.html
- Envelope Guide: https://tonejs.org/docs/api/Envelope
- Efeitos: https://tonejs.org/docs/api/Effect

---

**Pronto para converter suas 6 músicas autorais?** Comece transcrevendo uma música simples em JSON, depois me mostre para eu ajudar com a implementação final!