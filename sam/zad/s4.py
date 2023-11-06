def entry_exit_seq(employee_id, seq):
	employee_found = False
	output = []
	for item in seq:
		if item == employee_id and not employee_found:
			employee_found = True
		elif item == employee_id and employee_found:
			break
		else:
			output.append(item)
	return output
print(entry_exit_seq(8, (1,2,3))) # [8]
print(entry_exit_seq(8, (1,8,3,4,8,8,9,2))) # [8,8,8]
print(entry_exit_seq(8, (1,2,8,5,1,2,9))) # [8,1,2]