import math

def round_up(num: float, to: float) -> float:
    nearest = round(num / to) * to
    if math.isclose(num, nearest): return num
    return nearest if nearest > num else nearest + to

if __name__ == '__main__':
    
    print("Input Backet #1:\n")
    print("1 book at 12.490")
    print("1 music CD at 14.99")
    print("1 chocolate bar at 0.85\n")

    print("Input Backet #2:\n")
    print("1 imported box of chocolates at 10.00")
    print("1 imported bottle of perfume at 47.50\n")

    print("Input Backet #3:\n")
    print("1 imported bottle of perfume at 27.99")
    print("1 bottle of perfume at 18.99")
    print("1 packet of headache pills at 9.75")
    print("1 box of imported chocolates at 11.25\n")

    print("Output for Backet #1:")

    bookPrice = 12.49
    musicCDPrice = 14.99
    chocolateBarPrice = 0.85

    musicTax = (musicCDPrice/10)
    musicCDPrice = musicCDPrice + musicTax
    salesTax = musicTax
    salesTax = round_up(salesTax, 0.05)
    totalPrice = bookPrice + musicCDPrice + chocolateBarPrice

    print("1 book: " + str(bookPrice))
    print(f"1 music CD: {musicCDPrice:.2f}")
    print(f"1 chocolate bar: {chocolateBarPrice:.2f}")
    print(f"Sales Taxes: {salesTax:.2f}")
    print(f"Total: {totalPrice:.2f}" )


    print("\nOutput for Backet #2:")

    importedBoxChocolatesPrice = 10.00
    importedBottlePerfumePrice = 47.50

    importedBoxChocolatesTax = importedBoxChocolatesPrice / 20

    importedBottlePerfumeTax =  importedBottlePerfumePrice / 10
    importedBottlePerfumeTax = importedBottlePerfumeTax + (importedBottlePerfumePrice / 20)
    importedBottlePerfumeTax = round_up(importedBottlePerfumeTax, 0.05)


    salesTax = importedBoxChocolatesTax + importedBottlePerfumeTax

    salesTax = round_up(salesTax, 0.05)

    importedBoxChocolatesPrice = importedBoxChocolatesPrice + importedBoxChocolatesTax
    importedBottlePerfumePrice = importedBottlePerfumePrice + importedBottlePerfumeTax

    totalPrice = importedBoxChocolatesPrice + importedBottlePerfumePrice

    print(f"1 imported box of chocolates: {importedBoxChocolatesPrice:.2f}")
    print(f"1 imported bottle of perfume: {importedBottlePerfumePrice:.2f}")
    print(f"Sales Taxes: {salesTax:.2f}")
    print(f"Total: {totalPrice:.2f}" )




    print("\nOutput for Backet #3:")

    importedBottlePerfumePrice = 27.99
    perfumeBottlePrice = 18.99
    headachePillsPrice = 9.75
    importedChocolatesPrice = 11.25

    importedChocolatesTax = importedChocolatesPrice / 20
    importedChocolatesTax = round_up(importedChocolatesTax, 0.05)

    importedBottlePerfumeTax =  importedBottlePerfumePrice / 10
    importedBottlePerfumeTax = importedBottlePerfumeTax + (importedBottlePerfumePrice / 20)
    importedBottlePerfumeTax = round_up(importedBottlePerfumeTax, 0.05)

    perfumeBottleTax = perfumeBottlePrice / 10

    salesTax = importedChocolatesTax + importedBottlePerfumeTax + perfumeBottleTax
    salesTax = round_up(salesTax, 0.05)

    importedBottlePerfumePrice = importedBottlePerfumePrice + importedBottlePerfumeTax
    perfumeBottlePrice = perfumeBottlePrice + perfumeBottleTax
    importedChocolatesPrice =  importedChocolatesPrice + importedChocolatesTax

    totalPrice = perfumeBottlePrice + importedBottlePerfumePrice + importedChocolatesPrice + headachePillsPrice

    print(f"1 imported bottle of perfume: {importedBottlePerfumePrice:.2f}")
    print(f"1 bottle of perfume: {perfumeBottlePrice:.2f}")
    print(f"1 packet of headache pills: {headachePillsPrice:.2f}")
    print(f"1 imported box of chocolates: {importedChocolatesPrice:.2f}")
    print(f"Sales Taxes: {salesTax:.2f}")
    print(f"Total: {totalPrice:.2f}" )
