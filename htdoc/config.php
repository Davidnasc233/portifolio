<?php
  // Definindo as credenciais de acesso ao banco de dados
  $dbHost = 'Localhost';        // Nome do host (geralmente 'localhost' para servidores locais)
  $dbUsername = 'root';         // Usuário do MySQL (por padrão no XAMPP, o usuário é 'root')
  $dbPassword = '';             // Senha do MySQL (em ambientes locais, a senha geralmente é vazia)
  $dbName = 'cadastro_usuario'; // Nome do banco de dados que você criou no phpMyAdmin

  // Criando a conexão
  $conexao = new mysqli($dbHost, $dbUsername, $dbPassword, $dbName);

  // Verificando a conexão
  // if ($conexao->connect_error) {
  //     die("Falha na conexão: " . $conexao->connect_error);
  // } else {
  //     echo "Conexão com o banco de dados realizada com sucesso!";
  // }
?>