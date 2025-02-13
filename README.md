# Client TCP
Um cliente TCP (Transmission Control Protocol) é um programa ou dispositivo que inicia a comunicação com um servidor TCP para trocar dados em uma rede. O TCP é um protocolo de camada de transporte amplamente utilizado na internet, conhecido por fornecer comunicação confiável, ordenada e com verificação de erros. Aqui estão as principais funções de um cliente TCP:

Inicia a conexão: O cliente TCP inicia o processo de comunicação enviando uma solicitação de conexão ao servidor TCP. Isso é feito por meio de um processo chamado "three-way handshake" (aperto de mão em três etapas), onde o cliente e o servidor trocam pacotes SYN (sincronização) e ACK (confirmação) para estabelecer a conexão.

Envia dados: Após estabelecer a conexão, o cliente pode enviar dados ao servidor. O TCP garante que os dados sejam entregues de forma confiável e na ordem correta, retransmitindo pacotes perdidos ou corrompidos, se necessário.

Recebe dados: O cliente também pode receber dados do servidor. O TCP gerencia o fluxo de dados para evitar congestionamento e garante que os pacotes sejam reassembalados na ordem correta.

Fecha a conexão: Quando a comunicação é concluída, o cliente pode iniciar o fechamento da conexão. Isso é feito por meio de um processo de encerramento que envolve o envio de pacotes FIN (finalização) e a confirmação mútua entre cliente e servidor.

Gerencia erros e controle de fluxo: O cliente TCP lida com a detecção e correção de erros, além de controlar o fluxo de dados para evitar sobrecarregar o servidor ou a rede.

Exemplo de uso:
Um exemplo comum de cliente TCP é um navegador web (como Chrome ou Firefox) que se conecta a um servidor web (como Apache ou Nginx) para carregar uma página da internet. O navegador envia uma solicitação HTTP ao servidor, que responde com os dados da página, tudo isso utilizando o protocolo TCP para garantir a entrega confiável dos dados.

Em resumo, o cliente TCP é responsável por iniciar e gerenciar a comunicação com um servidor TCP, garantindo que os dados sejam transmitidos de forma confiável e eficiente.