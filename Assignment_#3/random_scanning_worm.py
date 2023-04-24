#!/usr/bin/env python3

def assign_ip_addresses():
	total_ip_addresses = [0] * 50000
	multiples_of_1000 = 0
	for i in range(0, 50000):
		total_ip_addresses[i] = 1
	while multiples_of_1000 < 50000:
		for j in range(multiples_of_1000+1, multiples_of_1000+11):
			total_ip_addresses[j] = 2
		multiples_of_1000 += 1000
	return total_ip_addresses

def random_scanning_worm_simulation(ip_addresses, tab):
	import random
	ip_addresses[2010] = 3
	number_of_infected_machines = 1
	number_of_active_infected_machines = 1
	infected_computers_countdown_timers = [20]*500
	were_computers_infected = [False]*500
	number_of_time_ticks = 1
	total_ticks_recorded = False
	for i in range(600):
		for j in range(len(were_computers_infected)):
			if(were_computers_infected[j] is True):
				number_of_infected_machines += 1
				were_computers_infected[j] = False
		for k in range(4 * number_of_active_infected_machines):
			random_ip = random.randint(0, 49999)
			if(ip_addresses[random_ip] == 2):
				ip_addresses[random_ip] = 3
				for infect in range(len(were_computers_infected)):
					if(were_computers_infected[infect] is False):
						were_computers_infected[infect] = True
						break
					else:
						continue
		for l in range(len(infected_computers_countdown_timers)):
			if(infected_computers_countdown_timers[l] < 20):
				infected_computers_countdown_timers[l] -= 1
				if(infected_computers_countdown_timers[l] == 0):
					number_of_active_infected_machines += 1
					infected_computers_countdown_timers[l] = 20
			else:
				continue
		for m in range(len(were_computers_infected)):
			if(were_computers_infected[m] is True):
				for n in range(len(infected_computers_countdown_timers)):
					if(infected_computers_countdown_timers[n] == 20):
						infected_computers_countdown_timers[n] -= 1
						break
					else:
						continue
		if(tab):
			print(tab + str(number_of_infected_machines))
		else:
			print(number_of_infected_machines)
		if(number_of_infected_machines == 500 and total_ticks_recorded is False):
			print(f"All machines infected at {number_of_time_ticks}")
			total_ticks_recorded = True
		elif(number_of_infected_machines < 500):
			number_of_time_ticks += 1
		else:
			continue

def main():
	tab = None
	for i in range(3):
		ip_addresses = assign_ip_addresses()
		random_scanning_worm_simulation(ip_addresses, tab)
		if(i == 0):
			tab = "\t"
		else:
			tab = "\t\t"

main()
