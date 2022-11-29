# Fund_Prog_Python_Agenda
Mapa da disciplina de fundamentos de programação Python, do curso de pós-graduação em desenvolvimento de sistemas em Python - 1º Bimestre.

<H1>Proposta</H1>

Considere que você está participando de um processo seletivo para uma vaga de desenvolvedor, foi requisitado a você elaborar um pequeno projeto em linguagem Python. O programa requisitado como Prova de Conceitos seria uma versão beta (versão de inicial), onde deveriam ser armazenados os dados de contato de sua agenda.
<h2>Para cada registro, deverá ser armazenado as seguintes informações:</h2>
<p>- Nome;</p
<p>- Telefone;</p>
<p>- Cidade;</p>
<p>- Estado;</p>
<p>- Status (P-> Pessoal) ou (C-> Comercial).</p>
<h2>O programa deverá apresentar um menu de opções ao usuário:</h2>
<p>1.	Cadastrar Pessoa na Agenda: ao selecionar essa opção, o usuário deverá ser capaz de informar todos os dados do contato para registro;</p>
<p>2.	Alterar dados da Pessoa: ao selecionar essa opção, o usuário deverá indicar o nome do contato que deseja alterar, caso seja encontrado apresentar os campos para realizar a alteração, caso não encontrado indicar: Pessoa com o nome XXX não encontrada;</p>
<p>3.	Listar Agenda: ao selecionar essa opção, o programa deverá imprimir, na tela, todos os registros, um contato por linha;</p>
<p>4.	Procurar pessoa na Agenda: ao selecionar essa opção, o usuário deverá indicar o nome do contato que deseja visualizar os dados, caso seja encontrado apresentar os dados do mesmo na tela, caso não encontrado indicar: Pessoa com o nome XXX não encontrada;</p>
<p>5.	Excluir Pessoa da Agenda: ao selecionar essa opção, o usuário deverá indicar o nome do contato que deseja excluir os dados, caso seja encontrado excluir o mesmo e escrever na tela “Cadastro excluído”, caso não encontrado indicar: Pessoa com o nome XXX não encontrada;</p>
<p>6.	Sair do sistema: o programa deve ser encerrado se, e somente se, o usuário escolher essa opção.</p>

<H1>The extra mile</H1>
<p>- A proposta do trabalho é relativamente simples, seria possível realizar utilizando uma lista, algunas iterações, e estaria resolvido. Mas na minha família temos 4 pedros, procurar um contato pelo nome poderia não funcionar. Por isso acrescentei uma chave primária, e a possibilidade de, após procurar o contato, selecionar qual das opções você queria, efetivamente;</p>
<p>- Ao fim de cada operação o usuário é questionado se deseja permanecer no programa ou não;</p>
<p>- Embora não fizesse parte do escopo da matéria, tentei criar minhas próprias funções encapsuladas e reutilizá-las na medida do possível.</p>
