
from Prac07.programminglanguage import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby","Dynamic",True,1995)
    python = ProgrammingLanguage("Python","Dynamic",True,1991)
    vb = ProgrammingLanguage("Visual Basic","Static",False,1991)
    language = [ruby, python, vb]
    print(ruby)
    print(python)
    print(vb)

    print("The dynamically typed languages are:")
    for item in language:
        item.is_dynamic()


main()
