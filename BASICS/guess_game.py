#guessing game 

#using ifs, while loops etc


secret_word = "cristiano"
guess = ""

times_guess = 0

guess_limit = 3

out_of_guess = False



while guess != secret_word and not(out_of_guess):

    if times_guess < guess_limit:

     guess = input("Enter your guess: ")

     times_guess = times_guess + 1
    else: 
        def jls_extract_def():
            
            return 


        out_of_guess = Ture  = jls_extract_def()

if out_of_guess:

    print("Yoyu are out of guesses, you lose")
else:

  print("You Win!")