def count_characters(start, end):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    hundred = "hundred"
    thousand = "thousand"

    def spell_number(n):
        if n == 0:
            return "zero"
        if n == 1000:
            return "onethousand"

        words = []
        if n >= 100:
            words.append(ones[n // 100])
            words.append(hundred)
            n %= 100
        if 10 <= n < 20:
            words.append(teens[n - 10])
        else:
            if n >= 20:
                words.append(tens[n // 10])
                n %= 10
            if n > 0:
                words.append(ones[n])
        return "".join(words)

    total_characters = 0
    for num in range(start, end + 1):
        total_characters += len(spell_number(num))
    return total_characters

print(count_characters(1, 3))
print(count_characters(41, 41))
print(count_characters(101, 101))
print(count_characters(0, 1000))
