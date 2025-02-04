from pulp import LpMaximize, LpProblem, LpVariable

def juice_count():
    problem = LpProblem("Maximize_Production", LpMaximize)
    lemonade = LpVariable("Lemonade", lowBound=0, cat='Integer')
    juice = LpVariable("Juice", lowBound=0, cat='Integer')

    problem += lemonade + juice, "Total_Production"
    problem += 2 * lemonade + juice <= 100, "Water"
    problem += lemonade <= 50, "Sugar"
    problem += lemonade <= 30, "LemonJuice"
    problem += 2 * juice <= 40, "FruitPuree"
    problem.solve()

    print(f"Виробити лимонаду: {lemonade.varValue} одиниць")
    print(f"Виробити фруктового соку: {juice.varValue} одиниць")
    print(f"Максимальна кількість продуктів: {lemonade.varValue + juice.varValue}")
    


def main():
    juice_count()

if __name__ == "__main__":
    main()
