### ADICIONANDO ELEMENTOS PÓS-TEXTUAIS: `APÊNDICES`, `AGRADECIMENTOS`, `BIOGRAFIA`...

##### Passo 35: Adicionar apêndices

- Às vezes, você pode desejar adicionar apêndices em seu artigo para incluir informações detalhadas sobre derivação de um método, provas teóricas ou algo que seja muito intrincado para caber no corpo do texto principal. Em nosso template, isto pode ser feito com o comando `\appendices`. No texto, temos dois apêndices.

```latex
\appendices

\section{Algumas equações para praticar a escrita}

\section{Personalidades no estudo de RNAs}
```

- Para este template, ao invocar `\section` após `\appendices`, a seção é automaticamente formatada para o nome `APPENDIX X`. 

- **Suplemento:** No apêndice B, incluímos uma lista ordenada com o comando `\enumerate`, que ainda não havia aparecido em nosso tutorial. 

```latex
\begin{enumerate}
    \item Warren S. McCulloch ($\star$ 1868 - $\dagger$ 1969) \\ 
    \item Walter Pitts ($\star$ 1923 - $\dagger$ 1969) \\ 
    \item Frank Rosenblatt ($\star$ 1928 - $\dagger$ 1971) \\ 
\end{enumerate}
```

- Alguns caracteres especiais foram também adicionados: `\star` ($\star$) e `\dagger` ($\dagger$). Outros são: 

|expressão|resultado|
|:---:|:---:|
|`$\ast$`|$\ast$|
|`$\bullet$`|$\bullet$|
|`$\circ$`|$\circ$|
|`$\times$`|$\times$|
|`$\vee$`|$\vee$|
|`$\wedge$`|$\wedge$|
|`$\ddagger$`|$\ddagger$|

##### Passo 36: Adicionar agradecimentos


- Comumente, agradecimentos são adicionados ao final de um artigo em que se direcionam notas de reconhecimento por algum financiamento recebido por empresas, apoio fundacional, bolsas de estudo concedidas, auxílio técnico ou discussões com outros pesquisadores. Em nosso template, há duas maneiras aceitáveis. 

```latex
% use section* for acknowledgment
\ifCLASSOPTIONcompsoc
  % The Computer Society usually uses the plural form
  \section*{Acknowledgments}
\else
  % regular IEEE prefers the singular form
  \section*{Acknowledgment}
\fi
G.O. agradece a oportunidade de ministrar este mini-curso.
```

- O bloco `\if...\else...\fi` modifica o nome da seção condicionado à revista para onde o artigo será submetido. Em geral, o comando usado para este bloco é `\acks`.

##### Passo 37: Adicionar biografia e foto dos autores 

- Algumas revistas fazem uso de biografia, resumo curricular e foto dos autores, outras não. Neste template, temos as seguintes opções: 

	- Com foto: 
	
	```latex
	\begin{IEEEbiography}[{\includegraphics[width=1in,
	height=1.25in,clip,keepaspectratio]
	{figs/gustavo}}]{Gustavo Oliveira}
	```
	
	- Sem foto:

	```latex
\begin{IEEEbiographynophoto}{Gustavo Oliveira}
Prof. do DCC/CI/UFPB e pesquisador do LaMEP. \\
Visite-nos em: \url{lamep.ci.ufpb.br}.
\end{IEEEbiographynophoto}
\begin{IEEEbiographynophoto}{Rafael Magalhães}
Prof. do DCX/CCAE/UFPB e pesquisador no LaMEP/UFPB.
\end{IEEEbiographynophoto}
```