#!/usr/bin/python3
import cmd
import inspect
import readline
from myclasses import *

class MainMenu(cmd.Cmd):
    intro = '\n'.join(["Welcome to my mini RPG",
                      "type help or '?' for help"
                      ])
    ruler = '-'
    prompt = ">>>"
    
    doc_header = '\n'.join(['Bro', 'The', 'Fuque!?'])
    undoc_header = "No help!"
    weapons = ['Dagger', 'Hammer', 'Sword']
    #def do_help(self, arg)
    #    return super().do_help(arg)
    
    def onecmd(self, line):
        if line.strip() in ["q", "quit", "exit"]:
            return self.do_EOF(line)
        if line.strip() in ["h", "help", "welp"]:
            return self.do_help(line)
        #if line.startswith("stats") or line.startswith("info"):
        #    return self.do_stats(line)
        return super().onecmd(line)
    
    def do_hero(self, name):
        if name:
            hero = Hero(name)
        else:
            print('Usage hero <name>')
            
    def do_stats(self, name):
        if name:
            if Hero.exists(name):
                instance = Hero.correspond(name)
                instance.info()
            else:
                print(f"{name} is not a hero")
        else:
            print('Usage stats <name>')
        
    def help_stats(self):   
        print ('\n'.join(['Displays a hero\'s stats',
                         'Usage stats <name>'
                         ]))
    
    def do_craft(self, line):
        args = line.split()
        if len(args) == 2:
            name, label = args
            if name in globals() and issubclass(globals()[name], Weapon):
                weapon = globals()[name](label)
                print(f"Crafted a {name} with label '{label}'")
            else:
                print(f"{name} must be a weapon. Type hcraft for more info")
        else:
            print('Usage craft <weapon_name> <weapon_label>')
            
    def complete_craft(self, text, line, begidx, endidx):
        weapons = [name for name in dir() if inspect.isclass(globals().get(name, None)) and issubclass(globals()[name], Weapon)
           and (globals()[name] != Weapon)]
        completion = [weapon for weapon in self.weapons if weapon.startswith(text)]
        return completion
    
    def do_equip(self, line):
        args = line.split()
        if len(args) == 2:
            hero, wp = args
            if not Hero.exists(hero):
                print(f"{hero} in not a hero")
            elif not Weapon.exists(wp):
                print(f"{wp} in not a weapon")
            else:
                hero_instance = Hero.correspond(hero)
                weapon = Weapon.correspond(wp)
                hero_instance.equip_weapon(weapon)
        else:
            print("Usage: equip <hero> <weapon>")
    
    def complete_equip(self, text, line, begidx, endidx):
        if not text:
            return Hero.hero_names[:]
        args = line.split()
        if len(args) == 1:
            return [name for name in Hero.hero_names if name.startswith(text)]
        elif len(args) == 2:
            hero = args[1]
            if Hero.exists(hero):
                return [name for name in Weapon.wp_names if name.startswith(text)]
                
    def complete_hero_related_commands(self, text, line, begidx, endidx):
        if not text:
            completions = Hero.hero_names[:]
        else:
            completions = [name for name in Hero.hero_names if name.startswith(text)]
        return completions
    
    complete_stats = complete_hero_related_commands
    
    def help_hero(self):
        print ('\n'.join(['Creates a Hero',
                         'Usage hero <name>'
                         ]))
            
    
    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    MainMenu().cmdloop()