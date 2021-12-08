# importing sys package to take command line inputs
import sys

# taking input from command line
command = sys.argv
command.pop(0)

# lists to store current completed and pending tasks
tasks = []
completed = []

# if task.txt file doesn't already exist then create one
try:
	file = open("task.txt",'r')
except:
	file = open("task.txt",'w')
	file.close()


# if completed.txt file doesn't already exist then create one
try:
	file = open("completed.txt",'r')
except:
	file = open("completed.txt",'w')
	file.close()

# function to read data from the task.txt file and completed.txt file
def readtasks():
	global tasks
	global completed

	# open the text file containing tasks
	taskfile = open("task.txt",'r')
	lines = taskfile.readlines()
	# read the dile line by line
	for line in lines:
		words = line.split()
		# storing the priority and task seperately in dictionary and storing the dixtionary as a seperate task
		tasks.append({"priority":int(words[0]),"task":" ".join(words[1:]).strip()})
	taskfile.close()

	# open the text file containing completed tasks
	compfile = open("completed.txt",'r')
	lines = compfile.readlines()
	# reading it line by line
	for line in lines:
		words = line.split()
		# storing the task in a list
		completed.append(" ".join(words).strip())
	compfile.close()

	# return both the lists
	return tasks,completed

# function to update the task.txt and complete.txt file
def writetasks():
	global tasks
	global completed

	# opening the file task.txt in write mode
	taskfile = open("task.txt",'w')
	for task in tasks:
		# writing the priority and then the task name
		taskfile.write(str(task['priority'])+" ")
		taskfile.write(str(task['task'])+" ")
		taskfile.write("\n") # line break
	taskfile.close()

	# opening completed.txt
	compfile = open("completed.txt",'w')
	# adding all the completed tasks on new lines.
	for comp in completed:
		compfile.write(comp)
		compfile.write("\n")
	compfile.close()
	

# function which prints the usage of the command line
def help():
	print("Usage :-")
	print('$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list')
	print('$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order')
	print('$ ./task del INDEX            # Delete the incomplete item with the given index')
	print('$ ./task done INDEX           # Mark the incomplete item with the given index as complete')
	print('$ ./task help                 # Show usage')
	print('$ ./task report               # Statistics')

# this function prints all the pending tasks and their respective priority
def pending():
	# if there are no pending tasks
	if(len(tasks) == 0):
		print("There are no pending tasks!")
		return
	# if there are pending tasks print the 
	# serial number, task then priority
	index = 1
	for task in tasks:
		print("{}. {} [{}]".format(index,task['task'],task['priority']))
		index+=1

# function to print the completed tasks
def complete():
	index = 1
	# print the serial number then the completed task
	for task in completed:
		print("{}. {}".format(index,task))
		index+=1

# function to delete a task
def delete(ind):
	# indices must start from 1 
	if(ind == 0):
		print("Error: task with index #{} does not exist. Nothing deleted.".format(ind))
		return
	# delete index if it exist
	try:
		tasks.pop(ind-1)
		print("Deleted task #{}".format(ind))
	# if doesnt exist then print error message
	except:
		print("Error: task with index #{} does not exist. Nothing deleted.".format(ind))

# function to mark task as done
def done(ind):
	# inices must start from 1
	if(ind == 0):
		print("Error: no incomplete item with index #0 exists.")
	# mark index completed if it exist
	try:
		task = tasks.pop(ind-1)
		completed.append(task['task']) # add task to the completed list 
		print("Marked item as done.")
	# if doesnt exist then print error message
	except:
		print("Error: no incomplete item with index {} exists.".format(ind))

# function to print the entire report
def report():
	# print the number of pending tasks
	print("Pending : {}".format(len(tasks)))
	pending() # call pending function to print them
	print() # line break
	# print the number of completed tasks
	print("Completed : {}".format(len(completed)))
	complete() # call the completed function to print them 

# add task to the list of tasks
def additem(priority,task):
	# add the task and its priority as a dictionary
	tasks.append({"priority":priority,"task":task})
	# sort task list according to priority
	tasks.sort(key = lambda x: x['priority'])
	# print message 
	print("Added task: \"{}\" with priority {}".format(task,priority))

# call readtask function  to read pending and completed tasks into respective lists
readtasks()
# sort the task list according to priority
tasks.sort(key = lambda x: x['priority'])

# if no command is passed / help command is passed then display help
if(len(command) == 0 or command[0] == 'help'):
	help()
# ls command lists all the pending tasks so call pending()
elif(command[0] == 'ls'):
	pending()
# del command deletes a task at given index
elif(command[0] == 'del'):
	try:
		# if index is given as integer
		ind = int(command[1])
		delete(ind) # call delete()
	except:
		# if no index is passed or if it is not an integer
		print("Error: Missing NUMBER for deleting tasks.")
	# done caommand marks a task done at given index
elif(command[0] == 'done'):
	try:
		# if index is given as integer
		ind = int(command[1])
		done(ind)
	except:
		# if no index is passed or if it is not an integer
		print("Error: Missing NUMBER for marking tasks as done.")
# report command prints all the tasks, completed or pending
elif(command[0] == 'report'):
	report()
# add command adds a new task to the pending tasks
elif(command[0] == 'add'):
	# if not all arguments(priority and task string) are passed
	if(len(command) <= 2):
		print("Error: Missing tasks string. Nothing added!")
	else:
		try:
			# add item to the task list
			additem(int(command[1])," ".join(command[2:]).strip())
		except:
			# if priority is not passed properly as integer
			print("Error: Missing NUMBER for task priority.")
# if no command matches then print help
else:
	help()

# update the files task.txt and completed.txt
# according to the new task and completed list
writetasks()