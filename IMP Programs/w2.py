

    cand1 = input("Enter name of 1st candidate:")
    cand2 = input("Enter name of 2nd candidate:")

    user = input("If u area new user....for registration press y/Y").lower()

    print(f"Candidates:\n1.{cand1}\n2.{cand2}")
    voted = []
    cand1_count = 0
    cand2_count = 0

    while True:
        if len(v_ids) > 0:
            id = int(input("Enter ur id:"))
            if id in v_ids:
                v_ids.remove(id)
                choice = int(input("Vote for candidate choose either 1 0r 2:"))

                if choice == 1:
                    cand1_count = cand1_count + 1
                    voted.append(id)
                    print("Successfully voted")

                elif choice == 2:
                    cand2_count += 1
                    voted.append(id)
                    print("Successfully voted")

                else:
                    print("OOPS!!! Wrong choice")

            elif id in voted:
                print("your are already voted!!")

            else:
                print("wrong id")

        else:
            print("voting completed\n")
            if cand1_count > cand2_count:
                print(f"Winner is {cand1} with {cand1_count} votes....")
                break
            elif cand1_count < cand2_count:
                print(f"Winner is {cand2} with {cand2_count} votes....")
                break
            elif cand1_count == cand2_count:
                print("match tied...")
                break
