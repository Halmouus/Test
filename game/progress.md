class RPGCmd(Cmd):
    # ... other methods ...

    def do_craft(self, arg):
        weapon_classes = ["dagger", "sword", "hammer"]  # List of available weapon classes

        if not arg:
            print("Available weapon classes:", ", ".join(weapon_classes))
            return

        args = arg.split()
        if len(args) < 2:
            print("Usage: craft <weapon_class> <weapon_name>")
            return

        weapon_class = args[0]
        weapon_name = " ".join(args[1:])

        if weapon_class not in weapon_classes:
            print("Invalid weapon class. Available weapon classes:", ", ".join(weapon_classes))
            return

        if weapon_class == "dagger":
            weapon = Dagger(weapon_name)
        elif weapon_class == "sword":
            weapon = Sword(weapon_name)
        elif weapon_class == "hammer":
            weapon = Hammer(weapon_name)
        else:
            print("Invalid weapon class.")
            return

        print(f"Crafted {weapon_class} '{weapon_name}'!")

    def complete_craft(self, text, line, begidx, endidx):
        if not text:
            completions = weapon_classes[:]
        else:
            completions = [w_class for w_class in weapon_classes if w_class.startswith(text)]

        return completions
