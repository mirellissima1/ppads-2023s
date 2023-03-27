CREATE TABLE IF NOT EXISTS turmas (
  id_turma INT AUTO_INCREMENT PRIMARY KEY,
  nome_turma VARCHAR(50) NOT NULL,


);
CREATE TABLE IF NOT EXISTS disciplina(
  id_disciplina INT AUTO_INCREMENT PRIMARY KEY,
  nome_disciplina VARCHAR(50) NOT NULL,
  horario VARCHAR(20) NOT NULL,
)
CREATE TABLE IF NOT EXISTS aluno(
  id_aluno INT AUTO_INCREMENT PRIMARY KEY,
  nome_aluno VARCHAR(50) NOT NULL,
  matricula VARCHAR(20) NOT NULL,
  email_responsavel VARCHAR(50) NOT NULL,
  turma_id INT,
  FOREIGN KEY (turma_id) REFERENCES turmas(id_turma),

)
CREATE TABLE IF NOT EXISTS professor(
  id_professor INT AUTO_INCREMENT PRIMARY KEY,
  nome_professor VARCHAR(50) NOT NULL,
  responsavel BOOLEAN NOT NULL DEFAULT FALSE,
  turma_id INT,
  disciplina_id INT,
  FOREIGN KEY (turma_id) REFERENCES turmas(id_turma),
  FOREIGN KEY (disciplina_id) REFERENCES disciplina(id_disciplina)
)

CREATE TABLE IF NOT EXISTS presencas (
  id INT AUTO_INCREMENT PRIMARY KEY,
  aluno_id INT,
  dia DATE NOT NULL,
  presente BOOLEAN NOT NULL,
  FOREIGN KEY (aluno_id) REFERENCES aluno(id_aluno)
);

CREATE TABLE IF NOT EXISTS  usuario (
  id INT AUTO_INCREMENT PRIMARY KEY,
  login VARCHAR(20) NOT NULL,
  password VARCHAR(50) NOT NULL,
  professor_id INT,
  FOREIGN KEY (professor_id) REFERENCES professor(id)
);

ALTER TABLE db_escola.turmas ADD COLUMN aluno_id INT, ADD FOREIGN KEY aluno_id(aluno_id) REFERENCES turmas(id_turma) ON DELETE CASCADE;

ALTER TABLE db_escola.turmas DROP FOREIGN KEY aluno_id;