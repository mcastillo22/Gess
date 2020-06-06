from GessGame import GessGame


def main():
    game = GessGame()
    print("Welcome to Gess!\n")
    game.print_board()

    running = True

    while running:
        print("== " + game.get_player().title() + "'s turn ==")
        print("Piece to move: ", end="")
        starting_center = input().lower()
        print("Destination center: ", end="")
        ending_center = input().lower()
        
        quit_options = ['q', 'quit', 0]

        if  starting_center in quit_options or ending_center in quit_options:
            print("Thanks for playing!")
            running = False
        
        else:
            game.make_move(starting_center, ending_center)
            game.print_board()
            print()


if __name__ == "__main__":
    main()
