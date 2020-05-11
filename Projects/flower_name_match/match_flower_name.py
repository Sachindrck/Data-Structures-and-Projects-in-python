# Write your code here
# HINT: create a dictionary from flowers.txt
filename = "flowers.txt"
flowers = {}
def flower_names(filename):
    with open(filename) as f:
        file_data = f.readlines()
        for line in file_data:
            l = line.split(":")
            flowers[l[0]] = l[1].strip()

flower_names(filename)

# HINT: create a function to ask for user's first and last name
if __name__ == "__main__":
    name = input("Enter your First [space] Last name only: ")
    for n_f_l, f_p in flowers.items():
        if n_f_l == name[0]:
            print("Unique flower name with the first letter: {}".format(f_p))
