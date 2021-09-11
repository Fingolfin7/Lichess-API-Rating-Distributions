import matplotlib.pyplot as plt
import statistics
import requests
import getToken
import ndjson
import math

LICHESS_TOKEN = getToken.get_token()


def team_members(name: str):
    print(f"Getting '{name}' members...")
    headers = {"Authorization": f"Bearer {LICHESS_TOKEN}"}
    search_req = requests.get(f"https://lichess.org/api/team/{name}/users", headers=headers)
    return ndjson.loads(search_req.content)


def get_user_data(user: dict, variant: str):
    if variant in user['perfs']:
        variant_rating = user['perfs'][variant]['rating']
    else:
        variant_rating = False

    if 'title' in user:
        title = user['title']
    else:
        title = False

    return [variant_rating, title]


# get the inter-quartile range
def get_IQR(data: list):
    if len(data) % 2 == 1:
        median = statistics.median(data)
        upper_half = data[data.index(median):]
        lower_half = data[0: data.index(median) - 1]
    else:
        upper_half = data[len(data) // 2:]
        lower_half = data[0: len(data) // 2]

    return statistics.median(upper_half) - statistics.median(lower_half)


def plotTeamRating(team_data, team_name: str, variant: str):
    ratings = []
    titled_ratings = []

    cm_ratings = []
    nm_ratings = []
    fm_ratings = []
    im_ratings = []
    gm_ratings = []

    for member in team_data:
        if member[0]:
            ratings.append(member[0])

        if member[1]:
            titled_ratings.append(member[0])
            title = member[1]

            if title == "CM":
                cm_ratings.append(member[0])
            elif title == "NM":
                nm_ratings.append(member[0])
            elif title == "FM":
                fm_ratings.append(member[0])
            elif title == "IM":
                im_ratings.append(member[0])
            elif title == "GM":
                gm_ratings.append(member[0])

    def hist_plot():
        ratings.sort()
        # Optimal number of bins in histogram by the Freedman–Diaconis rule
        h = 2 * get_IQR(ratings) * math.pow(len(ratings), -1 * (1 / 3))
        bin_count = math.ceil((max(ratings) - min(ratings)) / h)

        print(f"\nRating count: {len(ratings)}")
        print(f"Titled Count: {len(titled_ratings)}")

        print(f"\nMedian: {statistics.median(ratings)}")
        print(f"Mode: {statistics.mode(ratings)}")
        print(f"Mean: {round(statistics.mean(ratings), 2)}")

        print(f"\nBin Count: {bin_count}")

        plt.hist(ratings, bins=bin_count, label="All Ratings")

        if len(titled_ratings) > 0:
            plt.hist(titled_ratings, bins=bin_count, label="Titled Ratings")
        if len(cm_ratings) > 0:
            plt.hist(cm_ratings, bins=bin_count, label="CM")
        if len(nm_ratings) > 0:
            plt.hist(nm_ratings, bins=bin_count, label="NM")
        if len(fm_ratings) > 0:
            plt.hist(fm_ratings, bins=bin_count, label="FM")
        if len(im_ratings) > 0:
            plt.hist(im_ratings, bins=bin_count, label="IM")
        if len(gm_ratings) > 0:
            plt.hist(gm_ratings, bins=bin_count, label="GM")

    hist_plot()

    plt.title(team_name)
    plt.xlabel(f"Ratings ({variant.capitalize()})")
    plt.ylabel("Users")
    plt.legend()
    plt.show()


def main():
    team_id = input("team-id: ")
    varnt = input("variant: ").lower()

    data_list = [get_user_data(user, varnt) for user in team_members(team_id)]

    plotTeamRating(data_list, team_id, varnt)


if __name__ == "__main__":
    main()
