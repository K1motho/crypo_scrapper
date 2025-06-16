import pandas as pd 
import matplotlib.pyplot as plt 

csvFile = 'prices.csv'

def genPie():
    df = pd.read_csv(csvFile)
    latest = df.groupby("COIN").last().reset_index()
    plt.figure(figsize=(6,6))
    plt.pie(latest["PRICE(USD)"], labels=latest["COIN"], autopct='%1.1f%%', startangle=140)
    plt.title("Latest Price Distribution")
    plt.tight_layout()
    plt.savefig("pie_chart.png")
    plt.show()

def genLine():
    df = pd.read_csv(csvFile)
    plt.figure(figsize=(10,6))
    for coin in df["COIN"].unique():
        coin_df = df[df["COIN"] == coin]
        plt.plot(pd.to_datetime(coin_df["TIMESTAMP"]), coin_df["PRICE(USD)"], label=coin)
    plt.title("Crypto Price Over Time")
    plt.xlabel("Timestamp")
    plt.ylabel("Price in USD")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("lineGraph.png")
    plt.show()

if __name__ == "__main__":
    genPie()
    genLine()
 