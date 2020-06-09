from GessGame import GessGame


def main():
    game = GessGame()
    print("Welcome to Gess!\n")
    game.print_board()

    running = True

    while running:

        def quit(input):
            quit_options = ['q', 'quit', 0]
            if  input in quit_options:
                print("Thanks for playing!")
                return False
            return True

        print("== " + game.get_player().title() + "'s turn ==")
        print("Center of Piece to Move: ", end="")
        starting_center = input().lower()
        if not quit(starting_center):
            break
        print("Destination Center: ", end="")
        ending_center = input().lower()
        if not quit(ending_center):
            break

        if game.make_move(starting_center, ending_center):
            game.print_board()
            print()
        
        else:
            print("Invalid move!\n")


if __name__ == "__main__":
    main()
