### TRABALHANDO NA SEÇÃO `MÉTODOS`...

##### Passo 13: Escrever a seção `Métodos`

- Copiar o conteúdo para esta seção do arquivo `conteudo.txt`.

```latex
\section{Métodos}
\label{sec:metodos}

\subsection{Limiar de excitação}

Um neurônio biológico dispara quando a soma dos impulsos que ele recebe 
ultrapassa seu limiar de excitação (\textit{threshold}) $\theta$. 
Matematicamente, podemos modelar um neurônio $k$ pelo seguinte par de equações: 
\begin{equation}
    v_k = b_k + \displaystyle \sum_{j=1}^m w_{kj} x_j 
\end{equation}
e
\begin{equation}
    y_k = \phi(v_k),
\end{equation}
em que
\begin{itemize}
    \item $x_1,x_2,\ldots,x_m$ são \textbf{sinais de entrada};
    \item $w_{k1},w_{k2},\ldots,w_{km}$ são \textbf{pesos sinápticos};
    \item $u_k$ é o \textbf{adicionador} ou \textbf{combinador linear}; 
    \item $b_k$ é o \textbf{bias}\footnote{O \textit{bias} é um parâmetro externo 
    de entrada $x_0$ e peso $w_{k0} = b_k$ que tem o efeito de aumentar (se positivo) 
    ou diminuir (se negativo) a entrada líquida da função de ativação.};
    \item $v_k$ é o \textbf{potencial de ativação};
    \item $\phi$ é a \textbf{função de ativação};
    \item $y_k$ é a \textbf{saída}.
\end{itemize}

Quando $v_k > \theta$, o neurônio é ativado e produz uma saída. No caso do nó MCP, 
$y_k \in \{0,1\}$. 

\subsection{Funções de ativação}

Uma função de ativação define a saída do nó. A mais básica é a Heaviside, 
também conhecida como \textit{função de limiar}, definida na Eq. \eqref{eq:heaviside}.
\begin{equation}
\label{eq:heaviside}
\phi(v_k) = 
\begin{cases}
1, & \text{se} \, v_k \geq 0 \\
0, & \text{se} \, v_k < 0.
\end{cases}
\end{equation}

Outras funções de ativação são também utilizadas. A seguir, veremos mais dois exemplos.

\subsubsection{Função Relu}

A função Relu (\textit{rectified linear unit}) é definida como  
\begin{equation*} % sem referência.
\phi(v_k) = \max\{ 0, v_k \}.
\end{equation*}

\subsubsection{Função sigmoide}

A função sigmoide é definida como  
\begin{equation*} % sem referência.
\phi(v_k) = \frac{1}{1 + \exp(-a v_k)},
\end{equation*}
onde $a$ é um parâmetro de suavização.
```
- Interpretar os comandos novos: 
	- `\theta`: inclusão da letra grega $\theta$ (ver mais letras gregas);
		- Por exemplo: `\alpha, \beta, \Delta` gera $\alpha, \beta, \Delta$
	- `$...$`: modo matemático em linha (_inline_)
		- Escreva entidades matemáticas simples com o modo matemático.
		Por exemplo, `$\alpha + \beta = \Delta$` produz a equação $\alpha + \beta = \Delta$
	- O modo matemático aplica-se a todo caracter simples, entretanto atente-se para algumas diferenças:
		
		| expressão | resultado | erro? |
		|:-----:|:----------:|:---:|
		|`$a$`|$a$|
		|`$ab$`|$ab$|
		|`$a b$`|$a b$|
		|`$ a b $`|$ a b $|
		|`$a,b$`|$a,b$|
		|`$a\,b$`|$a\,b$|
		|`$a!b$`|$a!b$|
		|`$a\!b$`|$a\!b$|
		|`$a~b$`|$a~b$|
		|`$a\~b$`|$a\~b$| sim
		|`$a~~b$`|$a~~b$| 
		|`$a\ \b$`|$a\ \b$|	sim
		|`$a\ \ b$`|$a\ \ b$|		
		|`$a\ \ \ b$`|$a\ \ \ b$|			
		|`$a\\b$`|$a\\b$|
		|`$duas palavras$`|$duas palavras$|
		|`$duas \, palavras$`|$duas \, palavras$|
		|`$\text{duas palavras}$`|$\text{duas palavras}$|
		|`$\text{duas \, palavras}$`|$\text{duas \, palavras}$|
		|`${a,b}$`|${a,b}$|
		|`${{a,b}}$`|${{a,b}}$|
		|`$\{a,b\}$`|$\{a,b\}$|
		|`$\{a,b}$`|$\{a,b}$| sim
		|`$(a,b)$`|$(a,b)$|
		|`$[a,b]$`|$[a,b]$|
		|`$[a,b)$`|$[a,b)$|
		|`$)a,b\}$`|$)a,b\}$|
		|`$\{\{a,b\}\}$`|$\{\{a,b\}\}$|
		|`$\{[(a,b)]\}$`|$\{[(a,b)]\}$|
		|`$a&b$`|$a&b$| sim
		|`$a\&b$`|$a\&b$| 	
		
##### Passo 14: Analisar o ambiente `equation`

- Inserimos equações com o ambiente `equation`

```latex
\begin{equation}
    ...
\end{equation}
```

- Referenciamos com `\label`

```latex
\begin{equation}
\label{eq:nome}
    ...
\end{equation}
```

- Inserimos elementos matemáticos sem a necessidade do par `$...$`

```latex
\begin{equation}
\label{eq:nome}
    v_k = b_k + \displaystyle \sum_{j=1}^m w_{kj} x_j 
\end{equation}
``` 

- O que temos na equação do neurônio
`v_k = b_k + \displaystyle \sum_{j=1}^m w_{kj} x_j` 
$$v_k = b_k + \displaystyle \sum_{j=1}^m w_{kj} x_j$$ 
	- subscritos:
		- `v_k`, `b_k`, `w_{kj}`, `x_j`
   - somatória: 
   		-  `\sum_{j=1}^m`
   	- sobrescrito: 
		- `{j=1}^m` 
   	- comando de estilo: 
   		- `\displaystyle`
   	- operadores:
   		- `+`, `=`

- Podemos combinar tudo	 isso e construir qualquer expressão matemática. Vejamos:

	| expressão | resultado | erro? |
	|:-----:|:----------:|:---:|
	|`$c_d$`|$c_d$|
	|`$c^d$`|$c^d$|
	|`$ce^d$`|$ce^d$|
	|`${ce}^d$`|${ce}^d$|
	|`$(ce)^d$`|$(ce)^d$|
	|`$c^d_f$`|$c^d_f$|
	|`$ce^d_f$`|$ce^d_f$|
	|`$(ce)^d_f$`|$(ce)^d_f$|
	|`$2^d + 3^e$`|$2^d + 3^e$|
	|`$2^d + 3e_fg$`|$2^d + 3^e_fg$|
	|`$2^d^e$`|$2^d^e$| erro
	|`${2^d}^e$`|${2^d}^e$|
	|`$(g^h_j)_1$`|$(g^h_j)_1$|
	|`$A_{a=1}^b$`|$A_{a=1}^b$|
	|`$A_{a=1}^{b=2}$`|$A_{a=1}^{b=2}$|
	|`$\sum$`|$\sum$|
	|`$\Sigma$`|$\Sigma$|
	|`$\sum_{i=1}^2$`|$\sum_{i=1}^2$|
	|`$\prod$`|$\prod$|
	|`$\Pi$`|$\Pi$|
	|`$\pi$`|$\pi$|
	|`$\prod_{i=1}^2$`|$\prod_{i=1}^2$|
	|`$\sum_{i=1}^2 i + \prod_{i=1}^2 i = 5$`|$\sum_{i=1}^2 i + \prod_{i=1}^2 i = 5$|		
	|`$e^{\pii}$`|$e^{\pii}$|erro
	|`$e^{{\pi}i}$`|$e^{{\pi}i}$|
	|`$e^{i\pi}$`|$e^{i\pi}$|
	|`$e^{{\pi}i} - 1 = 0$`|$e^{{\pi}i} - 1 = 0$|

- Operadores aritméticos
 
	| expressão | resultado |
	|:-----:|:----------:|
	|`$a+b-(c.d) \div e = f$`|$a+b-(c.d) \div e = f$|
	|`$4 \div 3 \neq -1$`|$4 \div 3 \neq -1$|

##### Passo 15: Criar lista não ordenada com `itemize`

- Criamos listas não ordenadas com o seguinte bloco

```latex
\begin{itemize}
    \item A
    \item B
    ...
\end{itemize}
```

##### Passo 16: Preencher lista combinando modo matemático e texto

-  Escrevendo sequencias:

```latex
\item $x_1,x_2,\ldots,x_m$ são \textbf{sinais de entrada};
```

- Sequencias finitas ou infinitas podem ser indicadas com `...` e variantes

	| expressão | resultado | conveniente? |
	|:-----:|:----------:|:---:|
	|`$...$`|$...$|não
	|`$\ldots$`|$\ldots$|sim
	|`$a,\ldots,b$`|$a,\ldots,b$|sim
	|`$a_1,a_2,\ldots,a_n$`|$a_1,a_2,\ldots,a_n$|sim
	|`$\cdots$`|$\cdots$|
	|`$a,\cdots,b$`|$a,\cdots,b$|não
	|`$[a \cdots b]$`|$[a \cdots b]$|sim
	|`$.$`|$.$|
	|`$\cdot$`|$\cdot$|
	|`$a.b = ab$`|$a.b = ab$|
	|`$a \cdot b \neq $`|$a \cdot b$|

- Decorações para representar matrizes, vetores e entidades da Álgebra Linear

	| expressão | resultado 	
	|:-----:|:----------:|
	|`$\vdots$`|$\vdots$|
	|`$\ddots$`|$\ddots$|
	|`$\colon$`|$\colon$|
	|`$a:b \neq a \colon b$`|$a:b \neq a \colon b$|
	
- Vetor linha 

	| expressão | resultado 	
	|:-----:|:----------:|
	|`$[ v_1 v_2 \cdots v_n ]^T$`|$[ v_1 v_2 \cdots v_n ]^T$|
	|`$[ v_1 \ \ v_2 \ \ \cdots \ \ v_n ]^T$`|$[ v_1 \ \ v_2 \ \ \cdots \ \ v_n ]^T$|
	
- Vetores

	| expressão | resultado| comentário|	
	|:-----:|:----------:|:---:|
	|`$\vec{v}$`|$\vec{v}$|notação de Gibbs|
	|`$\bf{v}$`|$\bf{v}$|notação de Gibbs (variante)|
	|`$\underline{v}$`|$\underline{v}$|notação de Gibbs (variante)|
	|`$v_i$`|$v_i$|notação de Einstein|
	
- Letras gregas
 
 ```latex
 \item $\phi$ é a \textbf{função de ativação}
 ```
| expressão | resultado 	
|:-----:|:----------:| 
|`$\alpha$`|$\alpha$|
|`$\beta$`|$\beta$|
|`$\gamma$`|$\gamma$|
|`$\delta$`|$\delta$|
|`$\epsilon$`|$\epsilon$|
|`$\varepsilon$`|$\varepsilon$|
|`$\zeta$`|$\zeta$|
|`$\eta$`|$\eta$|
|`$\theta$`|$\theta$|
|`$\vartheta$`|$\vartheta$|
|`$\iota$`|$\iota$|
|`$\kappa$`|$\kappa$|
|`$\lambda$`|$\lambda$|
|`$\mu$`|$\mu$|
|`$\nu$`|$\nu$|
|`$\xi$`|$\xi$|
|`$\pi$`|$\pi$|
|`$\varpi$`|$\varpi$|
|`$\rho$`|$\rho$|
|`$\varrho$`|$\varrho$|
|`$\sigma$`|$\sigma$|
|`$\varsigma$`|$\varsigma$|
|`$\tau$`|$\tau$|
|`$\upsilon$`|$\upsilon$|
|`$\phi$`|$\phi$|
|`$\varphi$`|$\varphi$|
|`$\chi$`|$\chi$|
|`$\psi$`|$\psi$|
|`$\omega$`|$\omega$|
|`$\Gamma$`|$\Gamma$|
|`$\Delta$`|$\Delta$|
|`$\Theta$`|$\Theta$|
|`$\Lambda$`|$\Lambda$|
|`$\Xi$`|$\Xi$|
|`$\Pi$`|$\Pi$|
|`$\Sigma$`|$\Sigma$|
|`$\Upsilon$`|$\Upsilon$|
|`$\Phi$`|$\Phi$|
|`$\Psi$`|$\Psi$|
|`$\Omega$`|$\Omega$|

- Relacionais

```latex
Quando $v_k > \theta$, o neurônio é...
```

|expressão|resultado|
|:---:|:---:|
|`$>$`|$>$|
|`$<$`|$<$|
|`$\leq$`|$\leq$|
|`$\geq$`|$\geq$|
|`$=$`|$=$|
|`$\neq$`|$\neq$|
			
- Conjuntos 

```latex
... No caso do nó MCP, $y_k \in \{0,1\}$. 
```
|expressão|resultado|
|:---:|:---:|
|`$\in$`|$\in$|
|`$\notin$`|$\notin$|
|`$\subset$`|$\subset$|
|`$\supset$`|$\supset$|
|`$\cup$`|$\cup$|
|`$\cap$`|$\cap$|
|`$\bigcup$`|$\bigcup$|
|`$\bigcap$`|$\bigcap$|

##### Passo 17: Incluir entidades matemáticas especiais com `amsmath`

- Para ter acesso a um novo ferramental matemático, carregaremos o pacote `amsmath`

```latex
\documentclass[10pt,journal,compsoc]{IEEEtran}
...
\usepackage{amsmath,amssymb,bm} % entidades matemáticas <---
```

- `amssymb` e `bm` carregam uma sorte de novos símbolos

##### Passo 18: Construir definição de função com condições/restrições

```latex
\begin{equation}
\label{eq:heaviside}
\phi(v_k) = 
\begin{cases}
1, & \text{se} \, v_k \geq 0 \\
0, & \text{se} \, v_k < 0.
\end{cases}
\end{equation}
``` 

$$\phi(v_k) = 
\begin{cases}
1, & \text{se} \, v_k \geq 0 \\
0, & \text{se} \, v_k < 0.
\end{cases}$$

- O bloco `cases` permite-nos criar múltiplas definições para uma entidade 

```latex
$$f(x) = 
\begin{cases}
x, & \text{se} \, x > 1 \\
\sqrt{x}, & \text{se} \, 0 < x \leq 1 \\
0, & \text{se} \, x = 0 \\
x^3, & \text{se} \, -1 \le x < 0 \\
\cos(x), & \text{se} \, x < -1 
\end{cases}$$
```
$$f(x) = 
\begin{cases}
x, & \text{se} \, x > 1 \\
\sqrt{x}, & \text{se} \, 0 < x \leq 1 \\
0, & \text{se} \, x = 0 \\
x^3, & \text{se} \, -1 \le x < 0 \\
\cos(x), & \text{se} \, x < -1 
\end{cases}$$

- A função de `&` e `\\`

	- `&` é um separador
	- `\\` é uma quebra de linha

- Outras construções com `&` e `\\`

	- Equações alinhadas
	
	```latex
	$$\begin{eqnarray}
	a&=&1 \\
	b&=&2 \\
	c&=&3
	\end{eqnarray}$$
	```
$$\begin{eqnarray}
a&=&1 \\
b&=&2 \\
c&=&3
\end{eqnarray}$$

	- Sistemas de equações

	```latex
	$$\begin{cases}
	a_{11}x_1 +a_{12}x_2 + a_{1n}x_3 &=& b_1 \\
	a_{21}x_1 +a_{22}x_2 + a_{2n}x_3 &=& b_2 \\
	\vdots &\vdots&\vdots \\
	a_{m1}x_1 +a_{m2}x_2 + a_{mn}x_3 &=& b_m
	\end{cases}$$
	```
	$$\begin{cases}
	a_{11}x_1 +a_{12}x_2 + a_{1n}x_3 &=& b_1 \\
	a_{21}x_1 +a_{22}x_2 + a_{2n}x_3 &=& b_2 \\
	\vdots &\vdots&\vdots \\
	a_{m1}x_1 +a_{m2}x_2 + a_{mn}x_3 &=& b_m
	\end{cases}$$
	
##### Passo 19: Reconhcer equações sem numeração

- Podemos remover a numeração de equações adicionando um `*` após o bloco `equation`. Por exemplo:

```latex
A função Relu (\textit{rectified linear unit}) é definida como  
\begin{equation*} % sem referência.
\phi(v_k) = \max\{ 0, v_k \}.
\end{equation*}
```
##### Passo 20: Fazer referência a equações no texto com `ref` e `eqref`

- A função Heaviside no texto tem o label a seguir: 

```latex
\label{eq:heaviside}
```

- Podemos eferenciá-la no texto com 
	- `\ref{eq:heaviside}`: forma _sem_ parênteses. Compilará, por exemplo,  como Eq. 3
	- `\eqref{eq:heaviside}`: forma _com_ parênteses. Compilará, por exemplo,  como Eq. (3)


##### Passo 21: Compreender elementos matemáticos adicionais 

- Alguns elementos adicionais aparecem na definição das funções de ativação do texto

	- Funções 
	
	|expressão|resultado|
|:---:|:---:|
|`$\max$`|$\max$|
|`$\min$`|$\min$|
|`$\exp$`|$\exp$|

	- Frações
	
	|expressão|resultado|
|:---:|:---:|
|`$\frac{1}{2}$`|$\frac{1}{2}$|
|`$\dfrac{1}{2}$`|$\dfrac{1}{2}$|

	-  Funções logarítmicas

	|expressão|resultado|
|:---:|:---:|
|`$\ln$`|$\ln$|
|`$\log$`|$\log$|

	-  Álgebra linear

	|expressão|resultado|
|:---:|:---:|
|`$\det$`|$\det$|
|`$\dim$`|$\dim$|
|`$\deg$`|$\deg$|

	- Análise
	
	|expressão|resultado|
|:---:|:---:|
|`$\sup$`|$\sup$|
|`$\inf$`|$\inf$|
|`$\limsup$`|$\limsup$|
|`$\liminf$`|$\liminf$|

-  Funções trigonométricas (inversas)

	|expressão|resultado|
|:---:|:---:|
|`$\sin$`|$\sin$|
|`$\cos$`|$\cos$|
|`$\tan$`|$\tan$|
|`$\sec$`|$\sec$|
|`$\csc$`|$\csc$|
|`$\sinh$`|$\sinh$|
|`$\cosh$`|$\cosh$|
|`$\tanh$`|$\tanh$|
|`$\arcsin$`|$\arcsin$|
|`$\arccos$`|$\arccos$|


**Suplemento:** como escrever matrizes e determinantes?

- Matrizes simples 

```latex
$$\begin{matrix}
a_{11} & a_{12} & \ldots & a_{1n} \\
a_{21} & a_{22} & \ldots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \ldots & a_{mn}
\end{matrix}$$
```
$$\begin{matrix}
a_{11} & a_{12} & \ldots & a_{1n} \\
a_{21} & a_{22} & \ldots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \ldots & a_{mn}
\end{matrix}$$

- Matrizes com parênteses

```latex
$$\begin{pmatrix}
a_{11} & a_{12} & \ldots & a_{1n} \\
a_{21} & a_{22} & \ldots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \ldots & a_{mn}
\end{pmatrix}$$
```
$$\begin{pmatrix}
a_{11} & a_{12} & \ldots & a_{1n} \\
a_{21} & a_{22} & \ldots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \ldots & a_{mn}
\end{pmatrix}$$

- Matrizes com colchetes

```latex
$$\begin{bmatrix}
a_{11} & a_{12} & \ldots & a_{1n} \\
a_{21} & a_{22} & \ldots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \ldots & a_{mn}
\end{bmatrix}$$
```
$$\begin{bmatrix}
a_{11} & a_{12} & \ldots & a_{1n} \\
a_{21} & a_{22} & \ldots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \ldots & a_{mn}
\end{bmatrix}$$

- Matrizes com chaves

```latex
$$\begin{Bmatrix}
a_{11} & a_{12} & \ldots & a_{1n} \\
a_{21} & a_{22} & \ldots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \ldots & a_{mn}
\end{Bmatrix}$$
```
$$\begin{Bmatrix}
a_{11} & a_{12} & \ldots & a_{1n} \\
a_{21} & a_{22} & \ldots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \ldots & a_{mn}
\end{Bmatrix}$$

- Determinantes 

```latex
$$\begin{vmatrix}
a_{11} & a_{12} & \ldots & a_{1n} \\
a_{21} & a_{22} & \ldots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \ldots & a_{mn}
\end{vmatrix}$$
```
$$\begin{vmatrix}
a_{11} & a_{12} & \ldots & a_{1n} \\
a_{21} & a_{22} & \ldots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \ldots & a_{mn}
\end{vmatrix}$$

- Normas de matrizes

```latex
$$\begin{Vmatrix}
a_{11} & a_{12} & \ldots & a_{1n} \\
a_{21} & a_{22} & \ldots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \ldots & a_{mn}
\end{Vmatrix}$$
```
$$\begin{Vmatrix}
a_{11} & a_{12} & \ldots & a_{1n} \\
a_{21} & a_{22} & \ldots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \ldots & a_{mn}
\end{Vmatrix}$$