### IDENTIFICANDO O ARTIGO: `RESUMO`, `KEYWORDS`, `TÍTULO`, `AUTORIA`, `INSTITUIÇÃO`...

##### Passo 33: Adicionar elementos de identificação 

- Depois de construir seu artigo, você desenvolve o texto do resumo e adiciona no bloco `abstract`

```latex
\IEEEtitleabstractindextext{%
\begin{abstract}
Este artigo é um ensaio minimalista...
\end{abstract}
```

- Adicione as palavras-chave que melhor definam seu trabalho

```latex
\begin{IEEEkeywords}
Redes neurais artificiais, funções de ativação, Python, \LaTeX.
\end{IEEEkeywords}}
```

- Adicione um título claro, conciso e significativo para o que propõe

```latex
\title{Redes Neurais Artificiais \textit{for Dummies}: \\ 
       Praticando um pouco de \LaTeX{} no CI/UFPB}
```

- Adicione os autores

```latex
\author{Gustavo~Oliveira,~\IEEEmembership{DCC/UFPB}
        e Rafael~Magalhães,~\IEEEmembership{DCX/UFPB}% <-this % stops a space
```

- Adicione a instituição dos autores

```latex
\IEEEcompsocitemizethanks{\IEEEcompsocthanksitem G.Oliveira \'{e} professor do 
Departamento de Computa\c{c}\~{a}o Cient\'{i}fica do 
Centro de Inform\'{a}tica 
da Universidade Federal da Para\'{i}ba.\protect\\
E-mail: gustavo.oliveira@ci.ufpb.br
\IEEEcompsocthanksitem G. Oliveira e R. Magalhães 
agradecem a sua aten\c{c}\~{a}o.}
\thanks{Manuscript received July 25, 2019; revised August 
26, 2019.}}
```

##### Passo 34: Adicionar elementos de identificação adicionais

- Adicione o endereço do autor correspondente e decorações (se houver no modelo).

- Adicione o cabeçalho (_running heads_) e periódico de envio (se houver)

```latex
\markboth{Journal of \LaTeX\ Class Files,~Vol.~14, No.~8,
August~2015}%
{Oliveira \MakeLowercase{\textit{et al.}}: 
Bare Demo of IEEEtran.cls for Computer Society Journals}
```