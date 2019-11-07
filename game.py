import random
def start():
	camp = [(g,c) for g in 'kbn' for c in 'kbn']
	outcomes = 'DWLLDWWLD'
	game_dict = dict([(gc,r)for gc in camp for r in outcomes])
	Results = {'W':0,'D':0,'L':0}
	g = ' '
	while(true):
		g = input("Выбереите Б, К, или Н; Чтобы выйти нажмите ENTER")
		if (g):
			
			if g in 'kbn':
				print (g)
		else:
			print ("Что то пошло не так >3, попробуйте ёще раз!")
			continue
			random.choice
		c = random.choice('kbn')
		Results[game_dict[(g,c)]] +=1
		return Results
	if (__name__ == '__main__'):
		pint (start())