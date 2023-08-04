#!/usr/bin/python3
import cmd
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
            if name in Hero.hero_names:
                for h in Hero.hero_collection:
                    if h.name == name:
                        h.info()
            else:
                print(f"{name} is not a hero")
        else:
            print('Usage stats <name>')
        
    def help_stats(self):   
        print ('\n'.join(['Displays a hero\'s stats',
                         'Usage stats <name>'
                         ]))
    
    def do_craft(self, name)
        
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