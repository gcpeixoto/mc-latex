% Conhecendo o \LaTeX: usos, dicas e práticas
% Gustavo Oliveira, gustavo.oliveira@ci.ufpb.br 
% LaMEP/DCC/CI/UFPB, lamep.ci.ufpb.br -- Atualizado em: jul/2019

# O que é \LaTeX?

## Definição
- Sistema tipográfico de alta qualidade que inclui recursos projetados para a produção de documentação técnica e científica. 

- Padrão para comunicação e publicação de documentos científicos. 

- Pronúncia: "la-ték" ou "lei-ték" (de _Lamport Tex_)

- Site oficial: https://www.latex-project.org

## História 

- _TeX_ + _Metafont_ (Donald Knuth, 1978) 

- _LaTeX2_  (Leslie Lamport, 1986)

- _LaTeX2e_  (1994)

- _LaTeX3_ (Mittelbach, Carlisle et al., em projeto)

## Distribuições 

- _TeX_: linguagem mais básica (mais usada por desenvolvedores)
- _LaTeX_: criou os "pacotes" (conjunto de instruções _TeX_). 
- _pdfTeX_: permitiu a criação de PDFs (links embutidos, metadados, tabela de conteúdo) diretamente a partir do TeX superando o workflow _DVI_ + _Postscript_
- _pdfLaTeX_: facilitador para _pdfTeX_ (recomendado)
- _xeTeX_ e _xeLaTeX_: criado para incorporar fontes modernas (e.g. _fontawesome_)
- _LuaTeX_: facilitador de macros\footnote{A linguagem Lua (https://www.lua.org) foi criada na PUC-RJ. Essa é do Brasil!}  

## Inspiração 

- Knuth vê um livro sobre inteligência artificial lá pelos idos de 1970...

- O livro havia sido produzido digitalmente: 0s e 1s...

- Knuth pensa: tipografia é organizar 0s = tinta e 1s = (não) tinta

- Knuth diz: _"As a computer scientist, I really identify with patterns of 0's and 1's; I ought to be able to do something about this."_

- Knuth estuda por alguns anos até que o _Tex_ começa a voar... 

Fonte: https://www.tug.org/whatis.html
   
## Características 

- Escrita de artigos, revistas, relatórios técnicos, livros e apresentações (como estes slides).

- Controle sobre documentos com estrutura complexa: seções, referências cruzadas, tabelas, figuras, etc.

- Escrita de fórmulas matemáticas complexas.

- Tipografia avançada de matemática com AMS-\LaTeX\footnote{AMS-\LaTeX é um pacote de matemática da _American Mathematical Society_}.

- Geração automática de bibliografias e índices.

- Tipografia multilíngue.

## WYSIWYG x WYSINWYG x WYSIWYM

- **WYSIWYG**: _"What you see is what you get"_
	- Documento formatado na tela como impresso no papel
	- e.g. Word, OpenOffice, Pages, etc.
- **WYSINWYG**: _"What you see is NOT what you get"_
	- Documento não é formatado na tela, requer compilação
	- e.g. LaTeX
- **WYSIWYM**: _"What you see is what you MEAN"_
	- Documento estruturado por marcações 
	- https://en.wikipedia.org/wiki/WYSIWYM
	- e.g. LyX: https://www.lyx.org

## Derivações e gracejos 

Veja variações desse jargão (fonte: Wikipedia):

- **WISIWIT**: _"what I see is what I type"_
- **WYSIAWYG**: _"what you see is ALMOST what you get"_
- **WYSINWYW**: _"what you see is not what you WANT"_, 
- **WYSIWYD**: _"what you see is what you deserve"_

## Um novo conceito 

- **WYSIPCTWOTCG**: _"what you see is pretty close to what other tools can get"_
- *WordTeX*: um tipo de Latex para Word
- https://www.andrew.cmu.edu/user/twildenh/wordtex/
- https://www.youtube.com/watch?v=jlX_pThh7z8

## Por que usar \LaTeX? 

- Várias vantagens perante processadores de texto
- De grande interesse científico 
- Vejamos algumas vantagens e desvantagens


# Algumas vantagens e desvantagens

## Aparência e estética ($\uparrow$)

- Produção de texto com altíssima qualidade
- Tipografia à beira da perfeição
- Exemplos: 
	- Sem problemas de justificação
	- Hifenização e _kerning_ controláveis

## Rapidez e portabilidade ($\uparrow$)

- Compila conteúdo com 100, 1000... figuras como se fossem 10
- Separação entre entrada e saída (fonte + compilação) 
- Documentos utilizáveis em diferentes plataformas

## Foco no conteúdo ($\uparrow$)

- Usuário evita alterações por chamarizes da interface;
- Evita-se a formatação "a todo tempo" (um negrito aqui... um sublinhado ali...)
- Atenção total à escrita em vez da formatação
- Probabilidade de formatação acidental quase nula. 

## Estabilidade ($\uparrow$)

- Pouco propenso a _bugs_, travamentos e outros problemas
- Forte arcabouço de projeto por cientistas da computação


## Uso exagerado (sintoma) ($\downarrow$)

- LaTeX não será sempre o mais indicado para um trabalho
- Postcard para o Instagram? Use algo como canva.com, por exemplo

## Curva de aprendizagem ($\downarrow$)

- Leva tempo para se acostumar com o _LaTeX_ 
- Requer um nível de prática para se habituar 
- Um trabalho "sério" dá trabalho (mas vale o esforço)

## Baixa adesão ($\downarrow$)

- Nem toda gráfica local ou publicadora manipula LaTeX 
- Problemas com compatibilidade e configurações 
- Muitas revistas preferem texto processado por outros meios
- No mundo _TeX_, isso seria considerado "amadorismo" :) 


# Usos e práticas

## Equações

- Como ter isto?
$$
\dfrac{d\sigma}{d\cos(\theta)}(e^{+}e^{-}) \oplus
\left| \frac{1}{1 - \Delta\alpha} \right|^{2}
\times \iiint_{{\bf g} \in G(\mu)} ||{\bf g}|| \, d\kappa 
  \rightarrow \bar{f}
$$
- No \LaTeX é "simples" e "rápido":

```latex
\dfrac{d\sigma}{d\cos(\theta)}(e^{+}e^{-}) \oplus
\left| \frac{1}{1 - \Delta\alpha} \right|^{2}
\times \iiint_{{\bf g} \in G(\mu)} ||{\bf g}|| 
\, d\kappa \rightarrow \bar{f}
```

## Trilhas

- Para saber a respeito: \url{https://www.latex-project.org}

- Para aprender e praticar: 
	-  https://www.overleaf.com

- Para consultar e achar respostas:
	- https://en.wikibooks.org/wiki/LaTeX
	- https://tex.stackexchange.com/questions/

- Para se aprofundar e se especializar:
	- https://en.wikipedia.org/wiki/TeX

## Estou começando... 

- A "Apostila do Lenimar": 
	- http://www.mat.ufpb.br/lenimar/textos/breve21pdf.zip

- Procure tutoriais em Português (por exemplo):
	- http://www.ptep-online.com/ctan/lshort_port_br.pdf, por T. Oetiker
	- http://www.mat.ufmg.br/~regi/topicos/intlat.pdf
	- http://www.marcopolo.unir.br/images/downloads/material-extensao/curso_de_introducao_ao_latex.pdf

	
## Onde usar o que aprenderei?

- Basicamente qualquer tipo de documento
- Uma lista modesta:
	- TCCs, dissertações e teses (classe \texttt{memoir})
	- Artigos científicos e _white papers_ (classe \texttt{article})
	- Relatórios (classe \texttt{report})
	- CVs (muitas classes)
	- Provas (classe \texttt{exam})
	- Livros (classe \texttt{book})
	- Apresentações (classe \texttt{beamer})
	- Pôsteres (classe \texttt{baposter})
	- etc.

## Onde será bem mais útil? 

- Em eventos e palestras (este aqui é um exemplo)
- Em submissões de artigos para as principais casas publicadoras, tais como _Springer_, _Elsevier_, _IEEE_, _ASME_, etc.
- Em _cover letters_ e _VITAS_
- Em projetos de monitoria ou tutoria para confecção de listas de exercícios e provas
- Ao longo de toda sua vida em uma pós-graduação em ciências exatas (é raro não se deparar com LaTeX em algum momento)

## Distribuições e editores

- Distribuições mais conhecidas
	- Windows: MikTeX, https://miktex.org/
	- Linux: TeXLive, https://www.tug.org/texlive/
	- macOS: MacTeX, https://mactex.org/
- Editores 
	- TeXMaker, http://www.xm1math.net/texmaker/ (recomendado)
	- Veja lista: https://en.wikipedia.org/wiki/Comparison_of_TeX_editors 


## Repositório central

- *Com­pre­hen­sive TEX Archive Net­work (CTAN)*: lugar central para todos os materiais envolvendo TeX:
	- https://www.ctan.org/?lang=en
- Em 2017: 5378 pacotes; 2455 contribuintes
- Em 2019: 5719 pacotes; 2623 contribuintes


## Pacotes interessantes 

- Para pseudocódigos e algoritmos:
	- \texttt{algorithm}
- Para sintaxes de códigos:
	- \texttt{listings}, \texttt{minted}	
- Para caixas coloridas:
	- \texttt{tcolorbox}
- Para desenhos:
	- \texttt{tikz}, \texttt{pgf}
- Há centenas de muitos outros...


# Dicas gerais 

## Exercite-se 

- Use editores _online_
- Busque auxílio de colegas mais experientes
- Faça buscas na https://tex.stackexchange.com
- Tente instalar a ferramenta em seu computador

## Miscelânea

- Para gerar tabelas com rapidez
	- http://www.tablesgenerator.com

- Para experimentar: 
	- https://papeeria.com
	- https://authorea.com

- Para gerenciar bibliografia
	- http://bibdesk.sourceforge.net  
	- Veja http://www.bibtex.org
	
- Para lista de símbolos matemáticos:
	- Aqui tem basicamente todos de que você precisará: http://tug.ctan.org/info/symbols/comprehensive/symbols-a4.pdf

- Para renderizar equações para seu site: 
	- https://tex.s2cms.com

## cont. 

- Para explicar sua dúvida ao orientador:
	- http://alexeev.org/gmailtex.html
- Para iOS/Android
	- https://apps.texwriter.net
	- VerbTex

## Vídeos

- Donald Knuth's life story
	- https://www.youtube.com/playlist?list=PLVV0r6CmEsFzeNLngr1JqyQki3wdoGrCn
- Playlist da TUG Conference Brasil 2018
	- https://youtu.be/Nw_GE6yKo8E 

## Bibliografia complementar 

- Lamport, L.: [LaTeX: A Document Preparation System](https://www.amazon.com/LaTeX-Document-Preparation-System-2nd/dp/0201529831). Addison-Wesley, 1994. 
- Knuth, D. E.: [The TEXbook](https://www.amazon.com/TeXbook-Donald-Knuth/dp/0201134489/ref=pd_rhf_dp_s_pd_crcd_1_1/144-1182075-2730300?_encoding=UTF8&pd_rd_i=0201134489&pd_rd_r=4821f495-a73c-4943-b6ba-63b69c0d60de&pd_rd_w=XTMJV&pd_rd_wg=lYAbA&pf_rd_p=d17c2de0-cc1d-4b09-aad8-987099a21717&pf_rd_r=NTZY65477FA44ZTXER0M&psc=1&refRID=NTZY65477FA44ZTXER0M). Addison-Wesley, 1984.
- Mittelbach F., Goossens, M. et al.: [The LATEX Companion](https://www.amazon.com/LaTeX-Companion-Techniques-Computer-Typesetting/dp/0201362996). Addison-Wesley, 2004.

# Markdown

## Um pouco sobre Markdown 

- Uma linguagem de marcação bastante útil para renderizar equações e textos matemáticos
- https://www.markdownguide.org
- https://daringfireball.net/projects/markdown/

## Editores online 

- https://upmath.me
- https://stackedit.io


## Utilidades 

- Para e-mail:
	- https://markdown-here.com
 
- Para Github (especificação em _CommonMark_): 
	- https://github.github.com/gfm/

- Para livros: 
	- https://typora.io

- Para códigos interativos
	- https://colab.research.google.com
	- https://www.firstpythonnotebook.org/markdown/
	- https://rmarkdown.rstudio.com

## Aprofundamento 

- Jupyter notebook & markdown
	- https://jupyter.org/
	- https://www.youtube.com/watch?v=-F4WS8o-G2A&t=20s

- Motores de renderização 
	- https://www.mathjax.org
	- https://katex.org

- _pandoc_:
	- https://pandoc.org
	- https://www.youtube.com/watch?v=N31E_NZYQQY

- _ipypublish_: 
	- https://chrisjsewell.github.io/ipypublish/

# _Hands-on_: Primeiro projeto 

## Overleaf

- Uma plataforma excelente para LaTeXistas
	- https://overleaf.com 
- Fundiu-se com o ShareLatex para produzir o _Overleaf v2_
- Vantagens
	- Colaboração em tempo real 
	- Histórico de mudanças 
	- Facilidade de uso 
	- Nenhuma preocupação com instalação de ferramentas
	- Gratuito para o básico (pago na versão Pro)
	- Única ameaça: _queda de internet_...
	- Saída: manter um sistema operando localmente

- Existem alternativas ao Overleaf? 
	- Mais equivalente [?]: https://authorea.com
	

## Meu primeiro artigo

- _Redes Neurais Artificiais for Dummies: praticando um pouco de LaTeX no CI/UFPB_
- Simulando uma submissão para a IEEE (Computer Science)

	