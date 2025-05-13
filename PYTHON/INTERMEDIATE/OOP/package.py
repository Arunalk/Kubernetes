from prettytable import PrettyTable

table = PrettyTable()
'''
method usage
'''
table.add_column("Pokemon Name", ["Pikachu","Squirtell","Charmander"])
table.add_column("Type", ["Electric","Water", "Fire"])
'''
overriding attributes
'''
table.header_style = "upper"
table.align = "r"
print(f"table\n{table}")
