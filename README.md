# Automacao de Envios de Mensagem no Whatsapp

Essa automação é bem simples e o objetivo é ler dados de uma planilha (nome, número e mensagem) e enviar mensagens no whatsapp para essas pessoas.<br><br>

A automação entra na URL do whatsapp no navegador, pede o QR Code e, após lê-lo, entra na URL do whatsapp novamente passando número e mensagem na URL.<br><br>

A partir disso, a página com a mensagem no contato já é carregada e o botão de enviar é clicado logo em seguida. O processo se repete até a última linha preenchida da planilha.<br><br>

Um log em txt com os erros é criado caso dê algum erro no meio do processo.
