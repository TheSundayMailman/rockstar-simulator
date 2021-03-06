from rockstar import Rockstar



# graphics
divider = "\n==========================================================================="

concert = """
                          ,     
                      ,   |     
   _,,._              |  0'     
 ,'     `.__,--.     0'         
/   .--.        |           ,,, 
| [=========|==|==|=|==|=|==___]
\   "--"  __    |           ''' 
 `._   _,'  `--'                
    ""'     ,   ,0     ,        
            |)  |)   ,'|        
  ____     0'   '   | 0'        
  |  |             0'           
 0' 0'"""

party = """
                                   .''.
       .''.      .        *''*    :_\/_:     .
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :    /)\   ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::.  | ' *''*    * '.\*/.'_\(/_ '.':'.'
 : /\ : :::::  =  *_\/_*     -= o =- /)\     '  *
  '..'  ':::' === * /\ *     .'/.\*.  ' ._____
      *        |   *..*         :       |.   |' .---"|
        *      |     _           .--'|  ||   | _|    |
        *      |  .-'|       __  |   |  |    ||      |
     .-----.   |  |' |  ||  |  | |   |  |    ||      |
 ___'       ' /"\ |  '-."".    '-'   '-.'    '`      |____
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                       ~-~-~-~-~-~-~-~-~-~   /|
 -~-~-    )      ~-~-~-~-~-~-~-~  /|~       /_|\ 
        _-H-__  -~-~-~-~-~-~     /_|\    -~======-~
~-\XXXXXXXXXX/~     ~-~-~-~     /__|_\ ~-~-~-~
~-~-~-~-~-~    ~-~~-~-~-~-~    ========  ~-~-~-~
      ~-~~-~-~-~-~-~-~-~-~-~-~-~ ~-~~-~-~-~-~
                        ~-~~-~-~-~-~"""

rest = """
    ) )        /\ 
   =====      /  \ 
  _|___|_____/ __ \____________
 |::::::::::/ |  | \:::::::::::|
 |:::::::::/  ====  \::::::::::|
 |::::::::/__________\:::::::::|
 |_________|  ____  |__________|
  | ______ | / || \ | _______ |
  ||  |   || ====== ||   |   ||
  ||--+---|| |    | ||---+---||
  ||__|___|| |   o| ||___|___||
  |========| |____| |=========|
 (^^-^^^^^-|________|-^^^--^^^)
 (,, , ,, ,/________\,,,, ,, ,)
','',,,,' /__________\,,,',',;;"""

tomb = """
       ,-=-.       ______     _
      /  +  \     />----->  _|R|_
      | ~~~ |    // -/- /  |_ I _|
      |R.I.P|   //  /  /     |P|
\,vV,,|_____|V,//_____/VvV,v,|_|/,,vhjwv/,
"""

play_again = """
 ____________________ 
/                    \ 
|     YOU  KINDA     | 
|        ROCK!       | 
\____________________/
         !  !
         !  !
         L_ !
        / _)!
       / /__L
 _____/ (____)
        (____)
 _____  (____)
      \_(____)
         !  !
         !  !
         \__/
"""

you_rock = """
 ____________________ 
/                    \ 
|     YOU ROCK!!     | 
|     ----------     | 
\____________________/
         !  !
         !  !
         L_ !
        / _)!
       / /__L
 _____/ (____)
        (____)
 _____  (____)
      \_(____)
         !  !
         !  !
         \__/
"""

you_legend = """
 ____________________ 
/                    \ 
|     YOU ARE A      | 
|     LEGEND!!!!     | 
\____________________/
         !  !
         !  !
         L_ !
        / _)!
       / /__L
 _____/ (____)
        (____)
 _____  (____)
      \_(____)
         !  !
         !  !
         \__/
"""



# handles all tour logics
def handle_tour(player):
  if player.energy < 20:
    print(divider)
    print("\nOh no! {} has no energy to perform...so {} takes a rest instead...".format(player.name, player.pronoun))
    player.fail_tour()
  elif player.popularity < 100:
    print(divider)
    print("\n{} tours around the country to perform!!!".format(player.name))
    print("Oh no...{} seems to be losing it with {} fans...".format(player.pronoun, player.posessive))
    player.unpopular_tour()
  else:
    print(divider)
    print("\n{} tours around the country to perform!!!".format(player.name))
    print(concert)
    player.tour()



# handles all party logics
def handle_party(player):
  if player.money < player.cost:
    print(divider)
    print("\n{} is too broke to party...".format(player.name))
    print("So {} just sits and mopes around for awhile...".format(player.pronoun))
    player.broke_party()
  elif player.energy < 15:
    print(divider)
    print("\n{} does not have enough energy to party...".format(player.name))
    print("So {} just sits and mopes around for awhile...".format(player.pronoun))
    player.fail_party()
  else:
    print(divider)
    print(party)
    print("\n{} parties like a rockstar!!!".format(player.name))
    player.party()



# handles all rest logics
def handle_rest(player):
  print(divider)
  print(rest)
  print("\n{} goes on a haitus...".format(player.name))
  player.rest()


# handles game over
def handle_death(player):
  print(tomb)
  print("{} has died from partying too hard...".format(player.name))
  if player.popularity < 50:
    print("And left behind little fans to remember {}, sad...".format(player.posessive))
  else:
    print("But at least {} will be remembered as a rock legend!".format(player.pronoun))



# handles all ending scenarios
def handle_ending(player):
  print(divider)
  print("After one year of being a rockstar,")
  if player.popularity <= 50:
    print(play_again)
    print("{} is not very popular...".format(player.name))
  elif player.popularity > 50 and player.popularity <= 120:
    print(you_rock)
    print("{} is somewhat popular...".format(player.name))
  else:
    print(you_legend)
    print("{} is very popular!".format(player.name))
