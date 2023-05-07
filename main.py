#  Exercise 1

def create_file(names_file):
    names = ["Magda", "Miri", "Stefano", "Lance", "Berni", "Gianluca", "Maria", "Aurelia", "Max", "Franci"]
    with open(names_file, "w") as file:
        file.write(",".join(names))


create_file("names")


#  Exercise 2

def transform_to_row(input_file, output_file):
    with open(input_file, "r") as file:
        contents = file.read()
        words = contents.split(",")
    with open(output_file, "w") as output:
        for word in words:
            output.write(word.strip() + "\n")


transform_to_row("names", "output_names")


#  Exercise 3

def add_greeting(input_file, output_file):
    with open(input_file, "r") as file:
        lines = file.readlines()
    words = [f"Hello {name.strip()}" for line in lines for name in line.split(",")]
    with open(output_file, "w") as output:
        output.write("\n".join(words))


add_greeting("output_names", "hello_names")


#  Exercise 4

def strip_greeting(input_file, output_file):
    with open(input_file, "r") as file:
        lines = file.readlines()
    new_lines = [line.replace("Hello ", "") for line in lines]
    new_text = "".join(new_lines)
    with open(output_file, "w") as output:
        output.write(new_text)


strip_greeting("hello_names", "no_hello_names")
