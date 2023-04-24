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

def determine_sequential_or_random():
	import random
	sequential_or_random = random.randint(1, 10)
	if(sequential_or_random <= 3):
		return False
	else:
		return True

def assign_sequential_or_random(is_sequential, infected_computers_countdown_timers, assign_ip, index_accessor):
	if(index_accessor is None):
		if(is_sequential):
			for l in range(len(infected_computers_countdown_timers)):
				if(infected_computers_countdown_timers[l][0] == -1):
					infected_computers_countdown_timers[l][0] = assign_ip
					infected_computers_countdown_timers[l][1] = True
					break
				else:
					continue
		else:
			for m in range(len(infected_computers_countdown_timers)):
				if(infected_computers_countdown_timers[m][0] == -1):
					infected_computers_countdown_timers[m][0] = assign_ip
					infected_computers_countdown_timers[m][1] = False
					break
				else:
					continue
	else:
		if(is_sequential):
			for z in range(len(infected_computers_countdown_timers)):
				if(infected_computers_countdown_timers[z][0] == -1):
					infected_computers_countdown_timers[z][0] = infected_computers_countdown_timers[index_accessor][0]
					infected_computers_countdown_timers[z][1] = True
					break
				else:
					continue
		else:
			for y in range(len(infected_computers_countdown_timers)):
				if(infected_computers_countdown_timers[y][0] == -1):
					infected_computers_countdown_timers[y][0] = infected_computers_countdown_timers[index_accessor][0]
					infected_computers_countdown_timers[y][1] = False
					break
				else:
					continue


def is_ip_infected(ip_addresses, ip_address, list_accessor, were_computers_infected):
	if type(ip_address) is not list:
		if(ip_addresses[ip_address] == 2):
			ip_addresses[ip_address] = 3
			for i in range(len(were_computers_infected)):
				if(were_computers_infected[i] is False):
					were_computers_infected[i] = True
					break
				else:
					continue
			return True
		else:
			return False
	else:
		if(ip_addresses[ip_address[list_accessor][0]] == 2):
			ip_addresses[ip_address[list_accessor][0]] = 3
			for j in range(len(were_computers_infected)):
				if(were_computers_infected[j] is False):
					were_computers_infected[j] = True
					break
				else:
					continue
			return True
		else:
			return False

def activate_random_reinitialize_countdown(infected_computers_countdown_timers, index_accessor):
	infected_computers_countdown_timers[index_accessor][0] = -1
	infected_computers_countdown_timers[index_accessor][1] = False
	infected_computers_countdown_timers[index_accessor][2] = 20
	return 1

def sequential_scanning_worm_simulation(ip_addresses, tab):
	import random
	ip_addresses[2010] = 3
	number_of_infected_machines = 1
	number_of_active_random_infected = 0
	is_sequential = False
	is_sequential = determine_sequential_or_random()
	infected_computers_countdown_timers = [[-1, False, 20]*1 for i in range(500)]
	if(is_sequential):
		infected_computers_countdown_timers[0][0] = 2010
		infected_computers_countdown_timers[0][1] = True
		infected_computers_countdown_timers[0][2] = 0
	else:
		number_of_active_random_infected += 1
	were_computers_infected = [False]*500
	number_of_time_ticks = 1
	total_ticks_recorded = False
	for i in range(1000):
		for j in range(len(were_computers_infected)):
			if(were_computers_infected[j] is True):
				number_of_infected_machines += 1
				were_computers_infected[j] = False
		for k in range(4 * number_of_active_random_infected):
			random_ip = random.randint(0, 49999)
			if(is_ip_infected(ip_addresses, random_ip, k, were_computers_infected)):
				is_sequential = determine_sequential_or_random()
				assign_sequential_or_random(is_sequential, infected_computers_countdown_timers, random_ip, None)
		for m in range(len(infected_computers_countdown_timers)):
			if(infected_computers_countdown_timers[m][0] != -1 and infected_computers_countdown_timers[m][2] == 0):
				for n in range(4):
					if(infected_computers_countdown_timers[m][0] != 49999):
						if(is_ip_infected(ip_addresses, infected_computers_countdown_timers, m, were_computers_infected)):
							is_sequential = determine_sequential_or_random()
							assign_sequential_or_random(is_sequential, infected_computers_countdown_timers, None, m)
						infected_computers_countdown_timers[m][0] += 1
					else:
						infected_computers_countdown_timers[m][0] = 0
		for o in range(len(infected_computers_countdown_timers)):
			if(infected_computers_countdown_timers[o][0] != -1 and infected_computers_countdown_timers[o][2] != 0):
				infected_computers_countdown_timers[o][2] -= 1
				if(infected_computers_countdown_timers[o][2] == 0 and infected_computers_countdown_timers[o][1] is False):
					number_of_active_random_infected += activate_random_reinitialize_countdown(infected_computers_countdown_timers, o)
				else:
					continue
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
		sequential_scanning_worm_simulation(ip_addresses, tab)
		if(i == 0):
			tab = "\t"
		else:
			tab = "\t\t"

main()
