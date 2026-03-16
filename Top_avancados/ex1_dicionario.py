contato = {
  'nome' : 'Robert',
  'telefone' : 1123434,
  'email' : 'robert@gmail.com',
  'cidade' : 'RJ',

}
contato['instagram'] = '@daleste157',
del contato['telefone'],

print(contato.items()),
if 'email' in contato:
    print('Chave existe!!!')