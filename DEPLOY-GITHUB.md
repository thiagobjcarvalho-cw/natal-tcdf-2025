# 🚀 Deploy para GitHub

Guia para subir o projeto para GitHub.

---

## 📋 Pré-requisitos

```bash
# Verificar se git está instalado
git --version

# Configurar git (se necessário)
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

---

## 🔧 Inicializar Repositório

```bash
# Navegar até a pasta do projeto
cd /home/thiago/projetos/natal

# Inicializar repositório
git init

# Adicionar todos os arquivos (exceto .gitignore)
git add .

# Criar commit inicial
git commit -m "feat: projeto completo Natal TCDF 2025

- 6 telas interativas (Initial, Homenagem, Plantão, Heróis, Jogo, Conclusão)
- Jingle Bells completo (106 notas, Web Audio API)
- Jogo Bug Hunters (3 fases + boss)
- Performance otimizada (+50% FPS mobile, -62% memória)
- High score localStorage
- Suporte ENTER para navegação
- Zero dependências (HTML5 puro)"
```

---

## 🌐 Criar Repositório no GitHub

1. Acesse: https://github.com/new
2. **Repository name:** `natal-tcdf-2025`
3. **Description:** `🎄 Mensagem de Natal TCDF 2025 - Experiência interativa com jogo arcade`
4. **Visibility:** Public ou Private (sua escolha)
5. **NÃO** marcar "Initialize with README" (já temos)
6. Click em **"Create repository"**

---

## 📤 Push para GitHub

```bash
# Adicionar remote (substitua SEU_USUARIO pelo seu username GitHub)
git remote add origin https://github.com/SEU_USUARIO/natal-tcdf-2025.git

# Renomear branch para main (se necessário)
git branch -M main

# Push inicial
git push -u origin main
```

---

## 🌍 Habilitar GitHub Pages

1. No repositório GitHub, vá em **Settings**
2. No menu lateral, click em **Pages**
3. Em **Source**, selecione:
   - Branch: `main`
   - Folder: `/ (root)`
4. Click em **Save**
5. Aguarde ~1 minuto
6. Seu site estará em: `https://SEU_USUARIO.github.io/natal-tcdf-2025/`

---

## 🔄 Atualizações Futuras

```bash
# Após fazer alterações
git add .
git commit -m "tipo: descrição breve"
git push

# Tipos de commit:
# feat: nova funcionalidade
# fix: correção de bug
# perf: melhoria de performance
# docs: documentação
# style: formatação/estilo
```

---

## 📦 Estrutura que será commitada

```
natal-tcdf-2025/
├── .gitignore           ← Ignora backup/ e fkt-master/
├── README.md            ← Documentação principal
├── STATUS.md            ← Status detalhado
├── PLANO-EVOLUCAO.md    ← Roadmap
├── index.html           ← Aplicação (2140 linhas)
├── tree.png             ← Asset (1.6MB)
└── old/
    └── plantao-da-globo.mp3
```

**Ignorados:**
- `backup/` (versões antigas)
- `fkt-master/` (experimentos)

---

## ⚠️ IMPORTANTE

### tree.png (1.6MB)

Arquivo grande! GitHub aceita até 100MB, mas recomenda-se < 50MB.

**Opções:**

1. **Manter como está** (funciona, mas lento)
2. **Comprimir** antes do push:
   ```bash
   # Usar https://tinypng.com ou squoosh.app
   # Reduzir para ~200KB
   ```
3. **Usar Git LFS** (para arquivos grandes):
   ```bash
   git lfs install
   git lfs track "*.png"
   git add .gitattributes
   git commit -m "chore: add LFS for images"
   ```

---

## ✅ Checklist Final

- [ ] README.md atualizado
- [ ] .gitignore criado
- [ ] Commit inicial feito
- [ ] Repositório criado no GitHub
- [ ] Push realizado
- [ ] GitHub Pages habilitado
- [ ] Site funcionando online

---

## 🎯 Exemplo de URL Final

**Repositório:** `https://github.com/seu-usuario/natal-tcdf-2025`

**Site ao vivo:** `https://seu-usuario.github.io/natal-tcdf-2025/`

---

## 🆘 Troubleshooting

### "Large files detected"
```bash
# Se tree.png for rejeitado:
# Opção 1: Comprimir (recomendado)
# Opção 2: Usar Git LFS (ver acima)
```

### "Permission denied"
```bash
# Configurar SSH ou usar HTTPS com token
# Ver: https://docs.github.com/pt/authentication
```

### GitHub Pages não funciona
- Verificar se index.html está na raiz
- Aguardar 1-2 minutos após habilitar
- Verificar Actions tab (deploy automático)

---

**Pronto para deploy!** 🚀

Após push, compartilhe: `https://seu-usuario.github.io/natal-tcdf-2025/`
