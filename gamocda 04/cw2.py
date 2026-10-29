#2)კომენტარების სახით ახსენით თუ რასაკეთებს sort() reverse() count() index() და
#  შექმენით თქვენთვის სასურველი სია მაგ: [“apple”, “grape”, “peach”, “pineaple”] და გააკეთეთ თითო მაგალითი ზემოთ მოცემულ მეთოდებზე
# sort სიას ალაგებს ანბანის მიხედვით და თუ ციფრებია ზრდით
# reverse სიას აბრუნებს
# count სიაში ითვილს სიტყვა ან ციფრი რამდენჟერაც მეორდება
# index ნახულობს რომელ ინდექსზეა რაიმე სიტყვა ან ციფრი
numbers = [1 ,1 ,2, 32, 3, 3,244,6]
numbers.sort()
print (numbers)
print(numbers.count(1))
numbers.reverse()
print(numbers)
print(numbers.index(244))