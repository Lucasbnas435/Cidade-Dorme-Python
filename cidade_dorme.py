import random
import time


class Player:
	def __init__(self, identificador, nome="npc", funcao=""):
		self.identificador = identificador
		self.vida = 1
		self.nome = nome
		self.funcao = funcao
		
	def seleciona_funcao(self, letra):
		papel = ""
		if letra == "m":
			papel = "mafioso"
		elif letra == "c":
			papel = "cidadao"
		elif letra == "d":
			papel = "doutor"
		elif letra == "x":
			papel = "xerife"
		
		self.funcao = papel
		
		if self.identificador == 0:
			print("\nAtenção!!! Você é um", papel + "!")
			
	def morre(self, eliminado):
		self.vida = 0
		if eliminado and self.identificador == 0:
			print("\n" + self.nome + ",", "você foi eliminado!")
			
	def revive(self):
		self.vida = 1
			
	
lista_usuarios = []
		

def principal():
	global lista_usuarios
	nome = input("Seja bem-vindo ao jogo Cidade Dorme!\n\nPor favor, digite seu nome para jogar: ")
	print("\n" + nome + ",", "você estará jogando com outros 7 jogadores.\n\nHá um mafioso solto pela cidade...\nFelizmente, ainda temos um doutor e um xerife por aí...")
	quantidade_vivos = 8

	funcoes_disponiveis = ["m", "d", "x", "c", "c", "c", "c", "c"]
	
	aleatorio = random.randint(0, len(funcoes_disponiveis) - 1)
	
	lista_usuarios.append(Player(0, nome))
	lista_usuarios[0].seleciona_funcao(funcoes_disponiveis[aleatorio])

	for a in range(1, 8):
		del(funcoes_disponiveis[aleatorio])
		aleatorio = random.randint(0, len(funcoes_disponiveis) - 1)
		lista_usuarios.append(Player(a))
		lista_usuarios[a].seleciona_funcao(funcoes_disponiveis[aleatorio])

	rodada = 1
	
	while quantidade_vivos > 3:
		time.sleep(0.5)
		print("\n*** RODADA", rodada, "***")
		morto = mata()
		possivel_salvo = salva(morto)
		
		if possivel_salvo:
			time.sleep(1)
			print("\nNa última noite, um cidadão sofreu uma tentativa de assassinato. Felizmente, o doutor não mediu esforços e conseguiu salvá-lo!")
		elif morto != 0:
			time.sleep(1)
			print("\nNa última noite, um terrível assassinato ocorreu na cidade, e o player", morto, "foi morto.")
			quantidade_vivos = quantidade_vivos - 1
		else:
			quantidade_vivos = quantidade_vivos - 1
			time.sleep(1)
			print("\nNa última noite, um terrível assassinato ocorreu na cidade, e", lista_usuarios[0].nome, "foi morto.")
			print("\nOh não!", lista_usuarios[0].nome + ", o mafioso te matou!!!")
			sair = input("\nA partir daqui você só poderá participar como espectador. Deseja sair do jogo? ")
			if sair == "sim" or sair == "Sim" or sair == "s" or sair == "S":
				break
			else:
				print("\nAtenção!!! Agora, você está jogando como espectador!")
		
		if lista_usuarios[0].funcao == "xerife" and lista_usuarios[0].vida == 1:
			xerife_trabalha()
		
		if quantidade_vivos <= 4:
			time.sleep(1)
			print("\nCuidado e atenção nas decisões! Se o mafioso não for eliminado agora, será o fim do jogo com derrota da cidade.")
		
		acusacao = acusa(quantidade_vivos)
		quantidade_vivos = acusacao[0]
		humano_eliminado = acusacao[1]
		rodada = rodada + 1
		if quantidade_vivos == 2 or quantidade_vivos == 3:
			time.sleep(1)
			print("\n*** THE END ***\n")
			time.sleep(0.5)
			print("O MAFIOSO VENCEU!!!")
			time.sleep(0.5)
			for jogador in lista_usuarios:
				if jogador.funcao == "mafioso" and jogador.identificador == 0:
					print("\n" + nome, "era o terrível mafioso.")
				elif jogador.funcao == "mafioso":
					print("\nO player", str(jogador.identificador), "era o terrível mafioso.")
		elif humano_eliminado and quantidade_vivos != 0:
			time.sleep(1)
			sair = input("\nA partir daqui você só poderá participar como espectador. Deseja sair do jogo? ")
			if sair == "sim" or sair == "Sim" or sair == "s" or sair == "S":
				break
			else:
				print("\nAtenção!!! Agora, você está jogando como espectador!")
				

def mata():
	global lista_usuarios
	matou = False
	if lista_usuarios[0].funcao == "mafioso":
		while not matou:
			numero = int(input("\nDigite o número do player que você deseja matar: "))
			if numero <= 0 or numero > 7:
				print("\nNúmero inválido")
			elif lista_usuarios[numero].vida == 1 and numero != 0:
				matou = True
				lista_usuarios[numero].morre(False)
			else:
				print("\nEsse player já está morto!")
	else:
		while not matou:
			numero = random.randint(0, 7)
			if lista_usuarios[numero].funcao != "mafioso" and lista_usuarios[numero].vida == 1:
				matou = True
				lista_usuarios[numero].morre(False)

	return numero
	
		
def salva(numero):
	global lista_usuarios
	reviveu = False
	doutor_vivo = False
	escolha_valida = False
	
	for x in range(len(lista_usuarios)):
		if lista_usuarios[x].funcao == "doutor" and lista_usuarios[x].vida == 1:
			doutor_vivo = True
	
	if lista_usuarios[0].funcao == "doutor" and doutor_vivo:
		while not escolha_valida:
			escolha = int(input("\nDigite o número do player que você deseja tentar salvar: "))
			if numero == escolha:
				lista_usuarios[escolha].revive()
				reviveu = True
				escolha_valida = True
			elif lista_usuarios[escolha].vida == 0 and escolha != numero:
				print("\nEsse player já estava morto no início desta rodada e não participa mais do jogo. Escolha outro para tentar salvar.")
			else:
				escolha_valida = True
				
	elif doutor_vivo:
		while not escolha_valida:
			escolha = random.randint(0, 7)
			if numero == escolha:
				lista_usuarios[escolha].revive()
				reviveu = True
				escolha_valida = True
			elif lista_usuarios[escolha].vida == 1:
				escolha_valida = True

	return reviveu

	
def xerife_trabalha():
	global lista_usuarios
	vivo = False
	while not vivo:
		valido = False
		while not valido:
			escolha = int(input("\nXerife, digite o número do player que o senhor deseja investigar: "))
			if escolha <= 0 or escolha >= 8:
				print("\nNúmero inválido.")
			else:
				valido = True
		
		if lista_usuarios[escolha].funcao == "mafioso":
			time.sleep(0.5)
			print("\nEle é o mafioso!!! Agora você já sabe!")
			vivo = True
		elif lista_usuarios[escolha].vida == 1:
			time.sleep(0.5)
			print("\nEle não é o mafioso. Boa sorte na próxima investigação!")
			vivo = True
		else:
			print("\nEsse player já está morto! Investigue outro!")
			
	
def acusa(quantidade_vivos):
	global lista_usuarios
	resultado = False
	ja_acusado = 20000
	players_vivos = []
	printar_vivos = ""
	lista_defesas = ["Sou inocente!!! Por favor, não me eliminem!", "Enquanto a cidade dormia, eu estava passeando no shopping. Não cometi crime algum.", "Não fiz nada! Votem em outro!", "Eu estava dormindo na última noite.", "Virei a noite trabalhando, sou inocente."]
	
	for x in range(1, len(lista_usuarios)):
		if lista_usuarios[x].vida == 1:
			players_vivos.append(str(x))
			
	for y in range(len(players_vivos)):
		if y == (len(players_vivos) - 2):
			printar_vivos = printar_vivos + players_vivos[y] + " e "
		elif y == (len(players_vivos) - 1):
			printar_vivos = printar_vivos + players_vivos[y] + "."
		else:
			printar_vivos = printar_vivos + players_vivos[y] + ", "
	
	if lista_usuarios[0].vida == 0:
		print("\nRestam vivos estes players:", printar_vivos)
		while not resultado:
			acusacao = False
			while not acusacao:
				escolha = random.randint(1, 7)
				if lista_usuarios[escolha].vida == 1 and escolha != ja_acusado:
					acusacao = True
					print("\nOs jogadores decidiram acusar o player", str(escolha) + ".\n\nHora da votação!")
			
			voto_final = random.randint(0, 2)
			if voto_final > 0 and lista_usuarios[escolha].funcao != "mafioso":
				time.sleep(2)
				print("\nVotação concluída! O player acusado foi eliminado. \n\nInfelizmente, ele não era o mafioso...")
				resultado = True
				quantidade_vivos = quantidade_vivos - 1
				lista_usuarios[escolha].morre(True)
			elif voto_final > 0 and lista_usuarios[escolha].funcao == "mafioso":
				time.sleep(2)
				print("\nVotação concluída! O player acusado foi eliminado. \n\nEle era o mafioso!\n\n*** THE END ***\n\nA CIDADE VENCEU!!!")
				resultado = True
				quantidade_vivos = 0
			else:
				time.sleep(2)
				print("\nVotação concluída! O player acusado fez uma excelente defesa e não foi eliminado. Será necessário fazer outra acusação.")
				ja_acusado = escolha

		return [quantidade_vivos, False]

	else:
		print("\nRestam vivos estes players:", lista_usuarios[0].nome + ", " + printar_vivos)
	
	while not resultado:
		humano_eliminado = False
		acusacao = False
		escolha_valida = False
		while not escolha_valida:
			escolha = int(input("\nDigite o número do player que você quer acusar: "))
			if escolha <= 0 or escolha > 7:
				print("\nNúmero inválido.")
			elif lista_usuarios[escolha].vida == 0:
				print("\nEsse player já está morto. Escolha outro para acusar.")
			else:
				escolha_valida = True
				print("\nOs players vivos estão indicando quem eles querem acusar...")
				
		escolha_humano = escolha	
		decisao = random.randint(0, 2)
		if decisao > 0 and escolha_humano != ja_acusado:
			time.sleep(1.5)
			print("\nOutros jogadores concordaram com você, e o player", escolha, "está sendo acusado!")
		else:
			time.sleep(1.5)
			print("\nOs outros jogadores não concordaram com você e acusarão outro player.")
			while not acusacao:
				escolha = random.randint(0, 7)
				if lista_usuarios[escolha].vida == 1 and escolha != ja_acusado and escolha != escolha_humano:
					acusacao = True
					if escolha == 0:
						time.sleep(1.5)
						print("\nOs outros jogadores decidiram acusar você!!!")
					else:
						time.sleep(1.5)
						print("\nOs outros jogadores decidiram acusar o player", str(escolha) + ".")
		
		if escolha == 0:
			printar_nome = lista_usuarios[0].nome
			time.sleep(0.5)
			defesa = input("\nÉ hora da defesa. Tente demonstrar sua inocência aos outros players para que eles não te eliminem. Digite o que precisar:\n")
			
		else:		
			printar_nome = "O player " + str(escolha)
			time.sleep(0.5)
			print("\nÉ hora de ouvir a defesa. Confira a declaração do player acusado para tomar sua decisão de voto:")
			time.sleep(1.5)
			print("\n" + lista_defesas[random.randint(0, len(lista_defesas) - 1)])
			time.sleep(0.5)
			voto_usuario = input("\nChegou o momento de votar. Você deseja eliminar o player acusado? Digite sua decisão: ")
			print("\nOk! Os players vivos estão votando também...")
		voto_final = random.randint(0, 1)
		
		if voto_final > 0 and lista_usuarios[escolha].funcao != "mafioso":
			time.sleep(1)
			print("\nVotação concluída!", printar_nome, "foi eliminado.")
			
			time.sleep(1)
			print("\nInfelizmente, ele não era o mafioso...")
			resultado = True
			quantidade_vivos = quantidade_vivos - 1
			lista_usuarios[escolha].morre(True)
		elif voto_final > 0 and lista_usuarios[escolha].funcao == "mafioso":
			time.sleep(1)
			print("\nVotação concluída!", printar_nome, "foi eliminado.")
			time.sleep(1)
			print("\nEle era o mafioso!")
			time.sleep(1)
			print("\n*** THE END ***")
			time.sleep(0.5)
			print("\nA CIDADE VENCEU!!!")
			resultado = True
			quantidade_vivos = 0
		else:
			time.sleep(1)
			print("\nVotação concluída!", printar_nome, "fez uma excelente defesa e não foi eliminado. Será necessário fazer outra acusação.")
			ja_acusado = escolha
			
		if voto_final > 0 and escolha == 0:
			humano_eliminado = True
		
	return [quantidade_vivos, humano_eliminado]
						
		
principal()
