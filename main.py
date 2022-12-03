print('''        ,_   ,-"-._
                      .___   \'-._\  \`~,_
                      _'. `~-,\ ~-.|     \',
                    .'   \    |    \  '  /  \
                   / ~-.  |   '    | .' ;  ; \
                   |.--    \ . '   /    |  . |\
                   / ., `\ |     `___  /  .  ||
                   |/  \  \/\__.-'   `\;    / /
                        \ /      .--.  |   / /
                         /,     /    \ / .' /
                        / \\   /."".  |;  '(__,
                      ,_|/_\ ._/___.\_|'   .-.;_,
                     "==;_o_\ /_o__,==" \ / )) .'__,
                    ,="/    |      "=,   ; _/   _.'
                    %/\__..)_,)`-.__     /\%\%\.`.__,
                  .%/%/` .-._ _..-. `      `"%\%.--'
                     ;   `;-.:..-'/|          |./
                 _.--|     ).___.-||          ;  `'--._
               .'    |  o /|     / ;          /        `,
              /      |   ( `----' /          /           \
             /       |    '------'         /`             \
            /         \  (     ,        .'`                \
           /           '._`---'     _.-'                    ;
          /      /     `._`""""""""`                         ;
         /     .'      ,__/`~|~`\                            |
        /    ooooo,    \  \ '`)- |            ,              |
      .'   d888888888ooo\ /'-'\ /o8888888o,    \             |
    .'    888888888888888'._|_.'888888888888b   \            |
  .'      888888888888888888888888888888888888, |            ;
     jgs   Y88888888888888888888888888888888888b;            /''')

print("Welcom to Tresure Island. Your mission is to find th treasure")

tape = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n')
tape_lower_cas = tape.lower()
if tape_lower_cas == "left":
    typ = input("You\'ve come to a lake. There is an island in the middle of the like. type 'wait' to wait for a boat. Type 'swim' to swim across  \n")
    typ_lower_cas = typ.lower()
    if typ_lower_cas == "wait":
        choose = input("Your arrive at the island unharmed. There is a hause with 3 doors. one red, one yellow and one blue. Which colour do you choose? \n")
        choose_lower_cas = choose.lower()
        if choose_lower_cas == "yellow":
             print("You Win!")
        else:
            print("It's a room full of fire. Game Over.")        
    else:
             print("It's a room full of fire. Game Over.") 

else:
    print("It's a room full of fire. Game Over.")


