# ASE — Git e fundamentos de CI/CD

Este guia usa o repositório `MEI` e o ficheiro `ASE/Notes/git.md` como laboratório. Os exercícios são progressivos: executa um treino de cada vez e verifica o resultado antes de avançar. Os comandos apresentados são instruções para a prática; não foram executados automaticamente para criar commits, branches ou publicações.

## 1. Onde executar os comandos

No terminal PowerShell:

```powershell
cd C:\Users\xiaro\Desktop\MEI
git rev-parse --show-toplevel
git status
```

`cd` muda a pasta actual do terminal. `git rev-parse --show-toplevel` mostra a raiz do repositório Git: neste caso, `C:/Users/xiaro/Desktop/MEI`. A diferença entre barras não significa que seja outra pasta.

A raiz contém a pasta interna `.git`, onde Git guarda o histórico e outras informações. `ASE`, `Notes` e as outras cadeiras são pastas dentro do mesmo repositório; não precisam de `git init`. Uma branch pertence ao repositório inteiro, não apenas a uma cadeira.

Um caminho relativo é interpretado a partir da pasta actual. Todos os comandos deste guia pressupõem que estás em `MEI`; daí usarmos `ASE/Notes/git.md`.

### Porque vamos evitar `git add .` nos treinos

O ponto significa a pasta actual. Na raiz de `MEI`, `git add .` prepara alterações, adições e remoções em todas as subpastas, respeitando as regras de exclusão aplicáveis. Pode incluir ficheiros de outras cadeiras que não pretendias juntar ao exercício.

```powershell
git add ASE/Notes/git.md
```

Este comando selecciona apenas o estado actual desse ficheiro. Se voltares a editá-lo, as novas alterações precisam de outro `git add` para entrar no próximo commit.

## 2. O modelo que explica os comandos

| Elemento | O que é | Porque interessa |
| --- | --- | --- |
| Directório de trabalho | Os ficheiros que vês e editas | Uma alteração guardada no editor ainda não é um commit. |
| Staging area, ou índice | O conteúdo seleccionado para o próximo commit | Permite escolher o que pertence à mesma alteração lógica. |
| Commit | Um registo de uma versão, com metadados e referências aos seus antecessores | Permite recuperar versões e relacionar uma execução de CI com alterações concretas. |
| Branch | Um nome que aponta para um commit e avança quando crias commits nessa branch | Permite desenvolver e integrar linhas de trabalho. |
| `HEAD` | Normalmente indica a branch em que estás | Determina onde serão registados os próximos commits. |
| Remoto | Uma configuração local que identifica outro repositório por URL | `origin` é um nome convencional, não uma palavra que signifique necessariamente GitHub. |
| `origin/main` | Referência local ao último estado conhecido da `main` do remoto | Pode estar desactualizada até executares `fetch`. |
| Upstream | Branch associada à tua branch local para sincronização | Permite normalmente usar `push` e `pull` sem indicar o destino. |

Fluxo habitual:

```text
Editar e guardar → git add → git commit → git push
                    índice    histórico local   repositório remoto
```

`commit` não envia nada para a Internet. `push` envia commits, não alterações que só existem no editor ou no índice. Git guarda versões dos ficheiros acompanhados; pastas vazias não são acompanhadas por si próprias.

Uma flag é uma opção de um comando. Aprende-a associada ao seu efeito, não como uma lista isolada: `-c` em `switch` cria uma branch; `--staged` em `diff` selecciona a comparação com o índice. A mesma letra pode ter outro significado noutro comando.

## 3. Treino 1 — preparar e registar estas notas

Objectivo: observar a passagem do ficheiro de trabalho para o índice e depois para o histórico.

A escrita deste guia já constitui a primeira alteração. Na branch `main`, executa:

```powershell
git status
git diff -- ASE/Notes/git.md
git add ASE/Notes/git.md
git diff --staged -- ASE/Notes/git.md
git status
git commit -m "ASE: adiciona guia de Git e CI/CD"
git status
git log -3 --oneline
```

Executa por etapas, sem copiar tudo de uma vez:

1. Antes de `add`, `status` deve mostrar o ficheiro modificado e ainda não preparado.
2. `diff` compara o ficheiro de trabalho com o índice. Deves ver as alterações deste guia.
3. Depois de `add`, `diff --staged` compara o índice com `HEAD`: mostra o conteúdo que será incluído no commit.
4. `commit -m` cria o commit com a mensagem indicada; `-m` evita abrir um editor para a mensagem.
5. No fim, o ficheiro deixa de aparecer como modificado, desde que não o tenhas editado entretanto. O `status` pode indicar commits por enviar.
6. `log -3 --oneline` mostra até três commits, um por linha. O teu deve aparecer primeiro.

O separador `--` em `diff` indica que o que vem a seguir é um caminho. Evita ambiguidades entre nomes de ficheiros e nomes de branches.

Pergunta de controlo: depois do commit, antes de `push`, o GitHub já recebeu o guia? Não: o commit existe apenas localmente.

Se `commit` pedir uma identidade, consulta primeiro:

```powershell
git config user.name
git config user.email
```

Se estiverem por configurar, define no repositório o teu nome e endereço, substituindo os exemplos:

```powershell
git config user.name "O teu nome"
git config user.email "O teu endereço de email"
```

Não precisas de publicar este commit para continuar os treinos locais.

## 4. Treino 2 — criar uma branch e perceber a mudança de versões

Pré-condição: treino 1 concluído e directório de trabalho limpo. Se houver alterações de outras cadeiras, trata-as separadamente antes de mudar de branch. As alterações não registadas podem acompanhar a mudança; uma branch não as guarda automaticamente.

```powershell
git status
git branch
git switch -c ase/treino-git
```

`branch` lista as branches locais; o asterisco indica a actual. `switch -c` cria `ase/treino-git` a partir do commit actual e muda para ela. A barra no nome é apenas uma convenção de organização: não limita a branch à pasta `ASE`.

No fim deste ficheiro, na secção «Diário dos treinos», substitui:

```text
Estado do treino: por iniciar.
```

por:

```text
Estado do treino: primeiro commit numa branch.
```

Guarda o ficheiro e executa:

```powershell
git diff -- ASE/Notes/git.md
git add ASE/Notes/git.md
git commit -m "ASE: regista primeiro treino numa branch"
git log -3 --oneline
git switch main
```

Observa o diário no editor: deve voltar a mostrar `por iniciar`. Se o editor não actualizar imediatamente, reabre o ficheiro sem guardar por cima da versão que Git acabou de colocar.

```powershell
git switch ase/treino-git
```

Agora reaparece o texto do treino. Não desapareceu trabalho: Git colocou no directório de trabalho a versão correspondente a cada branch.

Pergunta de controlo: o commit da experiência alterou a `main`? Não. As branches apontam agora para commits diferentes.

## 5. Treino 3 — comparar e integrar

Pré-condição: treino 2 concluído, sem alterações pendentes. Mantém a `main` sem novos commits durante este exercício.

```powershell
git diff main ase/treino-git -- ASE/Notes/git.md
git log --oneline main..ase/treino-git
git switch main
git merge ase/treino-git
git log --oneline --graph --all -8
```

- `diff` compara o conteúdo nas pontas das duas branches.
- `log main..ase/treino-git` mostra os commits alcançáveis da branch de treino que não são alcançáveis de `main`; aqui deve mostrar o commit da experiência.
- `merge` integra a branch indicada na branch actual. Por isso mudamos primeiro para `main`.
- `--graph` desenha as ligações do histórico; `--all` inclui as referências locais e remotas conhecidas; `-8` limita a listagem a oito commits.

Neste cenário, Git deve anunciar um **fast-forward**: `main` era antecessora da branch de treino e pode simplesmente avançar até ao mesmo commit. Não é necessário criar um commit de merge.

Depois da integração:

```powershell
git branch -d ase/treino-git
```

`-d` elimina a referência da branch com uma verificação de integração. Os commits continuam alcançáveis através de `main`. Não uses `-D` para ultrapassar uma recusa sem compreender o motivo: essa opção força a eliminação da referência.

## 6. Treino 4 — retirar uma alteração do índice

Objectivo: distinguir o ficheiro guardado da selecção para o próximo commit.

Com o trabalho anterior registado, acrescenta ao diário:

```text
Nota temporária: treino de staging.
```

Guarda e executa:

```powershell
git add ASE/Notes/git.md
git diff -- ASE/Notes/git.md
git diff --staged -- ASE/Notes/git.md
git restore --staged ASE/Notes/git.md
git status
git diff -- ASE/Notes/git.md
```

Depois de `add`, o primeiro `diff` não mostra essa alteração porque o ficheiro coincide com o índice. O segundo mostra-a porque o índice difere do último commit.

`restore --staged` repõe a entrada do índice a partir de `HEAD`, mantendo o ficheiro de trabalho. A nota continua no editor, mas deixou de estar seleccionada para o commit.

Para terminar, apaga manualmente apenas a linha temporária e guarda. Se essa era a única alteração, `git status` deve voltar a indicar um directório de trabalho limpo.

### Outra operação: descartar alterações locais

```powershell
git restore ASE/Notes/git.md
```

Sem `--staged`, `restore` repõe o ficheiro de trabalho a partir do índice. Descarta alterações não preparadas nesse ficheiro. Se tinhas preparado uma versão intermédia, é essa versão que reaparece, não necessariamente a do último commit.

Este comando é uma referência, não um passo obrigatório do treino. Usa-o apenas quando pretendes perder as alterações não preparadas do ficheiro. Git normalmente não permite recuperar texto que nunca foi guardado num commit ou noutro mecanismo de preservação.

## 7. Treino 5 — provocar e resolver um conflito local

Objectivo: compreender um merge com histórias divergentes. Tudo acontece em branches de treino e apenas neste ficheiro.

Pré-condição: treinos anteriores concluídos, em `main`, sem alterações pendentes. Os nomes abaixo devem estar disponíveis.

```powershell
git switch main
git switch -c ase/conflito-base
```

No diário, substitui a linha `Estado do treino:` por:

```text
Estado do treino: base do conflito.
```

```powershell
git add ASE/Notes/git.md
git commit -m "ASE: prepara base do conflito"
git switch -c ase/conflito-alternativa
```

Na mesma linha, escreve `Estado do treino: proposta alternativa.` e guarda:

```powershell
git add ASE/Notes/git.md
git commit -m "ASE: escreve proposta alternativa"
git switch ase/conflito-base
```

Agora escreve nessa mesma linha `Estado do treino: proposta principal.` e guarda:

```powershell
git add ASE/Notes/git.md
git commit -m "ASE: escreve proposta principal"
git merge ase/conflito-alternativa
git status
```

As duas branches alteraram a mesma linha de maneiras diferentes desde o antecessor comum. Git deve comunicar um conflito. Os commits continuam intactos; a integração está por concluir.

No diário, encontrarás marcadores semelhantes a:

```text
    <<<<<<< HEAD
Estado do treino: proposta principal.
    =======
Estado do treino: proposta alternativa.
    >>>>>>> ase/conflito-alternativa
```

Os marcadores estão indentados neste exemplo apenas para evitar que a verificação do próprio guia os interprete como um conflito pendente. Num conflito real podem aparecer no início da linha. `HEAD` representa aqui a versão da branch actual. A parte inferior representa a branch que estás a integrar. O separador divide as propostas; não é conteúdo para conservar no documento.

Substitui o bloco inteiro, incluindo os marcadores, por:

```text
Estado do treino: conflito resolvido combinando as propostas.
```

Guarda e conclui:

```powershell
git diff --check
git add ASE/Notes/git.md
git commit -m "ASE: resolve conflito entre propostas"
git status
git log --oneline --graph --all -12
```

`diff --check` detecta, entre outros problemas, marcadores de conflito introduzidos e certos erros de espaços. Não prova que a decisão tomada está correcta. Tens de rever o conteúdo final. `add` assinala o ficheiro como resolvido; `commit` conclui o merge. Neste caso haverá um commit de merge com dois antecessores.

Se quiseres abandonar a integração enquanto o conflito ainda está pendente, a alternativa é `git merge --abort`. Não executes essa alternativa depois de concluíres o merge.

Para levar o resultado a `main` e limpar as branches, após concluir o conflito:

```powershell
git switch main
git merge ase/conflito-base
git branch -d ase/conflito-alternativa
git branch -d ase/conflito-base
```

## 8. Treino 6 — corrigir um commit preservando o histórico

Pré-condição: em `main`, sem alterações pendentes. Acrescenta ao diário a linha `Nota de teste: esta alteração será revertida.` e guarda.

```powershell
git add ASE/Notes/git.md
git commit -m "ASE: cria alteração para treino de revert"
git show --stat HEAD
git revert --no-edit HEAD
git log -3 --oneline
git status
```

`show --stat HEAD` resume os ficheiros alterados pelo último commit. `revert HEAD` cria outro commit com a alteração inversa; `--no-edit` aceita a mensagem automática sem abrir um editor.

A nota deve desaparecer. O commit original continua no histórico, acompanhado do commit que o reverte. Isto facilita a colaboração: quem já recebeu o commit original pode receber a correcção normalmente.

Executa este `revert` imediatamente após o commit de teste. `HEAD` significa o commit actual, não «o commit errado»; se avançares no histórico, passarás a reverter outro commit.

`reset` é diferente: pode deslocar a branch e, conforme as opções, alterar o índice e os ficheiros. Vamos estudá-lo depois de dominares estes exercícios. `reset --hard` pode descartar alterações acompanhadas; não é um substituto habitual de `revert` para commits partilhados.

## 9. Sincronização: fetch, pull e push

O remoto deste repositório é `https://github.com/jpx2026/MEI.git`. Para consultar a configuração:

```powershell
git remote -v
git branch -vv
```

`-v` mostra as URLs do remoto. `-vv` mostra informação adicional das branches, incluindo o upstream quando existe.

### Primeiro consultar, depois decidir

```powershell
git fetch origin
git status
git log --oneline main..origin/main
git log --oneline origin/main..main
```

`fetch` obtém objectos e actualiza referências do remoto, sem integrar automaticamente os commits na tua branch nem substituir os teus ficheiros de trabalho.

A primeira listagem mostra commits conhecidos da `main` remota que faltam na `main` local. A segunda mostra os commits locais que faltam na referência remota. É normal a primeira estar vazia e a segunda listar os exercícios ainda não publicados.

### Receber alterações

Em `main`, com directório de trabalho limpo:

```powershell
git pull --ff-only
```

`pull` obtém alterações e tenta integrá-las. A integração pode depender das opções e configuração: não assumes que significa sempre criar um merge.

`--ff-only` permite apenas avançar sem divergência. Se ambas as branches tiverem commits exclusivos, recusa integrar: analisa o histórico e decide como combinar o trabalho. Não resolvas essa recusa com um push forçado.

### Publicar alterações

Depois de rever os commits locais e integrar eventuais alterações remotas:

```powershell
git push
```

Na `main` deste repositório já existe associação a `origin/main`. Uma branch nova pode precisar de:

```powershell
git push -u origin ase/minha-alteracao
```

Este é um exemplo para uma branch que exista localmente. `-u` configura o upstream; nos envios seguintes podes normalmente usar apenas `git push` nessa branch. Uma política de protecção pode impedir envios directos para `main` e exigir um pedido de integração.

## 10. Da branch ao pedido de integração

Um **pull request** no GitHub, ou **merge request** no GitLab, propõe integrar uma branch noutra. É uma funcionalidade da plataforma; não é o comando `git pull`.

Num treino remoto futuro:

1. Em `main` actualizada e limpa, cria `ase/treino-pr` com `git switch -c ase/treino-pr`.
2. Altera apenas o diário, revê a alteração, prepara o ficheiro e cria um commit.
3. Publica a branch com `git push -u origin ase/treino-pr`.
4. No GitHub, abre um pull request com destino `main` e origem `ase/treino-pr`.
5. Revê a diferença e os resultados das verificações disponíveis. A ausência de verificações não significa que os testes passaram.
6. Integra pelo GitHub quando estiver pronto, segundo as regras do repositório.
7. Localmente, executa `git switch main`, `git pull --ff-only` e verifica o diário.

Não faças também o merge local antes de praticar a integração pelo GitHub: são dois percursos diferentes para o mesmo objectivo. Se a plataforma usar squash, reúne alterações num novo commit; nesse caso `git branch -d ase/treino-pr` pode recusar a limpeza porque os commits originais não são antecessores de `main`. Compara o conteúdo e compreende o histórico antes de decidir eliminar a branch.

## 11. CI/CD: o que Git permite e o que a automação acrescenta

**CI — Continuous Integration, ou integração contínua:** integrar alterações frequentemente e verificá-las automaticamente. Pode envolver compilar, executar testes e analisar o código. Integrações pequenas e frequentes reduzem o tempo durante o qual alterações incompatíveis evoluem separadamente; as verificações dão informação rápida sobre problemas.

**Continuous Delivery — entrega contínua:** manter o software validado e preparado para publicação. A publicação em produção pode exigir uma decisão humana.

**Continuous Deployment — publicação contínua:** publicar automaticamente em produção as alterações que satisfaçam as verificações e regras definidas.

CI não exige que cada alteração seja publicada. Um `push` também não cria uma pipeline por si só: precisa de existir uma ferramenta de automação configurada para reagir ao evento.

```text
Branch → commit → push → pedido de integração → verificações e revisão
                                                     ↓
                                              integração em main
                                                     ↓
                                      preparação e eventual publicação
```

Este é um fluxo possível. As verificações podem ocorrer tanto no push como no pedido de integração, e voltar a executar sobre o resultado integrado.

### Vocabulário para ler uma pipeline

| Termo | Significado e função |
| --- | --- |
| Pipeline / workflow | Processo automatizado com tarefas de verificação ou publicação. |
| Trigger / evento | Condição que inicia uma execução, como push, pedido de integração ou acção manual. |
| Job | Conjunto de passos executados num ambiente; tarefas independentes podem correr em paralelo. |
| Step | Operação dentro de uma tarefa, como obter o código ou executar testes. |
| Runner | Máquina ou ambiente que executa a tarefa. Não usa automaticamente os ficheiros nem as ferramentas do teu computador. |
| Checkout | Colocação da versão de código pretendida no ambiente de execução. |
| Build / compilação | Transformação do código num resultado executável ou distribuível, quando o projecto a exige. |
| Teste | Verificação de um comportamento esperado; o conjunto de testes tem cobertura limitada. |
| Lint | Análise de regras e problemas estáticos; não substitui testes de comportamento. |
| Artefacto | Resultado produzido pela execução, como um pacote ou relatório. |
| Ambiente | Destino ou contexto de execução, por exemplo testes, staging ou produção. Aqui staging é um ambiente de pré-produção, não o índice do Git. |
| Secret | Valor confidencial fornecido à automação, como uma credencial; não deve ser escrito no ficheiro versionado. |
| Deployment | Colocação de uma versão num ambiente onde será utilizada. |

Uma tarefa pode falhar porque um comando termina com um código de saída diferente de zero. Contudo, o resultado depende da configuração: uma pipeline pode tolerar determinadas falhas ou omitir tarefas. Verde significa que as verificações configuradas foram satisfeitas; não prova a ausência de todos os defeitos.

### Como isto se aplica ao nosso ficheiro

Para documentação, uma CI útil pode verificar links, regras de Markdown ou marcadores de conflito esquecidos. Não há aqui uma aplicação que precise de compilação ou publicação em produção. Estamos a aprender o fluxo com documentação antes de o aplicar ao código de ASE.

Em GitHub Actions, a configuração real fica em `.github/workflows/` na raiz do repositório. Um bloco YAML escrito neste Markdown é apenas documentação e não executa nada. Para uma pipeline real será necessário criar pelo menos esse ficheiro adicional; manter os exercícios limitados a `git.md` permite praticar Git, mas não activar CI remota.

Por agora, não foi criada nem activada uma pipeline. Quando avançarmos para essa fase, escolheremos uma verificação pequena, executá-la-emos localmente, configuraremos a automação e provocaremos uma falha deliberada para observar o diagnóstico.

Git e a plataforma têm funções distintas: Git guarda e combina versões; GitHub aloja o repositório e os pedidos de integração; GitHub Actions executa a automação configurada. Se a cadeira usar GitLab ou outra plataforma, os conceitos mantêm-se, mas mudam os ficheiros de configuração e a interface.

## 12. Versões, tags e rastreabilidade

Uma **tag** dá um nome a um ponto do histórico, por exemplo `v1.0.0`. Uma branch avança com novos commits; uma tag é usada como referência estável de uma versão. Tecnicamente pode ser alterada, mas mudar uma tag já publicada prejudica a confiança nesse nome.

Exemplo de treino futuro, após escolheres o commit a identificar:

```powershell
git tag -a ase-treino-v1 -m "Primeira versão do treino ASE"
git show ase-treino-v1
```

`-a` cria uma tag anotada, com metadados e mensagem. Sem indicar outro commit, identifica `HEAD`. Não executa nem publica uma aplicação.

O envio é explícito:

```powershell
git push origin ase-treino-v1
```

O `git push` habitual não envia necessariamente as tags. Uma pipeline pode reagir a tags se estiver configurada para isso.

**Rastreabilidade** é conseguir relacionar o que foi publicado com o commit, as verificações e o artefacto que lhe deram origem. Uma prática útil é validar um artefacto e promover esse mesmo resultado entre ambientes, evitando reconstruções diferentes sem controlo. Um identificador de commit ajuda a localizar a versão, mas a reprodução também depende das ferramentas, dependências e configuração utilizadas.

## 13. Referência rápida e sequência de aprendizagem

| Intenção | Comando |
| --- | --- |
| Consultar o estado | `git status` |
| Rever alterações não preparadas | `git diff -- ASE/Notes/git.md` |
| Preparar só as notas de ASE | `git add ASE/Notes/git.md` |
| Rever o próximo commit | `git diff --staged` |
| Registar a selecção | `git commit -m "Mensagem"` |
| Criar uma branch e mudar para ela | `git switch -c nome` |
| Mudar para uma branch existente | `git switch nome` |
| Integrar na branch actual | `git merge nome` |
| Consultar o histórico | `git log --oneline --graph --all` |
| Inspeccionar o commit actual | `git show HEAD` |
| Retirar o ficheiro do índice | `git restore --staged ASE/Notes/git.md` |
| Anular um commit através de outro | `git revert IDENTIFICADOR` |
| Actualizar o conhecimento do remoto | `git fetch origin` |
| Receber permitindo apenas avanço linear | `git pull --ff-only` |
| Enviar commits | `git push` |

Em `git revert IDENTIFICADOR`, substitui `IDENTIFICADOR` pelo identificador real do commit. Os nomes dos exemplos não são palavras especiais de Git.

Ordem proposta: treino 1 → treino 2 → treino 3 → treino 4 → treino 5 → treino 6 → sincronização → pedido de integração → pipeline real → versões e publicação. Não executes toda a documentação como um único script: há edições manuais e verificações entre comandos.

### Inicialização e clonagem: apenas quando necessário

Para obter um repositório existente noutro computador:

```powershell
git clone https://github.com/jpx2026/MEI.git
cd MEI
```

Executa `clone` na pasta que deverá conter a nova pasta `MEI`, não dentro da cópia actual. Obtém o histórico, configura `origin` e coloca a branch inicial no directório de trabalho. Não precisas de `init` nem, normalmente, de um `pull` imediatamente a seguir.

Para um projecto novo ainda sem Git, com um repositório remoto vazio já criado, o fluxo é `git init -b main`, seleccionar ficheiros, criar o primeiro commit, `git remote add origin URL` e `git push -u origin main`. `-b` define a branch inicial; substitui `URL` pelo endereço real. Não repitas este processo no `MEI`, que já está configurado.

## 14. Fontes oficiais

- [Livro Pro Git: fundamentos](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)
- [Livro Pro Git: branches e merges](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
- [Referência de git restore](https://git-scm.com/docs/git-restore)
- [Referência de git fetch](https://git-scm.com/docs/git-fetch)
- [Referência de git revert](https://git-scm.com/docs/git-revert)
- [GitHub Actions: componentes e funcionamento](https://docs.github.com/en/actions/get-started/understand-github-actions)
- [GitHub Actions: workflows](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflows)

## Diário dos treinos

Esta secção é o alvo das edições práticas. Nos treinos, altera o texto aqui, não os exemplos das secções anteriores.

Estado do treino: por iniciar.
