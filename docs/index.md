<h2><a href= "https://www.mackenzie.br">Universidade Presbiteriana Mackenzie</a></h2>
<h3><a href= "https://www.mackenzie.br/graduacao/sao-paulo-higienopolis/sistemas-de-informacao">Sistemas de Informação</a></h3>



**Conteúdo**

- [Autores](#autores)
- [Descrição do projeto](#descrição-do-projeto)
- [Diagrama de casos de uso](#diagrama-de-casos-de-uso)
- [Descrição dos casos de uso](#descrição-dos-casos-de-uso)
- [Protótipos de tela](#protótipos-de-tela)
- [Modelo de domínio](#modelo-de-domínio)
- [Decisões de arquitetura](#decisões-de-arquitetura)
- [Diagrama de implantação](#diagrama-de-implantação)
- [Referências](#referências)


# Autores

* Mirella Monção de Souza
* Rute de Almeida Lourenço
* Isabella Lee Abdala
* Luan Kennedy Gomes de Carvalho


# Descrição do projeto

*Projeto sobre sitema para controle de presença dos alunos da escola Octógono.*
*Nesse sistema, diariamente os professores da escola Octógono podem registrar o controle de prenseça e faltas de forma fácil e intuitiva.*


# Diagrama de casos de uso
![Diagrama Casos de Uso](https://github.com/mirellissima1/ppads-2023s/assets/88807596/217a1197-463e-4866-aa6f-c5cbd4ebfd77)

# Descrição dos casos de uso

* Caso de Uso Principal
Descrição: Permitir que o professor registre faltas e Enviar notificações por e-mail para pais e responsáveis em caso de faltas excessivas.
Atores: Administrador, Professor e Pais/Responsáveis

1. Caso de uso: Efetuar chamada (Ator: Professor)

-O professor seleciona a turma na qual deseja efetuar a chamada.
-O professor informa data e hora do lançamento das faltas.
-O sistema exibe a lista de alunos matriculados na turma.
-O professor marca a presença ou falta de cada aluno, usando opções disponíveis no sistema.
-Após finalizar a chamada, o sistema registra as informações de presença/falta para cada aluno.

2. Caso de uso: Alterar registro de presença (Ator: Professor)

-O professor seleciona a turma em que deseja fazer a alteração de presença.
-O professor informa data e hora do dia em que lançou a falta
-O sistema exibe o registro de presença atual dos alunos.
-O professor seleciona o aluno para o qual deseja fazer a alteração.
-O sistema registra alteração do registro de presença.

3. Caso de uso: Receber notificação (Ator: Responsável)

-O sistema identifica a falta de um aluno em uma aula.
-O sistema envia uma notificação por e-mail para o responsável (pai/mãe) do aluno faltante.
-A notificação contém informações sobre a data, horário e disciplina da aula em que o aluno faltou.

4. Caso de uso: Cadastrar professor (Ator: Administrador)

O administrador do sistema seleciona a opção de cadastrar um novo professor.
O sistema exibe um formulário para preenchimento dos dados do professor, como nome, e-mail e senha.
O administrador preenche os dados do professor.
O sistema valida os dados e registra o novo professor no sistema.

5. Caso de uso: Cadastrar disciplina (Ator: Administrador)

O administrador seleciona a opção de cadastrar uma nova disciplina.
O sistema exibe um formulário para preenchimento dos dados da disciplina, como nome e descrição.
O administrador preenche os dados da disciplina.
O sistema valida os dados e registra a nova disciplina no sistema.

6. Caso de uso: Cadastrar aluno (Ator: Administrador)

O administrador seleciona a opção de cadastrar um novo aluno.
O sistema exibe um formulário para preenchimento dos dados do aluno, como nome, data de nascimento e matrícula.
O administrador preenche os dados do aluno.
O sistema valida os dados e registra o novo aluno no sistema.

7. Caso de uso: Cadastrar turma (Ator: Administrador)

O administrador seleciona a opção de cadastrar uma nova turma.
O sistema exibe um formulário para preenchimento dos dados da turma, como ano, curso e horário.
O administrador preenche os dados da turma.
O sistema valida os dados e registra a nova turma no sistema.


# Protótipos de tela
![TELA - LOGIN](https://user-images.githubusercontent.com/88807596/219998781-8097e83b-0637-4f4f-a232-a27b40e5c23e.jpg)
![Web 1920 – 9](https://user-images.githubusercontent.com/88807596/235555557-75c155b9-ee13-4056-89e1-aae97abc0034.jpg)
![TELA - ADD NOVA TURMA](https://user-images.githubusercontent.com/88807596/235555568-f2fcd317-567a-45d5-a973-117436faa4ac.jpg)
![Web 1920 – 10](https://user-images.githubusercontent.com/88807596/235555574-fc101482-4ab1-49c0-8745-50e618a88117.jpg)
![Web 1920 – 11](https://user-images.githubusercontent.com/88807596/235555580-2829f204-a2fe-4a76-8a6d-4a089d0ed990.jpg)
![Web 1920 – 12](https://user-images.githubusercontent.com/88807596/235555590-606bdae8-4e4f-4ce5-8a87-2f3800da8cca.jpg)
![TELA - SALAS PROFESSOR](https://user-images.githubusercontent.com/88807596/219998789-fa3e580d-4559-4437-8ba1-ab976d827a8e.jpg)
![TELA - INFORMAR DATA E HORA DO REGISTRO](https://user-images.githubusercontent.com/88807596/222939093-d73e9d50-4b23-49fc-95eb-ca152d082566.png)
![TELA - REGISTRAR PRESENÇA](https://user-images.githubusercontent.com/88807596/222939104-70efa4cc-1a20-401f-8863-1158135adf54.png)



# Modelo de domínio

![ModeloDominio-PratAns](https://github.com/mirellissima1/ppads-2023s/assets/88807596/e2ec4b4d-912b-4af1-94fc-6f4747e74be2)



# Decisões de arquitetura

Skill
Nosso time é composto por três integrantes, que se divide com habilidades em front end, back end e organização de projetos, fazendo com que auxiliamos uns aos outros. 

Visão
Não queremos construir algo complexo, trazendo algo simples, mas eficiente e facilidade no uso do software.

Desenvolvimento
Pretendemos desenvolver Back-End em Node, banco não relacional MongoDB e Front-End em react.

# Diagrama de implantação

*&lt;Diagrama de implantação&gt;*

# Referências

*&lt;Lista de referências&gt;*
