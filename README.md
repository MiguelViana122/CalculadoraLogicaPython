aplicação desktop desenvolvida em Python utilizando Tkinter. O programa permite inserir expressões de lógica proposicional, gerar automaticamente a tabela-verdade e classificar a expressão como tautologia, contradição ou contingência.

Funcionalidades
Suporte a até 5 variáveis proposicionais: p, q, r, s, t
Validação de fórmula bem formada (FBF)
Geração automática da tabela-verdade
Classificação da expressão em:
Tautologia
Contradição
Contingência
Interface gráfica simples e intuitiva
Botões para inserção rápida dos operadores
Operadores Suportados
Símbolo	Significado
¬	Negação
∧	Conjunção (AND)
∨	Disjunção (OR)
⊻	Ou exclusivo (XOR)
→	Implicação
↔	Bicondicional
Como Executar
Pré-requisitos
Python 3 instalado
Passos
git clone https://github.com/MiguelViana122/CalculadoraLogicaPython.git
cd CalculadoraLogicaPython
python calculadora.py

Observação: substitua calculadora.py pelo nome real do seu arquivo, se for diferente.

Exemplo de Uso

Entrada:

(p ∧ q) → ¬r

Saída:

Tabela-verdade completa
Classificação da expressão
Estrutura do Projeto
verificar_fbf() → valida a expressão lógica
avaliar() → resolve a expressão
mostrar_tabela() → gera a tabela-verdade
Interface construída com Tkinter
Validação de Entrada

O programa verifica:

Parênteses balanceados
Uso correto dos operadores
Estrutura válida da expressão

Caso haja erro, uma mensagem será exibida.

Tecnologias Utilizadas
Python 3
Tkinter
itertools
Autor

Projeto desenvolvido por Miguel Viana para fins acadêmicos.
