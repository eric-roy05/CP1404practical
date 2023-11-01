class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, name, typing, reflection, year):

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if the programming language is dynamically typed."""
        return self.typing.lower() == 'dynamic'

    def __str__(self):
        """Return a string representation of the programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"


if __name__ == "__main__":
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)
    print(ruby)
    print(visual_basic)

    languages_list = [python, ruby, visual_basic]

    print("\nThe dynamically typed languages are:")
    for language in languages_list:
        if language.is_dynamic():
            print(language.name)
