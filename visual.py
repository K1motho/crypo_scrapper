import pandas as pd 
import matplotlib.pyplot as plt 

csvFile = 'prices.csv'

def genPie():
    df=pd.read_csv(csvFile)
    latest= df.groupby("coin").last().reset_index()
    plt.figure(figsize=(6,6))
    plt.title("Latest Price Distribution")
    plt.tight_layout()
    plt.savefig("pie_chart.png")
    plt.show()

def genLine():
    df=pd.read_csv(csvFile)
    plt.figure(figsize=(10,6))
    for coin in df["coin"].unique():
         coin_df = df[df["coin"] ==coin]
         plt.plot(pd.to_datetime(coin_df["timestamp"]), coin_df["price_usd"], label=coin)
    plt.title("crypto price over time")
    plt.xlabel("Timestamp")
    plt.y("price in USD")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("lineGraph.png")
    plt.show

if  __name == "main":
    genPie()
    genLine