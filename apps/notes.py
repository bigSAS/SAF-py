def run_program():
	print(options)
	print("")
	command = input("Type 'option' which you'd like to do: ").lower()
	if command in commands:
		option = commands[command]
		option()
	else:
		print('Invalid option')
		print('-'*10)
		run_program()
	run_program()


def list_notes():
	i = 1
	for note in notes:
		print(f'{i}. {note}')
		i = i + 1


def add_note():
	note = input("Write new note: ")
	if len(note) > 0:
		notes.append(note)
		list_notes()
	else:
		print('Invalid note, write again')
		add_note()
	
def delete_note():
	list_notes()
	command_delete = input("Which note you'd like to delete? ")
	try:
		command_delete_int = int(command_delete)
		notes.pop(command_delete_int - 1)
		list_notes()
	except:
		print('Invalid number')
		delete_note()
			
def edit_note():
	list_notes()
	command_edit = input("Which note you'd like to edit? ")
	command_edit_int = int(command_edit)
	#do poprawy
	if notes[command_edit_int -1] in range(len(notes - 1)):
		try:
			command_edit_index = command_edit_int - 1
			print(notes[command_edit_index])
			new_note = input('Write your note and press Enter: ')
			notes.pop(command_edit_index)
			notes.insert(command_edit_index, new_note)
			list_notes()
		except:
			print("Invalid number, please type which note you'd like to edit: ")
			print("-"*10)
			edit_note()
	else:
		print("Invalid number, please type which note you'd like to edit: ")
		list_notes()
		
def quit_notes_app():
		print("NoteApp is closing... .. .  .   .  CLOSED!")
		import sys
		sys.exit()
		


options = """
What are you going to do?
List your notes - type 'list'
Add new note - type 'add'
Delete note - type 'delete'
Edit note - type 'edit'
"""

commands = {
		"list": list_notes, 
		"add": add_note, 
		"delete": delete_note, 
		"edit": edit_note, 
		"quit": quit_notes_app,
}

notes = [
	"elo melo 520",
	"west coast is the best"
	]
	
option_is_valid = False

delete_command_is_valid = False


run_program()
