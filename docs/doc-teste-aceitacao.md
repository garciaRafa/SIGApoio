**US001 – Autenticação de Usuário**

| Teste | Descrição | Especificação | Resultado |
| :---- | :---- | :---- | :---- |
| Teste 01 Cadastrar Usuário | TA01 \- Cadastrar Usuário 	<br> A1.1 \- O ator preenche os dados de cadastro; 			  <br> A1.2 - O ator seleciona a opção Cadastrar; 			 <br>A1.3 \- O sistema salva os dados; 			<br> A1.4 \- O sistema exibe uma mensagem de: Cadastro realizado com sucesso. ; <br> A1.5 \- Fim do fluxo. | Especificação OK. 		 | OK	 |
| Teste 02 Login de usuário | TA03 \- Excluir Produto 	 A3.1 \- O ator preenche os dados de login			 <br> A3.2 \- O ator seleciona a opção login ; <br> A3.3 \- O sistema confirma o login baseado nas informações 	 <br> A3.4 \- O ator é redirecionado para a tela principal do sistema; <br> A3.5 \- O Sistema exibe uma mensagem de Login realizado com sucesso.| A função implementada não segue o passo 3.4. A implementação não segue o User Story. 	 | O login é efetuado, contudo a mensagem de login efetuado não foi exibida. |
| Teste 03 Logout de usuário | TA05 \- Logout de usuário 			 A5.1 \- O ator autenticado seleciona a opção logout; <br> A5.2 \- O sistema apresenta uma mensagem de confirmação de logout; <br> A5.3 \- O ator seleciona a confirmação do logout; 			 <br> A5.4 \- O ator é deslogado do sistema.        | Requisição OK. | OK. |
| Teste 04 Excluir conta | TA06 \- Excluir conta            A6.1 O ator navega até a área de configurações de perfil  <br> 6.2 \- O ator seleciona a opção Excluir conta  <br> 6.3 \- O ator preenche as informações para confirmação     <br>6.4 \- O ator confirma seleciona a confirmação de exclusão   <br>6.5 \- O sistema exclui aconta <br> 6.6 \- O sistema exibe uma mensagem [MSG005] de conta removida com sucesso | A função implementada não segue os passos TA 6.6. | A mensagem [MSG005] não é exibida, contudo a conta é excluída do sistema.

**Relatório de Bugs e Providências**  
Responsabilidade do Gerente

| Teste | Providência | Tarefas/Tipo |
| :---- | :---- | :---- |
| Teste 02 – Logout de Usuário| Corrigir a implementação do fluxo do user story.	 | Tarefa: Bug de Implementação. |
| Teste 04 – Excluir conta | Corrigir a especificação do fluxo do US e sua implementação. | Tarefa:  Tarefa: Bug de Implementação. |

