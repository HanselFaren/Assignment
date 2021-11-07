my_dictionary = {
    "Python": "A general-purpose, high-level programming language with an emphasis on code readability.",
    "Go": "A statically typed, compiled programming language designed at Google",
    "C++": "A general purpose programming language that can be used to create small programs or large applications.",
    "Java": "A high-level, class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible",
    "SQL": "It is a special-purpose programming language used for getting information from and updating databases.",
}

result = dict(sorted(my_dictionary.items(), key=lambda x: x[0]))

for k, v in result.items():
    print(k)
    print(v)
    print()

# notes : maaf masi bingung untuk print sesuai urutan yang ditentukan jadinya aku mengakali dengan urutan huruf
#         logika belum masuk jika menggunakan for atau def tetapi setauku memakai get()