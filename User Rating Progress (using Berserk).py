import matplotlib.pyplot as plt
import berserk  # lichess python endpoint
import pandas as pd
from datetime import datetime
from getToken import get_token

LICHESS_TOKEN = get_token()
session = berserk.TokenSession(LICHESS_TOKEN)
client = berserk.Client(session)


def get_user_progression(t_username: str, variant: str, t_client: berserk):
    data = t_client.users.get_rating_history(t_username)

    for element in data:
        if element["name"].find(variant) != -1:

            dates = [       # year       # day             # month
                    datetime(int(x[0]), int(x[1]) + 1, int(x[2]), 0, 0).strftime('%m-%d-%Y')
                    for x in element["points"]
                    ]

            user_progress = [x[3] for x in element["points"]]

            contiguous_dates = []
            contiguous_progress = []

            for i in range(len(dates) - 1):
                in_between_dates = pd.date_range(start=dates[i], end=dates[i+1]).to_pydatetime().tolist()

                for j in range(len(in_between_dates)):
                    contiguous_progress.append(user_progress[i])
                    contiguous_dates.append(in_between_dates[j].strftime('%m-%d-%Y'))

            print(contiguous_dates)
            print(contiguous_progress)
            return contiguous_dates, contiguous_progress


def main():
    usernames = input("Enter comma separated Lichess Usernames: ").split(', ')
    variant = input("Enter Variant: ").capitalize()
    variant_list = ["Classical", "Rapid", "Blitz", "Bullet", "Correspondence"]

    while variant not in variant_list:
        print(f"Invalid Variant! Try: {str(variant_list)}")
        variant = input("Enter Variant: ").capitalize()

    for username in usernames:
        username = username.strip()
        date_list, ratings = get_user_progression(username, variant, client)
        plt.plot([datetime.strptime(d, "%m-%d-%Y") for d in date_list], ratings, label=username)

    plt.xlabel("Dates")
    plt.ylabel(f"Ratings ({variant})")
    plt.legend()
    plt.grid(axis='y')
    plt.show()


if __name__ == "__main__":
    main()
