🧠 Calculadora de Lógica Proposicional

Aplicação desktop desenvolvida em Python utilizando Tkinter, capaz de avaliar expressões de lógica proposicional, gerar automaticamente a tabela-verdade e classificar a fórmula como tautologia, contradição ou contingência.

📌 Funcionalidades
Suporte a até 5 variáveis proposicionais: p, q, r, s, t
Validação de Fórmula Bem Formada (FBF)
Geração automática da tabela-verdade completa
Classificação da expressão em:
✔️ Tautologia
❌ Contradição
🔄 Contingência
Interface gráfica interativa com botões para inserção de símbolos
Área de exibição com rolagem para resultados
🔣 Operadores Lógicos Suportados
Símbolo	Operação
¬	Negação
∧	Conjunção (AND)
∨	Disjunção (OR)
⊻	Ou exclusivo (XOR)
→	Implicação
↔	Bicondicional
🖥️ Interface

A interface permite:

Inserir expressões por meio de botões
Apagar caracteres (DEL)
Limpar a entrada (C)
Gerar a tabela verdade (Resultado)
⚙️ Como Executar
Pré-requisitos:
Python 3 instalado
Passos:
# Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git

# Acesse a pasta
cd seu-repositorio

# Execute o programa
python nome_do_arquivo.py
🧪 Exemplo de Expressão
(p ∧ q) → ¬r

Saída:

Tabela verdade completa
Classificação da expressão
📁 Estrutura do Projeto
avaliar() → Avalia a expressão lógica
verificar_fbf() → Valida a sintaxe da expressão
mostrar_tabela() → Gera e exibe a tabela-verdade
Interface construída com Tkinter
⚠️ Validação de Entrada

O sistema verifica:

Uso correto de parênteses
Ordem válida de operadores
Evita combinações inválidas (ex: p q, ∧ ∧, etc.)

Caso a expressão seja inválida, uma mensagem de erro é exibida.

🚀 Tecnologias Utilizadas
Python 3
Tkinter (interface gráfica)
itertools (geração de combinações)
