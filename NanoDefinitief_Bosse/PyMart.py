import Diary
import Number_Guess


def choiceMenu():
    print(" PPPPPPPPPPPPPPPPP                            MMMMMMMM               MMMMMMMM                                               tttt\n"
          " P::::::::::::::::P                           M:::::::M             M:::::::M                                            ttt:::t\n"
          " P::::::PPPPPP:::::P                          M::::::::M           M::::::::M                                            t:::::t\n"
          " PP:::::P     P:::::P                         M:::::::::M         M:::::::::M                                            t:::::t\n"
          "  P::::P     P:::::Pyyyyyyy           yyyyyyyM::::::::::M       M::::::::::M  aaaaaaaaaaaaa   rrrrr   rrrrrrrrr   ttttttt:::::ttttttt\n"
          "  P::::P     P:::::P y:::::y         y:::::y M:::::::::::M     M:::::::::::M  a::::::::::::a  r::::rrr:::::::::r  t:::::::::::::::::t\n"
          "  P::::PPPPPP:::::P   y:::::y       y:::::y  M:::::::M::::M   M::::M:::::::M  aaaaaaaaa:::::a r:::::::::::::::::r t:::::::::::::::::t\n"
          "  P:::::::::::::PP     y:::::y     y:::::y   M::::::M M::::M M::::M M::::::M           a::::a rr::::::rrrrr::::::rtttttt:::::::tttttt\n"
          "  P::::PPPPPPPPP        y:::::y   y:::::y    M::::::M  M::::M::::M  M::::::M    aaaaaaa:::::a  r:::::r     r:::::r      t:::::t\n"
          "  P::::P                 y:::::y y:::::y     M::::::M   M:::::::M   M::::::M  aa::::::::::::a  r:::::r     rrrrrrr      t:::::t\n"
          "  P::::P                  y:::::y:::::y      M::::::M    M:::::M    M::::::M a::::aaaa::::::a  r:::::r                  t:::::t\n"
          "  P::::P                   y:::::::::y       M::::::M     MMMMM     M::::::Ma::::a    a:::::a  r:::::r                  t:::::t    tttttt\n"
          "PP::::::PP                  y:::::::y        M::::::M               M::::::Ma::::a    a:::::a  r:::::r                  t::::::tttt:::::t\n"
          "P::::::::P                   y:::::y         M::::::M               M::::::Ma:::::aaaa::::::a  r:::::r                  tt::::::::::::::t\n"
          "P::::::::P                  y:::::y          M::::::M               M::::::M a::::::::::aa:::a r:::::r                    tt:::::::::::tt\n"
          "PPPPPPPPPP                 y:::::y           MMMMMMMM               MMMMMMMM  aaaaaaaaaa  aaaa rrrrrrr                      ttttttttttt\n"
          "                          y:::::y\n"
          "                         y:::::y\n"
          "                        y:::::y\n"
          "                       y:::::y\n"
          "                      yyyyyyy                                                                                                                                         \n")
    print("--PyMart; The mini-app Store--")
    print("1. Play Number Guess")
    print("2. Open Diary")
    print("3. Exit")

def mainMenu():
    while True:
        choiceMenu()
        choice = input("\nChoose an option: ")
        if choice == "1":
            Number_Guess.number_guesser()
        elif choice == "2":
            Diary.diary_main()
        elif choice == "3":
            print("Goodbye!")
            break

mainMenu()