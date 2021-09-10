# Lichess API Rating Distributions
Python project to show the rating distribution of a given Lichess team using the Lichess API.

Simply enter the id of a team, as well as the game variant (i.e Classical, Rapid, Blitz, Bullet etc.)


## Prerequisites
* Python 3
* Matplotlib
* A [Lichess Personal Access Token](https://lichess.org/account/oauth/token)


## Getting the project

Download the project or clone it with git. You can create a virtual environment if you can.
Install the requisites by running

```
pip install -r requirements.txt
```

You will need to create a `personal-access-token.txt` file in the source folder and paste a Lichess Personal Access Token inside it. 
You can generate a genius token [here](https://lichess.org/account/oauth/token)


## Usage Example
Take this team as an example:
 
![image](https://user-images.githubusercontent.com/63872314/132925237-dadb429e-7b5b-4259-802d-63dacc706a7d.png)

The team id can be copied from the url, then we can use that in the program.

![image](https://user-images.githubusercontent.com/63872314/132925330-7b417278-f8cf-4b33-9583-7a0156da5c26.png)

The program will collect the rating information for every member in the team and print the following information to the console before drawing a histogram

![image](https://user-images.githubusercontent.com/63872314/132925402-0d210696-2869-4e9a-affb-4045fa1d12f0.png)


### Output
Finally, the program will plot a histogram showing:

* all ratings,
* titled players,
* GM, CM, NM, IM and FM ratings.

![image](https://user-images.githubusercontent.com/63872314/132925572-25b0818d-c6f8-4640-a3c9-536c7a8af3e0.png)

 
