import time
import random

print()
print('A wild Jigglypuff appears!')
time.sleep(0.2)
print('You only have one pokemon, Snorlax.')
time.sleep(0.2)
print('I choose you, Snorlax!!!!!')
print()
time.sleep(0.2)


# Starting HPs
snorlax_hp = 200
jiggly_hp = 125

#Print out the starting HP:
print('Original HP:')
time.sleep(0.2)
print('- Snorlax HP:' + str(snorlax_hp))
time.sleep(0.2)
print('- Jigglypuff HP:' + str(snorlax_hp))
time.sleep(0.2)
print()
time.sleep(0.2)

while snorlax_hp > 0 and jiggly_hp > 0:
	print('Battle Options:')
	time.sleep(0.2)
	print('- [1] Sleep Heal')
	time.sleep(0.2)
	print('- [2] Tackle')
	time.sleep(0.2)
	print('- [3] Roundhouse Kick')
	time.sleep(0.2)
	print('- [4] Hyper Beam')
	time.sleep(0.2)
	print('- [5] Capture')
	time.sleep(0.2)
	your_move = input('Choose a move using the corresponding number: ')
	print()

	if your_move == '1':
		snorlax_hp = snorlax_hp + 50
		print('Snorlax uses Sleep Heal, his HP increases to ' + str(snorlax_hp))
	elif your_move == '2':
		snorlax_hp = jiggly_hp - 10
		print('Snorlax uses Tackle, and deals 10 damage to Jigglypuff!')
		time.sleep(0.2)
	elif your_move == '3':
		snorlax_hp = jiggly_hp - 30
		print('Snorlax uses Roundhouse Kick, and deals 30 damage to Jigglypuff!')
		time.sleep(0.2)
	elif your_move == '4':
		snorlax_hp = jiggly_hp - 40
		print('Snorlax uses Hyperbeam, and deals 30 damage to Jigglypuff!')
		time.sleep(0.2)
	elif your_move == '5':
		capture_roll = random.randint(0,125)
		if capture_roll > jiggly_hp:
			print('You have captured jigglypuff!')
			break
		else:
			print('You tried to capture jigglypuff, but it escaped!')
	print()

	# jigglypuff attacks
	enemy_move = random.randint(1,2)
	enemy_move = str(enemy_move)

	if enemy_move == '1':
		snorlax_hp = snorlax_hp - 30
		jiggly_hp = jiggly_hp + 30
		print('Jigglypuff uses Drink Blood and deals 30 HP of damage while recovering!')
		time.sleep(0.2)
	elif enemy_move == '2':
	     snorlax_hp = snorlax_hp - 50
	     jiggly_hp = jiggly_hp + 50
	     print('Jigglypuff uses Breathe Fire and deals 50 HP of damage while recovering!')
	     time.sleep(0.2)
	elif enemy_move == '3':
		 snorlax_hp = snorlax_hp - 70
		 jiggly_hp = jiggly_hp + 70
		 print('Jigglypuff uses Death Balloon and deals 70 HP of damage while recovering!')
		 time.sleep(0.2)
	elif enemy_move == '4':
		 snorlax_hp = snorlax_hp - 90
		 jiggly_hp = jiggly_hp + 90
		 print('Jigglypuff uses Lollypop Anesthetic and deals 90 HP of damage while recovering!')
		 time.sleep(0.2)
	elif enemy_move == '5':
		capture_roll = random.randint(0,125)
		if spike_roll > snorlax_hp:
			print('You have spiked Snorelax!')
			break
		else:
			print('You tried to spike Snorelax, but it escaped!')
	print()

	# snorelax counterattacks
	your_move = random.randint(1,2)
	your_move = str(your_move)

	if your_move == '1':
		snorlax_hp = snorlax_hp + 80
		print('Snorlax uses Sleep Heal, his HP increases to ' + str(snorlax_hp))
	elif your_move == '2':
		snorlax_hp = jiggly_hp - 30
		print('Snorlax uses Tackle, and deals 30 damage to Jigglypuff!')
		time.sleep(0.2)
	elif your_move == '3':
		snorlax_hp = jiggly_hp - 60
		print('Snorlax uses Roundhouse Kick, and deals 60 damage to Jigglypuff!')
		time.sleep(0.2)
	elif your_move == '4':
		snorlax_hp = jiggly_hp - 90
		print('Snorlax uses Hyperbeam, and deals 30 damage to Jigglypuff!')
		time.sleep(0.2)
	elif your_move == '5':
		capture_roll = random.randint(0,125)
		if capture_roll > jiggly_hp:
			print('You have captured jigglypuff!')
			break
		else:
			print('You tried to capture jigglypuff, but it escaped!')
	print()

	# Check for overkill and if so, set hp to 0
	if snorlax_hp < 0:
		snorlax_hp = 0
	if jiggly_hp < 0:
		jiggly_hp = 0

	print('Updated HP!')
	time.sleep(0.2)
	print('- Snorlax HP:' + str(snorlax_hp))
	time.sleep(0.2)
	print('- Jigglypuff HP:' + str(snorlax_hp))
	time.sleep(0.2)
	print()
	time.sleep(0.2)

if snorlax_hp == 0:
	print('Snorlax has been defeated! Winner: Jigglypuff!')
elif jiggly_hp == 0:
	print('Jiggly puff has been defeated! Winner: Snorlax!')