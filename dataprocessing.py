import pandas as pd
import requests

filename = "data.csv"
appids = pd.read_csv(filename).iloc[:, 10].dropna().astype(int).tolist()

def get_concurrent_players(appids):
    """
    Given a list of Steam AppIDs, return their concurrent player counts.
    """
    base_url = "https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/"
    results = {}

    for appid in appids:
        try:
            response = requests.get(base_url, params={"appid": appid}, timeout=5)
            data = response.json()
            print(data)
            if "response" in data and "player_count" in data["response"]:
                results[appid] = data["response"]["player_count"]
            else:
                results[appid] = None
        except Exception as e:
            results[appid] = f"Error: {e}"

    return results

counts = get_concurrent_players(appids)

df_counts = pd.DataFrame(list(counts.items()), columns=["AppID", "ConcurrentPlayers"])
df_counts.to_csv("concurrent_players.csv", index=False)
