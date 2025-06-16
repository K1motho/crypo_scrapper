from scrapper import fetch_prices, csvsave
from update import initDB, DB_save
from visual import genLine, genPie

def main():
    print("initializing database")
    initDB()
    print("fetching crypto prices ...")
    prices = fetch_prices()
    print("saving to database")
    DB_save(prices)
    csvsave(prices)
    print("prices saved to csv ")

    print("generating visuals")
    genLine()
    genPie()
    print("visual construction complete")

if __name__ == "__main__":
    main()