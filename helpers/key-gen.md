  # lets create a key to sign these tokens with
    - openssl genpkey -out tela.pem -algorithm rsa -pkeyopt rsa_keygen_bits:2048 
  # lets generate a public key for it...
    - openssl rsa -in tela.pem -out tela.pub -pubout 
 