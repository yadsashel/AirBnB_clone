![65f4a1dd9c51265f49d0](https://github.com/yadsashel/AirBnB_clone/assets/124151323/5bbf5078-0220-4766-afad-e20b0ec3557b)

# AirBnB Clone Project

## Description

This project aims to deploy a simple copy of the AirBnB website on your server. It covers fundamental concepts of the higher level programming track.

## Installation

## 1.Clone the Repository:

```bash
git clone https://github.com/yad_sashel/AirBnB_clone.git

```

## 2.Navigate to the Project Directory:

```bash
cd AirBnB_clone

```

## 3.Install Dependencies:

```bash
pip install -r requirements.txt

```

## 4.Run the Project:

```bash
python main.py

```

## Command Interpreter

The command interpreter, also referred to as the console, is a tool designed to manipulate data without a visual interface, similar to a shell. It allows users to perform various operations such as creating, updating, deleting, and managing objects within the project. The command interpreter serves as a crucial tool for development and debugging purposes.

### How to Start

```bash
$ python3 console.py

```

in shell it should work like this in interactive mode:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

```
But also in non-interactive mode: (like the Shell project in C):

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

```

### How to Use

Once the command interpreter is running, you can interact with it using various commands. These commands enable you to perform operations such as creating, updating, deleting, and managing objects within the project. Below are some example commands:

create <classname>: Create a new instance of the specified class.
show <classname> <id>: Display details of a specific instance.
update <classname> <id> <attribute> <value>: Update the specified attribute of an instance.
destroy <classname> <id>: Delete a specific instance.
Refer to the project documentation or use the help command within the command interpreter for a complete list of available commands and their usage

### Examples

Below are some examples demonstrating the usage of the command interpreter:

```bash
$ python3 console.py
(hbnb) create BaseModel
5bc44e6f-a938-4752-929b-d5e29b015dff
(hbnb) show BaseModel 5bc44e6f-a938-4752-929b-d5e29b015dff
[BaseModel] (5bc44e6f-a938-4752-929b-d5e29b015dff) {'id': '5bc44e6f-a938-4752-929b-d5e29b015dff', 'created_at': '2024-02-10T12:00:00', 'updated_at': '2024-02-10T12:00:00'}
(hbnb) update BaseModel 5bc44e6f-a938-4752-929b-d5e29b015dff name "New Name"
(hbnb) show BaseModel 5bc44e6f-a938-4752-929b-d5e29b015dff
[BaseModel] (5bc44e6f-a938-4752-929b-d5e29b015dff) {'id': '5bc44e6f-a938-4752-929b-d5e29b015dff', 'created_at': '2024-02-10T12:00:00', 'updated_at': '2024-02-10T12:00:00', 'name': 'New Name'}
(hbnb) destroy BaseModel 5bc44e6f-a938-4752-929b-d5e29b015dff
(hbnb) show BaseModel 5bc44e6f-a938-4752-929b-d5e29b015dff
** no instance found **

```

### Authors
 - Yazide Salhi
 - Email: yazidepk@gmail.com
 - GitHub: yad_sashel
