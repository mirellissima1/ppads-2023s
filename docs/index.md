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


* Diagrama Caso de Uso:![Diagramas Pratica Analise Sistemas](https://user-images.githubusercontent.com/88807596/235549665-6e07ab33-450f-4cfb-8d7c-a00da86e04c5.jpeg)


# Descrição dos casos de uso

* Caso de Uso Principal
Descrição: Permitir que o professor registre faltas e Enviar notificações por e-mail para pais e responsáveis em caso de faltas excessivas.
Atores: Aluno, Professor e Pais/Responsáveis

Fluxo: 
1. O Administrador cadastra professor, disciplina, aluno e turma no sistema.
2. O professor acessa o sistema de registro de faltas.
3. O sistema apresenta uma lista de turmas e disciplinas que o professor leciona.
4. O professor seleciona a turma e disciplina desejada.
5. O sistema apresenta a lista de alunos matriculados na turma selecionada.
6. O professor marca as faltas dos alunos ausentes na aula.
7. O sistema registra as faltas e armazena a informação para futuras consultas.
8. O sistema verifica o número de faltas de um aluno em um período específico.
9. Se o número de faltas for superior a um limite estabelecido, o sistema envia uma notificação por e-mail para os pais ou responsáveis pelo aluno.
10. O sistema registra o envio da notificação e armazena a informação para futuras consultas.


# Protótipos de tela
![TELA - LOGIN](https://user-images.githubusercontent.com/88807596/219998781-8097e83b-0637-4f4f-a232-a27b40e5c23e.jpg)
![TELA - SALAS PROFESSOR](https://user-images.githubusercontent.com/88807596/219998789-fa3e580d-4559-4437-8ba1-ab976d827a8e.jpg)
![TELA - INFORMAR DATA E HORA DO REGISTRO](https://user-images.githubusercontent.com/88807596/222939093-d73e9d50-4b23-49fc-95eb-ca152d082566.png)
![TELA - REGISTRAR PRESENÇA](https://user-images.githubusercontent.com/88807596/222939104-70efa4cc-1a20-401f-8863-1158135adf54.png)




# Modelo de domínio

![Modelo de Dominio](https://user-images.githubusercontent.com/100171962/224523321-7890625a-424d-422a-b3f5-0b84165ed88a.jpeg)



# Decisões de arquitetura

Skill
Nosso time é composto por três integrantes, que se divide com habilidades em front end, back end e organização de projetos, fazendo com que auxiliamos uns aos outros. 

Visão
Não queremos construir algo complexo, trazendo algo simples, mas eficiente e facilidade no uso do software.

Desenvolvimento
Pretendemos desenvolver Back-End em Python com banco relacional SQL, Front-End em HTML e CSS.

# Diagrama de implantação

*&lt;Diagrama de implantação&gt;*

# Referências

*&lt;Lista de referências&gt;*
